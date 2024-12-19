from django.urls import path
from .views.llm_ai_views import ask_question_from_ai_view
from .views.llm_system_health_check_views import health_check_view


urlpatterns = [
    # path(
    #     'add-assets-product-vendor-into-monitor-mode',
    #     AddAssetsProductVendorView.as_view(),
    #     name='add-assets-product-vendor-into-monitor-mode'),

    path('ai-subsystem/ask-question-from-ai/', ask_question_from_ai_view, name='ask_question_from_ai'),
    path('ai-subsystem/health-check/', health_check_view, name='health-check'),

]
