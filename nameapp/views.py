from .models import Address
from django.contrib import messages
from django.shortcuts import render, redirect



def home(request):
    if request.method == 'POST':
        address= request.POST.get('address', '').strip()
        if address:
            Address.objects.create(address=address)
            messages.success(request, f'Address "{address}" saved successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please enter a valid address.')
    
    addresses = Address.objects.all()
    return render(request, 'nameapp/home.html', {'addresses': addresses})
