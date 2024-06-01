from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from diams_cms_application.models.categories import Category


class PortalPage(Page):
    parent_page_types = ['home.HomePage']
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL, related_name="portal_pages")
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("category"),
        FieldPanel("description"),
    ]
