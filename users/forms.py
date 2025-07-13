from os import name
from django import forms
from .models import User, TURKISH_CITIES
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine, GlutenFreeRecipe, Category, RecipeCategory
from .turkey_data import DISTRICTS

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Kullanıcı Adı', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}))
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'}))

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre'}))
    role = forms.ChoiceField(choices=User.Role.choices, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'role', 'can_edit_foods', 'can_edit_venues', 'can_edit_hotels', 'can_edit_medicines', 'can_edit_recipes']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}),
            'can_edit_foods': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_venues': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_hotels': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_medicines': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_recipes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'role', 'is_active', 'can_edit_foods', 'can_edit_venues', 'can_edit_hotels', 'can_edit_medicines', 'can_edit_recipes']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_foods': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_venues': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_hotels': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_medicines': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_edit_recipes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'first_name': 'İsim',
            'last_name': 'Soyisim',
            'username': 'Kullanıcı Adı',
            'role': 'Rol',
            'is_active': 'Aktif',
            'can_edit_foods': 'Glutensiz Gıda Yetki',
            'can_edit_venues': 'Glutensiz Mekan Yetki',
            'can_edit_hotels': 'Glutensiz Otel Yetki',
            'can_edit_medicines': 'Glutensiz İlaç Yetki',
            'can_edit_recipes': 'Glutensiz Tarif Yetki',
        }

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Mevcut Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mevcut Şifre'}))
    new_password1 = forms.CharField(label='Yeni Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Şifre'}))
    new_password2 = forms.CharField(label='Yeni Şifre (Tekrar)', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Şifre (Tekrar)'}))

class GlutenFreeFoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['brand'].required = True
        self.fields['category'].required = True
        self.fields['name'].error_messages = {'required': 'İsim alanı zorunludur.'}
        self.fields['brand'].error_messages = {'required': 'Marka alanı zorunludur.'}
        self.fields['category'].error_messages = {'required': 'Kategori alanı zorunludur.'}
        self.fields['category'].empty_label = "Kategori seçin"

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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-select', 'id': 'id_brand'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'id_category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class GlutenFreeVenueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # İlçe alanını zorunlu yap
        initial_city = self.instance.city if self.instance and self.instance.pk else None
        district_choices = [('', 'İlçe seçiniz')]
        
        # Eğer şehir varsa, o şehre ait ilçeleri ekle
        if initial_city and initial_city in DISTRICTS:
            district_choices.extend([(district, district) for district in DISTRICTS[initial_city]])
        
        self.fields['district'].choices = district_choices
        
        # Düzenleme modunda ilçe değerini set et
        if self.instance and self.instance.pk and self.instance.district:
            self.fields['district'].initial = self.instance.district
        self.fields['district'].required = True

    class Meta:
        model = GlutenFreeVenue
        # Formda gösterilecek alanların sırasını düzenlyoruz
        fields = [
            'name', 'city', 'district', 
            'gluten_free_products', 'contact', 'address', 'website', 
            'description', 'is_approved'
        ]
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'Mekan Adı',
            'city': 'Şehir',
            'district': 'İlçe',
            'is_approved': 'Onaylı mı?',
            'description': 'Açıklama',
            'contact': 'İletişim',
            'address': 'Adres',
            'website': 'Web Sitesi',
            'gluten_free_products': 'Glutensiz Ürünler',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-select', 'id': 'id_city'}),
            'district': forms.Select(attrs={'class': 'form-select', 'id': 'id_district'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'gluten_free_products': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        district_choice = cleaned_data.get('district')
        
        # İlçe alanı zorunlu
        if not district_choice:
            self.add_error('district', 'İlçe bilgisi zorunludur.')
        
        return cleaned_data

class GlutenFreeHotelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # İlçe alanını zorunlu yap
        initial_city = self.instance.city if self.instance and self.instance.pk else None
        district_choices = [('', 'İlçe seçiniz')]
        
        # Eğer şehir varsa, o şehre ait ilçeleri ekle
        if initial_city and initial_city in DISTRICTS:
            district_choices.extend([(district, district) for district in DISTRICTS[initial_city]])
        
        self.fields['district'].choices = district_choices
        
        # Düzenleme modunda ilçe değerini set et
        if self.instance and self.instance.pk and self.instance.district:
            self.fields['district'].initial = self.instance.district
        self.fields['district'].required = True

    class Meta:
        model = GlutenFreeHotel
        # Alan listesini otel modeline göre düzenliyoruz
        fields = [
            'name', 'city', 'district', 
            'contact', 'address', 'website', 'description', 'is_approved'
        ]
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'Otel Adı',
            'city': 'Şehir',
            'district': 'İlçe',
            'is_approved': 'Onaylı mı?',
            'description': 'Açıklama',
            'contact': 'İletişim',
            'address': 'Adres',
            'website': 'Web Sitesi',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # ID'ler aynı kalmalı ki JavaScript kodumuz bu formu da etkilesin
            'city': forms.Select(attrs={'class': 'form-select', 'id': 'id_city'}),
            'district': forms.Select(attrs={'class': 'form-select', 'id': 'id_district'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        district_choice = cleaned_data.get('district')
        
        # İlçe alanı zorunlu
        if not district_choice:
            self.add_error('district', 'İlçe bilgisi zorunludur.')
        
        return cleaned_data

class GlutenFreeMedicineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['brand'].required = True
        self.fields['name'].error_messages = {'required': 'İsim alanı zorunludur.'}
        self.fields['brand'].error_messages = {'required': 'Marka alanı zorunludur.'}

    class Meta:
        model = GlutenFreeMedicine
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'İsim',
            'brand': 'Marka',
            'description': 'Açıklama',
            'is_approved': 'Onaylı mı?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-select', 'id': 'id_brand'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class GlutenFreeRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['category'].required = True
        self.fields['name'].error_messages = {'required': 'Tarif adı zorunludur.'}
        self.fields['category'].error_messages = {'required': 'Kategori alanı zorunludur.'}
        self.fields['category'].empty_label = "Kategori seçin"

    class Meta:
        model = GlutenFreeRecipe
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'Tarif Adı',
            'category': 'Kategori',
            'description': 'Açıklama',
            'ingredients': 'Malzemeler',
            'instructions': 'Hazırlanış',
            'created_at': 'Oluşturulma Tarihi',
            'is_approved': 'Onaylı mı?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'id_category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
