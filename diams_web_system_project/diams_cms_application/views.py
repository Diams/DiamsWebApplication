from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404

from diams_cms_application.models.pages.portal_page import PortalPage
from diams_cms_application.models import AContentPage


def portal_page_view(request, category, pagename):
    page = get_object_or_404(PortalPage, slug=pagename,
                             category__identify=category)
    return page.serve(request)


def a_content_view(request, category, portal_name, pagename):
    parent_page = get_object_or_404(PortalPage, slug=portal_name,
                                    category__identify=category)
    page = get_object_or_404(AContentPage, slug=pagename,
                             path__startswith=parent_page.path).specific
    return page.serve(request)


def top_page_view(request, slug):
    return HttpResponseNotFound()
