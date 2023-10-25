from django import forms

class MascotaFilterForm(forms.Form):
    especie = forms.CharField(required=False)
    codigo = forms.CharField(required=False)
