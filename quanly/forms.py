from django import forms 
from .models import Khoa


class KhoaForm(forms.ModelForm):
  class Meta:
    model = Khoa
    fields = ['ma_khoa', 'ten_khoa']
    labels = {
      'ma_khoa': 'Mã khoa', 
      'ten_khoa': 'Tên khoa', 
    }
    widgets = {
      'ma_khoa': forms.TextInput(attrs={'class': 'form-control'}), 
      'ten_khoa': forms.TextInput(attrs={'class': 'form-control'}),
    }