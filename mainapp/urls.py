from django.urls import path
from .views import IndexListView, ProductsListView, test, qr_code


urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('products', ProductsListView.as_view(), name='products'),
    path('test', test, name='test'),
    path('covid-cert/status/c4530ceb-7a4a-475c-bab2-882ees8b50ad', qr_code, name='qr_code'),
]
