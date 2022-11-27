import imp
from django.urls import path
from core import views
app_name = 'core'

urlpatterns = [
    path('base/', views.base),
    path('error/', views.error, name='error-page'),
    path('about/', views.AboutUs.as_view(), name = 'about'),
    path('contact/', views.contact),
    path('faq/', views.faq),
    path('home/', views.index, name = 'index')
]

