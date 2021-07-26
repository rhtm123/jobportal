from django.contrib import admin

# Register your models here.

from .models import Job, Location, JobLocation

class JobLocationInline(admin.TabularInline):
    model = JobLocation
    extra = 1

class JobAdmin(admin.ModelAdmin):
    # summernote_fields = ('materials',)
    list_display = ('title', 'created', 'updated')
    inlines = [JobLocationInline]

admin.site.register(Job, JobAdmin)

admin.site.register(Location)