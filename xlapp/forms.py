from django import forms
from xlapp.models import *

class Profile_Form(forms.ModelForm):
    class Meta:
        model = File
        fields ='__all__'

class CouplingUploadForm(forms.ModelForm):

    coupling_file = forms.FileField(label='XML File Upload:', required=True)

    class Meta:
        model = File
        fields = '__all__'


class ImportExcelForm(forms.Form):
    file  = forms.FileField(label= "Choose excel to upload")