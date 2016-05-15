from django import template
from django.core.files.storage import default_storage

register = template.Library()

@register.simple_tag
def storage(*parts):
    return default_storage.url('/'.join(parts))
