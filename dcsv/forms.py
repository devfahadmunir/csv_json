from django import forms
from .models import csvdata


class csvForm(forms.ModelForm):
    class Meta:
        model = csvdata
        fields = ("name", "csv_file",)


class practiceForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'bootstrappclass'}))
    email = forms.EmailField()
    csv = forms.forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}))  # CharField(widget=forms.FileInput,)
