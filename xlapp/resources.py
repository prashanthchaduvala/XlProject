from import_export import resources
from xlapp.models import *


class FileResource(resources.ModelResource):
    class meta:
        model = File
        fields = '__all__'