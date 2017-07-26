from django.conf.urls import url, include
from post_service.views import post_list

urlpatterns = [
    url(r'^$', post_list)
]