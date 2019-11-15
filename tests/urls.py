from django.conf.urls import include, url
from django.contrib import admin
from tests.views import TestView, TestAPIView


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', TestView.as_view(), name="test-view"),
    url(r'^api/$', TestAPIView.as_view(), name="test-api-view"),

]
