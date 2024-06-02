from django.db import models
from wagtail.snippets.models import register_snippet


@register_snippet
class Category(models.Model):
    priority = models.IntegerField(default=0)
    identify = models.CharField(max_length=255)
    screen_name = models.CharField(max_length=255)

    def __str__(self):
        return self.screen_name

    class Meta:
        verbose_name_plural = "Categories"
