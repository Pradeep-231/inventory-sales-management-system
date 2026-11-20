from django.urls import path
from .views import sales_history,sales_analysis,dashboard

urlpatterns = [
    path('history/', sales_history, name='sales_history'),
    path('analysis/',sales_analysis,name='sales_analysis'),
    path('dashboard/',dashboard,name='dashboard')
]