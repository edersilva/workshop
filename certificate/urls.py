from django.urls import path
from . import views
from .views import CertificateView
app_name = 'certificate'  # This line registers the 'certificate' namespace

urlpatterns = [
    path('', views.list_certificates, name='list'),
    path('<int:certificate_id>/', CertificateView.as_view(), name='detail'),
    # Add other URL patterns as needed
]

