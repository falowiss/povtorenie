from django import forms

class Faculter(forms.Form):
    name = forms.CharField(max_lenght=40)
    hours = forms.IntergerField()



