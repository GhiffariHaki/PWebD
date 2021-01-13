from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#LIST TUGASNYA
class Tugas(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('tugas:tugas_edit', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('tugas:tugas_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Document(models.Model):
    tugas_id = models.ForeignKey(Tugas, default=1, on_delete=models.SET_DEFAULT)
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    assignment = models.FileField(upload_to='submission/')
    nilai = models.IntegerField(blank=True, null=True)
    submitted_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('tugas:assignment_edit', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('tugas:assignment_edit', args=(self.id,))
        return f'<a href="{url}"> {self.nilai} </a>'

