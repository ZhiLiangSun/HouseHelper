from django import forms
from django.contrib.auth.forms import UserCreationForm

Factor_Choices = [
    ('None', '無'),
    ('Accidents', '車禍事故'),
    ('Hospitals', '醫療資源'),
    ('Librarys', '圖書館'),
    ('Markets', '市場'),
    ('Stolens', '竊盜案件')
]


class FactorForm(forms.Form):
    FirstChoices = forms.CharField(label='第一注重', widget=forms.Select(choices=Factor_Choices))
    SecondChoices = forms.CharField(label='第二注重', widget=forms.Select(choices=Factor_Choices))
    ThirdChoices = forms.CharField(label='第三注重', widget=forms.Select(choices=Factor_Choices))


class QueryForm(forms.Form):
    HouseQuery = forms.CharField(label='搜尋', required=False, widget=forms.TextInput(attrs={'placeholder': '搜尋標題或區域'}))


class MessageForm(forms.Form):
    comment = forms.CharField(label='', max_length=200, required=True,
                              widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder': '留下您的評論',
                                                           'font-family': 'Microsoft JhengHei'}))


class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        label="用戶名稱",
    )
    password1 = forms.CharField(
        label="輸入密碼",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="確認密碼",
        widget=forms.PasswordInput,
    )
