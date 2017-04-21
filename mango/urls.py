from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from mango.views import MangoListView

urlpatterns = patterns(
    'mango.views',


    #home page section management with image and texts
    url(r'^list$', MangoListView.as_view(), name='mango-list'),
    # url(r'^slider-image/(?P<section_pk>[0-9]+)/create$', SliderImageCreate.as_view(), name='slider-image-create'),
    # url(r'^slider-image/(?P<image_pk>[0-9]+)/(?P<section_pk>[0-9]+)/update$', SliderImageUpdate.as_view(), name='slider-image-update'),
    # url(r'^slider-image/(?P<image_pk>[0-9]+)/(?P<section_pk>[0-9]+)/delete$', SliderImageDelete.as_view(), name='slider-image-delete'),
    # url(r'^slider-image/(?P<news_pk>[0-9]+)/details$', NewsDetails.as_view(), name='news-details'),
)