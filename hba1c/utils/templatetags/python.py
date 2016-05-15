import __builtin__

from django import template

register = template.Library()

for x in ('repr', 'int', 'str'):
    @register.filter(x)
    def fn(val):
        return getattr(__builtin__, x)(val)
