# catalog/templatetags/my_tags.py

from django import template
from django.conf import settings

register = template.Library()

@register.filter
def mymedia(val):
    """
    Filter to add the /media/ prefix to the file path.
    """
    if val:
        return f'{settings.MEDIA_URL}{val}'
    return '#'