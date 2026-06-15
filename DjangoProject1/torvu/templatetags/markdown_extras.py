import markdown as md
from django import template
from django.template.defaultfilters import stringfilter
from django.urls import NoReverseMatch, reverse

register = template.Library()


@register.filter(name='markdown')
@stringfilter
def markdown_filter(value):
    return md.markdown(
        value,
        extensions=['extra', 'tables', 'sane_lists'],
        output_format='html5',
    )


@register.filter(name='resolve_url')
@stringfilter
def resolve_url(value):
    if not value:
        return value

    if value.startswith('/') or '://' in value:
        return value

    try:
        return reverse(value)
    except NoReverseMatch:
        return value
