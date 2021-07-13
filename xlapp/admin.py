from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from xlapp.models import *

@admin.register(File)
class FieleAdmin(ImportExportModelAdmin):
    list_display = ['file']