from django.template import Library
from django.contrib.sites.models import Site
 
register = Library()


@register.simple_tag(takes_context = True)
def get_current_site_name(context):

    return Site.objects.get_current().name


@register.simple_tag(takes_context = True)
def get_current_site_domain(context):

    return Site.objects.get_current().domain
    
