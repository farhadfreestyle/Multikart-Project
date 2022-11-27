from django.urls import path
from authorization.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterAPI


urlpatterns = [
    path('loginapi/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('loginapi/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registerapi/', RegisterAPI.as_view(), name='api_register'),
]