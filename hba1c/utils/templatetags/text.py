import re

from django import template
from django.utils.crypto import get_random_string

register = template.Library()

re_indent = re.compile("^", re.M)

@register.simple_tag()
def random_string(length=None):
    return get_random_string(length)

@register.filter()
def indent(value, arg=4):
    return re_indent.sub(' ' * int(arg), value)
