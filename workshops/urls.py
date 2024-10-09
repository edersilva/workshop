from django.urls import path
from .views import WorkshopListView

urlpatterns = [
    path('', WorkshopListView.as_view(), name='workshop_list'),
]
