from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('wishlist/', views.wishlist), 
    path('register/', views.register, name='register'),
    path('login/', views.login_user,name='login', ),
    path("login-auth/", views.login_auth, name="login_auth"),
    path('logout-user/', views.logout_user, name='logout', ),
    path("logout-auth/", views.logout_auth, name="logout_auth"),
    path("auth-callback/", views.auth_callback, name="auth_callback"),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password/password_reset_complete.html'), name='password_reset_complete'), 
    path("password_reset", views.password_reset_request, name="password_reset"),
    


]
