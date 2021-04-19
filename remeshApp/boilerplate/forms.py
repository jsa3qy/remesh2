from django import forms

class ConversationForm(forms.Form):
    title = forms.CharField(max_length=200)

class MessageForm(forms.Form):
    title = forms.CharField(max_length=200)

class ThoughtForm(forms.Form):
    text = forms.CharField(max_length=200)

class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=200)