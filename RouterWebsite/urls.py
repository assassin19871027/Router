from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    
    url(r'^logout/', views.show_logout, name='logout'),
    url(r'^home/', views.show_home, name='home'),
    url(r'^login/', views.show_login, name='login'),
    url(r'^registration/', views.show_register, name='register'),
    url(r'^register_done/', views.show_signup, name='sign_up'),
    url(r'^user/', views.show_user, name='user'),
    url(r'^device/(?P<device_name>[^/]+)/', views.show_device, name='device'),
    #url(r"^device/(?P<device_id>\d+)/$", views.show_device, name="device"),
    url(r'^ssid/', views.show_ssid, name='ssid'),
    url(r'^$', views.show_login, name='login'),
)