from django import forms
from django.contrib import admin
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            })
        }