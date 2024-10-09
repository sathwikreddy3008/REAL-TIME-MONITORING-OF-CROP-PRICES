# crop_monitoring_app/forms.py
from django import forms
from .models import CropPrice


class CropPredictionForm(forms.Form):
    crop_data = forms.CharField(label='Crop Data', max_length=100)

class CropPriceForm(forms.ModelForm):
    class Meta:
        model = CropPrice
        fields = ['price']  # Add other fields if needed