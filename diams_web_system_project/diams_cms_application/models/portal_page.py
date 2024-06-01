from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from diams_cms_application.app_utils.categories import MAJOR_CATEGORIES


class PortalPage(Page):
    parent_page_types = ['home.HomePage']
    category = models.CharField(
        max_length=255, choices=MAJOR_CATEGORIES, default=list(MAJOR_CATEGORIES.keys())[0])
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("category"),
        FieldPanel("description"),
    ]
