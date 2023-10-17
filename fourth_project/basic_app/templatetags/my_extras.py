from django import template

register = template.Library()

def custom_filter(value, arg):
    """

    this cuts out all values of "arg" from the string!
    """

    return value.replace(arg, '')

register.filter('custom_filter', custom_filter)