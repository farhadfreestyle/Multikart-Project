import imp
from django.urls import path
from . import views
from api import views


urlpatterns = [
    path("productapi/", views.ListProductAPIView.as_view(), name="product_list"),
    path("productapi/create/", views.CreateProductAPIView.as_view(), name="product_create"),
    path("productapi/update/<int:pk>/", views.UpdateProductAPIView.as_view(), name="update_product"),
    path("productapi/delete/<int:pk>/", views.DeleteProductAPIView.as_view(), name="delete_product"),
    path("productapi/retrieve/<int:pk>/", views.RetrieveProductAPIView.as_view(), name="retrieve_product"),
    path('api/create', views.Createview.as_view()),
    path('api/list', views.Listview.as_view()),
    path('api/update/<int:pk>', views.Updateview.as_view()),
    path('api/delete/<int:pk>', views.Deleteview.as_view()),
    path('cartapi/', views.ListCartAPIView.as_view()),
]