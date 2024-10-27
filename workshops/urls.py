from django.urls import path
from .views import WorkshopListView, WorkshopDetailView, WorkshopAccountListView, join_workshop

urlpatterns = [
    path('', WorkshopListView.as_view(), name='workshop_list'),
    path('<int:pk>/', WorkshopDetailView.as_view(), name='workshop_detail'),
    path('workshop/join/<int:workshop_id>/', join_workshop, name='join_workshop'),
    path('workshops/list/', WorkshopAccountListView.as_view(), name='workshop_account_list'),
]
    