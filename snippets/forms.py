from django import forms
from .models import Snippet, Language, Framework

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'description', 'language', 'framework']
    

class SnippetUpdateForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'description', 'language', 'framework']


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']


class FrameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = ['name', 'language']

