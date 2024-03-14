from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Patient, Prescriptions
from .forms import CustomUserCreationForm, LoginForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    add_form = LoginForm
    list_display = ['username', 'email', 'role']

@admin.register(Patient)
class UserPatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email', 'birth_date'] 
    search_fields = ('name', 'email')   

@admin.register(Prescriptions)
class Prescription(admin.ModelAdmin):
    list_display = ['first_name', 'description']
# prescription class










