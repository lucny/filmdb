from django.contrib import admin
# Import modelů ze souboru models.py
from .models import Genre

# Registrace nového modelu v administraci
admin.site.register(Genre)