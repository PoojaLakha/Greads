from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    # User profile
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

]
