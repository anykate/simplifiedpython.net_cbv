from django.urls import path
from . import views

app_name = 'genericviews'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('details/<int:product_id>/', views.ProductDetailView.as_view(), name='details'),
    path('save/', views.saveproducttodb, name='save'),
]
