from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Certificate

@login_required
def list_certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    context = {
        'certificates': certificates,
        'title': 'Certificados',
    }
    return render(request, 'certificate/list.html', context)

