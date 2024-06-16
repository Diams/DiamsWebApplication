from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

from diams_cms_application.models import AContentPage


class BlogPage(AContentPage):
    body = RichTextField(blank=True, null=True)

    content_panels = AContentPage.content_panels + [
        FieldPanel("body"),
    ]
