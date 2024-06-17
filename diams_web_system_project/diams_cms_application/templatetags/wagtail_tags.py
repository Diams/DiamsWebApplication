from django import template
from wagtail.query import PageQuerySet

from home.models import HomePage

register = template.Library()


@register.simple_tag
def get_home_page():
    try:
        home_page_query: PageQuerySet = HomePage.objects
        home_page = home_page_query.live().public().first()
        home_page: HomePage = home_page.url
        return home_page
    except HomePage.DoesNotExist:
        return "/"
