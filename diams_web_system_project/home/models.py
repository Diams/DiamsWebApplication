from wagtail.models import Page
from wagtail.query import PageQuerySet

from diams_cms_application.models.categories import Category


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        categories = Category.objects.all().order_by("priority")
        children: PageQuerySet = self.get_children()
        children = children.live().specific()
        navigation_categories = {
            category.identify: (
                category.screen_name,
                children.filter(portalpage__category=category)
            ) for category in categories
        }
        context["navigation_categories"] = navigation_categories
        return context
