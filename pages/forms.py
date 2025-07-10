from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'Ad Soyad',
            'email': 'E-posta',
            'subject': 'Konu',
            'message': 'Mesaj',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız ve Soyadınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta adresiniz'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Konu'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız', 'rows': 5}),
        }
