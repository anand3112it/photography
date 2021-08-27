from django import template
from datetime import datetime
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def get_date(ip_date):
	return ip_date.strftime('%d')

@register.simple_tag
def get_month(ip_date):
	return ip_date.strftime('%b')

@register.simple_tag
def get_day_month_year(ip_date):
	return ip_date.strftime('%d %b %y')

@register.filter
def get_item(dictionary, key):
	return dictionary[key]

@register.simple_tag
def load_error_box(err):
	if not err:
		return ''

	return mark_safe('<span class="error-message" style="display: block; color: red; opacity: 1">{}</span>'.format(err))
