from django.urls import path
from .views import AddAssetsProductVendorView

urlpatterns = [
    path('add-assets-product-vendor-into-monitor-mode', AddAssetsProductVendorView.as_view(), name='add-assets'),
]