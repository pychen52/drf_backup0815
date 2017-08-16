from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns
from weather import views
from django.views.generic.base import RedirectView

urlpatterns = [ 
    url(r'^weather/(?P<pk>[0-9]+)/$', views.LightList.as_view()),
    url(r'^weather/(?P<Region>.+&P<Date>.+)/$',views.LightList.as_view()),
    url(r'^.*$', views.LightList.as_view(), name='weather_list'),
]
                                         
urlpatterns = format_suffix_patterns(urlpatterns)

