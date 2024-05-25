from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=20)
    country = forms.CharField(required=False)
    birthday = forms.DateField()
