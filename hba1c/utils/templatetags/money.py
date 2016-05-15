from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter
def money(cents):
    return floatformat(cents / 100., 2)

@register.filter
def money_quantity(cents, quantity):
    return floatformat(cents * quantity / 100., 2)

@register.filter
def money_compact(cents):
    quotient, remainder = divmod(cents, 100)

    if remainder != 0:
        return money(cents)

    return quotient
