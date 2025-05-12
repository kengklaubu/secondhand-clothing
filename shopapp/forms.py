# apps/core/forms.py
from django import forms
from .models import ClothingItem

class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = ['title', 'description', 'category', 'price', 'image', 'is_for_sale']
