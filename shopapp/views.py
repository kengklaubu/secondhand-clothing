# apps/core/views.py
from django.shortcuts import render, redirect
from .models import ClothingItem
from .forms import ClothingItemForm

def home(request):
    items = ClothingItem.objects.all()
    return render(request, 'home.html', {'items': items})

# apps/core/views.py
from django.shortcuts import render, redirect
from .models import ClothingItem
from .forms import ClothingItemForm

def add_item(request):
    if request.method == 'POST':
        form = ClothingItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClothingItemForm()
    return render(request, 'add_item.html', {'form': form})

