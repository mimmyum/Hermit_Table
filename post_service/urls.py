from django.conf.urls import url, include
from post_service.views import post_list, post_list_mobile_ruli, post_list_mobile

urlpatterns = [
    url(r'^$', post_list),
    url(r'^mobile$', post_list_mobile),
    url(r'^mobile/ruli$', post_list_mobile_ruli)
]