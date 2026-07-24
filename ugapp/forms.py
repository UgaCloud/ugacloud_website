from django import forms

from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email',
                'required': True,
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject',
                'required': True,
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                'rows': 5,
            }),
        }
