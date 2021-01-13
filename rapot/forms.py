from django import forms
from django.forms import ModelForm
from .models import TemplateKPI, TemplateNilai, Rapot

class TemplateNilaiForm(forms.ModelForm):
    class Meta :
        model = TemplateNilai
        fields = ['nilai']

class TemplateKPIForm(forms.ModelForm):
    class Meta :
        model = TemplateKPI
        fields = ['KPI']

class RapotForm(forms.ModelForm):
    class Meta :
        model = Rapot
        fields = ['nilai', 'realisasiNilai', 'KPI', 'realisasiKPI']