from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^vc/', views.index, name="e"),
    url(r'^$', views.index, name="inicio" ),
    url(r'^contenido/', views.MeetingListView.as_view(), name='contenido'),
    url(r'^(?P<slug>[-\w]+)/$', views.MeetingDetailView.as_view(), name='meeting-display' )

]



