from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Name


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            Name.objects.create(name=name)
            messages.success(request, f'Name "{name}" saved successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please enter a valid name.')
    
    names = Name.objects.all()
    return render(request, 'nameapp/home.html', {'names': names})
