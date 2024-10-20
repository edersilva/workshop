from django.urls import path
from .views import WorkshopListView, WorkshopDetailView, favorite_workshop, join_workshop

urlpatterns = [
    path('', WorkshopListView.as_view(), name='workshop_list'),
    path('<int:pk>/', WorkshopDetailView.as_view(), name='workshop_detail'),
    path('api/favorite-workshop/<int:workshop_id>/', favorite_workshop, name='favorite_workshop'),
    path('api/join-workshop/<int:workshop_id>/', join_workshop, name='join_workshop'),
]
    