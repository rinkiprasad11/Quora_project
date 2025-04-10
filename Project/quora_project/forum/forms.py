from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter the question title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe the question...'}))

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your answer...'}))