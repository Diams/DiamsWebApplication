from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class PortalPage(Page):
    description = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]
