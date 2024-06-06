from django import forms
from .models  import Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'gender']

# forms.py
from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']


