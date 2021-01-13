from django.db import models
from django.contrib.auth.models import User

class TemplateNilai(models.Model):
    nilai = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nilai

class TemplateKPI(models.Model):
    KPI = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.KPI

class Rapot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nilai = models.ForeignKey(TemplateNilai, on_delete=models.CASCADE)
    realisasiNilai = models.FloatField(default=0, blank=True, null= False)
    KPI = models.ForeignKey(TemplateKPI, on_delete=models.CASCADE)
    realisasiKPI = models.FloatField(default=0, blank=True, null=False)