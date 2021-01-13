from django.urls import path

from . import views

app_name = 'rapot'

urlpatterns = [
    path('', views.RapotView.as_view(), name='list_rapot'),
    path('newNilai/', views.create_templateNilai, name='templateNilai_new'),
    path('newKPI/', views.create_templateKPI, name='templateKPI_new'),
    path('<int:user_id>/detail/', views.rapot_details, name="detail_rapot"),
    path('add_detailrapot/<int:user_id>', views.add_detailrapot, name='add_detailrapot'),
]