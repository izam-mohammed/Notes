from django.contrib import admin
from .models import Notes

# Register the Notes model with the Django admin site.

# This allows administrators to manage Notes data through the admin interface.
admin.site.register(Notes)
