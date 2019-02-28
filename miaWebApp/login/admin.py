from django.contrib import admin
from .models import Login

# Register your models here.


class LoginAdmin(admin.ModelAdmin):
    # deve essere in modo che stampi la matricola a sinistra.
    list_display = ["__str__", "username"]
    prepopulated_fields = {"slug": ("username",)}

class Meta:
    model = Login

admin.site.register(Login, LoginAdmin)