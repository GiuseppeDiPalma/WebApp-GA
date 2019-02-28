from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length = 10)
    password = models.CharField(max_length = 5)
    data_login = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    slug = models.SlugField()

    def __str__(self):
        return self.username