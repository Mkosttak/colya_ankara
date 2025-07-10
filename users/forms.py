from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine, GlutenFreeRecipe

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Kullanıcı Adı', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}))
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'}))

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'}))
    role = forms.ChoiceField(choices=User.Role.choices, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'role']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Mevcut Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mevcut Şifre'}))
    new_password1 = forms.CharField(label='Yeni Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Şifre'}))
    new_password2 = forms.CharField(label='Yeni Şifre (Tekrar)', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Şifre (Tekrar)'}))

class GlutenFreeFoodForm(forms.ModelForm):
    class Meta:
        model = GlutenFreeFood
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'İsim',
            'brand': 'Marka',
            'category': 'Kategori',
            'is_approved': 'Onaylı mı?',
            'description': 'Açıklama',
        }

class GlutenFreeVenueForm(forms.ModelForm):
    class Meta:
        model = GlutenFreeVenue
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'İsim',
            'is_approved': 'Onaylı mı?',
            'description': 'Açıklama',
            'contact': 'İletişim',
            'address': 'Adres',
            'gluten_free_products': 'Glutensiz Ürünler',
        }

class GlutenFreeHotelForm(forms.ModelForm):
    class Meta:
        model = GlutenFreeHotel
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'İsim',
            'is_approved': 'Onaylı mı?',
            'description': 'Açıklama',
            'contact': 'İletişim',
            'address': 'Adres',
        }

class GlutenFreeMedicineForm(forms.ModelForm):
    class Meta:
        model = GlutenFreeMedicine
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'İsim',
            'brand': 'Marka',
            'is_approved': 'Onaylı mı?',
        }

class GlutenFreeRecipeForm(forms.ModelForm):
    class Meta:
        model = GlutenFreeRecipe
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'İsim',
            'description': 'Açıklama',
            'created_at': 'Oluşturulma Tarihi',
        }
