from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Rapot, TemplateKPI, TemplateNilai, User
from .forms import RapotForm, TemplateKPIForm, TemplateNilaiForm

# Create your views here.
class RapotView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'listrapot.html'

def create_templateNilai(request):   
    form = TemplateNilaiForm(request.POST or None)
    if request.POST and form.is_valid():
        nilai = form.cleaned_data['nilai']
        TemplateNilai.objects.get_or_create(
            nilai=nilai,
        )
        return redirect('rapot:list_rapot')
    else:
        form = TemplateNilaiForm()
    context = {
        'form' : form,
    }
    return render(request, 'rapottemplateform.html', context)


def create_templateKPI(request):   
    form = TemplateKPIForm(request.POST or None)
    if request.POST and form.is_valid():
        KPI = form.cleaned_data['KPI']
        TemplateKPI.objects.get_or_create(
            KPI=KPI,
        )
        return redirect('rapot:list_rapot')
    else:
        form = TemplateKPIForm()
    context = {
        'form' : form,
    }
    return render(request, 'rapottemplateKPIform.html', context)

@login_required
def rapot_details(request, user_id):
    user = User.objects.get(id=user_id)
    rapot = Rapot.objects.filter(user=user)
    context = {
        'user': user,
        'rapot': rapot
    }
    return render(request, 'rapot_details.html', context)

def add_detailrapot(request, user_id):
    forms = RapotForm()
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        forms = RapotForm(request.POST)
        if forms.is_valid():
            nilai = forms.cleaned_data['nilai']
            realisasiNilai = forms.cleaned_data['realisasiNilai']
            KPI = forms.cleaned_data['KPI']
            realisasiKPI = forms.cleaned_data['realisasiKPI']
            Rapot.objects.create(
                user=user,
                nilai=nilai,
                realisasiNilai=realisasiNilai,
                KPI=KPI,
                realisasiKPI=realisasiKPI,
            )
    context = {
        'form': forms
    }
    return render(request, 'add_detailrapot.html', context)