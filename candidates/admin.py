from django.contrib import admin

from .models import Candidate


# admin.site.register(Candidate)
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'age']
