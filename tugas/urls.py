from django.urls import path

from tugas import views

app_name = 'tugas'

urlpatterns = [
    path('', views.TugasView.as_view(), name='list_tugas'),
    path('new/', views.create_tugas, name='tugas_new'),
    path('<int:pk>/edit/', views.TugasEdit.as_view(), name='tugas_edit'),
    path('<int:tugas_id>/assign/', views.upload_file, name="assignment"),
    path('<int:tugas_id>/listassign/', views.list_assignment, name="list_assignment"),
    path('<int:pk>/edit/document/', views.PenilaianDocument.as_view(), name='assignment_edit'),
]