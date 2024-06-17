import importlib

from django.db import models
from wagtail.admin.panels import FieldPanel

from diams_cms_application.models import AContentPage


class OtherAppPage(AContentPage):
    application_name = models.CharField(max_length=255, blank=True, null=True)
    view_obj_name = models.CharField(max_length=255, blank=True, null=True)

    content_panels = AContentPage.content_panels + [
        FieldPanel("application_name"),
        FieldPanel("view_obj_name"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["contents"] = "this is other app's contents"
        if isinstance(self.application_name, str):
            try:
                application = importlib.import_module(
                    self.application_name + ".contents")
                context["contents"] = getattr(
                    application, "get_contents")(self.view_obj_name, request)
            except ModuleNotFoundError:
                context["contents"] = "指定したアプリケーションは存在しません"
            except AttributeError:
                context["contents"] = "指定したビューは存在しません"
        return context
