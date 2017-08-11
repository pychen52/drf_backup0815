from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns
from weather import views
from django.views.generic.base import RedirectView

urlpatterns = [ 
    url(r'^rainfall/$', views.RainfallList.as_view()),
    url(r'^rainfall/(?P<pk>[0-9]+)/$', views.RainfallDetail.as_view()),
    url(r'^stations/(?P<Region>.+&P<Date>.+)/$',views.StationList.as_view()),
    url(r'^.*$', views.StationList.as_view(), name='station_list'),
]
                                         
urlpatterns = format_suffix_patterns(urlpatterns)

