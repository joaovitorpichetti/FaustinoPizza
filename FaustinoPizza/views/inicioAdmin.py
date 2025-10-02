from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def inicioAdmin(request):
    context = {
        'nome': request.user.first_name,
    }
    return render(request, 'inicioAdmin.html', context)
