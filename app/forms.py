from tkinter import Widget
from django import forms
from django.db.models import fields

from app.models import Question


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name",widget=forms.TextInput(attrs={'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(max_length=30, label="Last Name",widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), required=True)
    college_email = forms.EmailField(
        max_length=120, label="College Email",widget=forms.EmailInput(attrs={'placeholder': 'College Email id'}), required=True
    )
    password = forms.CharField(
        max_length=30, label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True
    )


class LoginForm(forms.Form):
    college_email = forms.EmailField(
        max_length=120, label="College Email", widget=forms.EmailInput(attrs={'placeholder': 'College Email id'}), required=True
    )
    password = forms.CharField(
        max_length=30, label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True
    )   


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("text", "department")
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Type your question here...'})
        }


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your answer here...'}), required=True, label="Answer" )
    
