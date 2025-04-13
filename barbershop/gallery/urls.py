from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_home, name='gallery'),
    path('upload/', views.upload_image, name='upload_image'),
    path('category/<slug:category>/', views.gallery_category, name='gallery_category'),
]
