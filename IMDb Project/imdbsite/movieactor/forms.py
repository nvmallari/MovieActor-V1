from django import forms

class NameForm(forms.Form):
    name1 = forms.CharField(label='Movie 1', max_length=100)
    name2 = forms.CharField(label='Movie 2', max_length=100)