from datetime import datetime, date
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Tugas, Document
from .forms import TugasForm, DocumentForm

class TugasView(LoginRequiredMixin, generic.ListView):
    model = Tugas
    template_name = 'listtugas.html'
    context = {
        'tugas' : Tugas,
    }

@login_required
def create_tugas(request):    
    form = TugasForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        deadline = form.cleaned_data['deadline']
        Tugas.objects.get_or_create(
            title=title,
            description=description,
            deadline=deadline,
            created_date=datetime.now(),
        )
        return redirect('tugas:list_tugas')
    else:
        form = TugasForm()
    context = {
        'form' : form,
    }
    return render(request, 'tugasform.html', context)

class TugasEdit(generic.UpdateView):
    model = Tugas
    fields = ['title', 'description', 'deadline']
    template_name = 'tugasform.html'
    success_url = reverse_lazy('tugas:list_tugas')

@login_required
def upload_file(request, tugas_id):
    form = DocumentForm()
    tugas = Tugas.objects.get(id=tugas_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            assignment = form.cleaned_data['assignment']
            Document.objects.create(
                tugas_id=tugas,
                user_id=request.user,
                description=description,
                assignment=assignment,
                submitted_date=datetime.now()
            )
            return redirect('tugas:list_tugas')
    else:
        form = DocumentForm()
    context = {
        'form' : form,
        'assignmenttugas' : tugas
    }
    return render(request, 'assignment_tugas.html', context)

@login_required
def list_assignment(request, tugas_id):
    tugas = Tugas.objects.get(id=tugas_id)
    document = Document.objects.filter(tugas_id_id=tugas)
    context = {
        'tugas': tugas,
        'document': document
    }
    return render(request, 'assignment_list.html', context)

class PenilaianDocument(SuccessMessageMixin, generic.UpdateView):
    model = Document
    fields = ['nilai']
    template_name = 'assignment_penilaian.html'