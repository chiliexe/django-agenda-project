from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contato(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=180, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'pk': self.pk})