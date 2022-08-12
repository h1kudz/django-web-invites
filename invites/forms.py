from django import forms
from .models import Invites


class InvitesForm(forms.ModelForm):
    class Meta:
        model = Invites
        #fields = '__all__'
        fields = ['name', 'comment', 'is_confirm']
        choices = ((True, 'Обязательно буду!'), (False, 'К сожалению, не смогу ...'),)
        widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control'}),
             'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
             'is_confirm': forms.RadioSelect(attrs={'class': 'form-check-input', 'name':'rating'}, choices=choices),
        }
