from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(label='имя:', max_length=20)
    country = forms.CharField(label='страна', required=False, help_text='Необязательное поле')
    birthday = forms.DateField(label='год', help_text='только год')
