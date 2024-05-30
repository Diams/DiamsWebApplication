from wagtail.models import Page

from diams_cms_application.app_utils.categories import MAJOR_CATEGORIES


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        navigation_categories = {
            key: (MAJOR_CATEGORIES[key], []) for key in MAJOR_CATEGORIES
        }
        # 全てのmodelを調査し、カテゴリごとにグループ化。後で実装する。
        context["navigation_categories"] = navigation_categories
        return context
