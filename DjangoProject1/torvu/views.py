from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404, render
from .models import Post

from torvu.models import my_photos, RequestAssistanceModel


# Create your views here.


def home(request):
    good_feed_posts = Post.objects.filter(post_type=Post.Post_Type.GOOD_FEED).order_by('-created_at')[:6]
    news_posts = Post.objects.filter(post_type=Post.Post_Type.NEWS).order_by('-created_at')[:6]
    guide_posts = Post.objects.filter(post_type=Post.Post_Type.GUIDE).order_by('-created_at')[:6]
    testimonial_posts = Post.objects.filter(post_type=Post.Post_Type.TESTIMONIAL).order_by('-created_at')[:6]
    return render(request, 'index.html', {
        'good_feed_posts': good_feed_posts,
        'news_posts': news_posts,
        'guide_posts': guide_posts,
        'testimonial_posts': testimonial_posts,
    })

@never_cache
def request_assistance_form(request):

    if request.method == 'POST':
        if request.session.get("submitted"):
            return redirect("torvu:success_page")

        assistance = RequestAssistanceModel.objects.create(
            first_name=request.POST.get('first-name'),
            last_name=request.POST.get('last-name'),
            date_of_birth=request.POST.get('date_of_birth'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            country=request.POST.get('country'),
            postal=request.POST.get('postal'),
            gender=request.POST.get('gender'),

            edu_level=request.POST.get('edu-level'),
            edu_major=request.POST.get('edu-major'),
            edu_grad_year=request.POST.get('edu-grad-year'),
            edu_institution=request.POST.get('edu-institution'),
            edu_inst_location=request.POST.get('edu-inst-location'),
            edu_certs=request.POST.get('edu-certs'),

            emp_status=request.POST.get('emp-status'),
            emp_title=request.POST.get('emp-title'),
            emp_employer=request.POST.get('emp-employer'),
            emp_address=request.POST.get('emp-address'),
            emp_start=request.POST.get('emp-start'),
            emp_end=request.POST.get('emp-end') or None,
            emp_ssn=request.POST.get('emp-ssn'),
            emp_ssn_confirm=request.POST.get('emp-ssn-confirm'),
            emp_summary=request.POST.get('emp-summary'),

            upload_w4=request.FILES.get('upload-w4'),
            upload_i9=request.FILES.get('upload-i9'),

            id_type=request.POST.get('id-type'),
            id_number=request.POST.get('id-number'),
            id_state=request.POST.get('id-state'),
            id_issue=request.POST.get('id-issue'),
            id_expiry=request.POST.get('id-expiry'),

            id_upload_front=request.FILES.get('id-upload-front'),
            id_upload_back=request.FILES.get('id-upload-back'),
            id_upload_selfie=request.FILES.get('id-upload-selfie'),

            terms_agree=True,
        )
        assistance.save()
        request.session['submitted'] = True
        return redirect('torvu:success_page')
    return render(request, 'request_assistance_form.html', {})

def dummy_form(request):

    if request.method == 'POST':
        photo_name = request.POST['photo_name']
        photo_description = request.POST['photo_description']
        photo = request.FILES['image']
        print(photo)
        my_photos.objects.create(photo_name=photo_name, photo_description=photo_description, image=photo)

    return render(request, 'dummy_form.html', {})


def success_page(request):
    return render(request, 'success_page.html', {})


def blog_post1(request):
    blogs = Post.objects.all()
    return render(request, 'blog_post.html', {'blogs': blogs})


# views.py

def blog_post(request, slug):
    post = get_object_or_404(
        Post.objects.prefetch_related('blocks', 'tags'),
        slug=slug,
    )
    featured = Post.objects.all().exclude(pk=post.pk).order_by('-created_at')[:6]

    return render(request, 'blog/post.html', {
        'post': post,
        'featured': featured,
    })

def blog_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(
        tags=tag,
        status=Post.Status.PUBLISHED
    ).order_by('-created_at')

    return render(request, 'blog/tag.html', {
        'tag': tag,
        'posts': posts,
    })

def stay_informed(request):
    feel_good_posts = Post.objects.filter(post_type=Post.Post_Type.GOOD_FEED).order_by('-created_at')[:6]
    news_posts = Post.objects.filter(post_type=Post.Post_Type.NEWS).order_by('-created_at')[:6]
    testimonials = Post.objects.filter(post_type=Post.Post_Type.TESTIMONIAL).order_by('-created_at')[:6]
    guides = Post.objects.filter(post_type=Post.Post_Type.GUIDE).order_by('-created_at')[:6]
    return render(request, 'stay_informed_page.html', {
        'feel_good_posts': feel_good_posts,
        'news_posts': news_posts,
        'testimonials': testimonials,
        'guides': guides
        })


def about(request):
    return render(request, 'about_page.html', {})

def contact(request):
    return render(request, 'contact_page.html', {})