from django.urls import path
from .views import WorkshopListView, WorkshopDetailView

urlpatterns = [
    path('', WorkshopListView.as_view(), name='workshop_list'),
    path('<int:pk>/', WorkshopDetailView.as_view(), name='workshop_detail'),
]
