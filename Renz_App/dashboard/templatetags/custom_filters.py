from django import template
import locale

register = template.Library()

@register.filter
def currency_format(value):
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        return locale.currency(float(value), grouping=True, symbol=True)
    except:
        return f"${value:,.2f}"

@register.filter
def number_format(value):
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        return "{:,}".format(int(value))
    except:
        return value 