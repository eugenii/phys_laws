from django import forms
from .models import Laws


class LawForm(forms.ModelForm):
    # Все описания удалены, настройки в Meta

    class Meta:
        model = Laws
        fields = '__all__'
         