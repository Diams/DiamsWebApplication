from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404

from diams_cms_application.models.pages.portal_page import PortalPage


def portal_page_view(request, category, pagename):
    page = get_object_or_404(PortalPage, slug=pagename,
                             category__identify=category)
    return page.serve(request)


def top_page_view(request, slug):
    return HttpResponseNotFound()
