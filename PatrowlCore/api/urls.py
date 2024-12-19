from django.urls import path
from .views.integration_views import AddAssetsProductVendorView
from .views.llm_ai_views import ask_question_from_ai_view


urlpatterns = [
    path(
        'add-assets-product-vendor-into-monitor-mode',
        AddAssetsProductVendorView.as_view(),
        name='add-assets-product-vendor-into-monitor-mode'),


    path('ask-question-from-ai/', ask_question_from_ai_view, name='ask_question_from_ai'),

]
