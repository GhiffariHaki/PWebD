from django import forms
from django.forms import ModelForm, DateInput
from .models import Tugas, Document

class TugasForm(forms.ModelForm):
    class Meta :
        model = Tugas
        widgets = {
            'deadline': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }
        exclude = ['created_date']

    def __init__(self, *args, **kwargs):
        super(TugasForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['deadline'].input_formats = ('%Y-%m-%dT%H:%M',)

class DocumentForm(forms.ModelForm):
    class Meta :
        model = Document
        fields = ['description', 'assignment']