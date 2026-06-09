from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect

from torvu.models import my_photos, RequestAssistanceModel


# Create your views here.


def home(request):
    return render(request, 'index.html', {})

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