from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseNotFound
from .models import Certificate  # Add Workshop import

@login_required
def list_certificates(request):
    certificates = Certificate.objects.all()
    context = {
        'certificates': certificates,
        'title': 'Certificados',
    }
    return render(request, 'certificate/list.html', context)

class CertificateView(View):
    template_name = 'certificate/certificate.html'

    def get(self, request, certificate_id):
        certificate = Certificate.objects.filter(workshops=certificate_id).first()
        workshop = certificate.workshops.first() if certificate else None
        
        context = {
            'full_name': f"{request.user.first_name} {request.user.last_name}",
            'title': "Certificados",
            'certificate': certificate,
            'workshop': workshop,
            'error_message': None
        }

        if not certificate:
            context['error_message'] = "Certificado não encontrado."
        elif not workshop:
            context['error_message'] = "Workshop não encontrado para este certificado."

        return render(request, self.template_name, context)
