from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # password reset
    url(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ), name='password_reset'),
    url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    # change password after account login
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='password_change_done.html'),
        name='password_change_done'),

    # User profile
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

]
