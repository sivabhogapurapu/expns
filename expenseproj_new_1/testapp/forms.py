from django import forms
from django.contrib.auth.models import User
from testapp.models import Expenses

class ExpForm(forms.ModelForm):
    purchasedate = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                 input_formats=('%d/%m/%Y',))
    class Meta:
        model=Expenses
        fields='__all__'

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Login
#         fields = '__all__'
