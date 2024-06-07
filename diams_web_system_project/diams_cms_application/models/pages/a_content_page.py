from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from diams_cms_application.models import Category
from diams_cms_application.models import PortalPage


class AContentPage(Page):
    parent_page_types = ['diams_cms_application.PortalPage']

    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        categories = Category.objects.all().order_by("priority")
        portal_pages = PortalPage.objects.all()
        navigation_categories = {
            category.identify: (
                category.screen_name,
                portal_pages.filter(category=category),
            ) for category in categories
        }
        context["navigation_categories"] = navigation_categories
        return context
