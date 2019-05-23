from django import forms
from django.contrib.auth import get_user_model


class EmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
        if get_user_model().objects.filter(email=data).first():
            raise forms.ValidationError("That email is already taken. Please enter another email.")
        return data
