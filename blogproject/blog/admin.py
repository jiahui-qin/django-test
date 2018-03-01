from django.contrib import admin

# Register your models here.
from .models import meta
class metaAdmin(admin.ModelAdmin):
    list_display = ['metabolomics', 'mz', 'rt', 'provider', 'updatetime']
admin.site.register(meta, metaAdmin)