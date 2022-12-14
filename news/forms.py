from django import forms
from .models import News
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text= "Имя пользователя должно состоять макс из 150 символов",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'autocomplete': "off"
                                                             }))
    email = forms.CharField(label='Почта',
                               widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Подверждение пароля',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'autocomplete': "off"
                                                             }))

    password = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
