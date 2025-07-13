from os import name
from django import forms
from .models import User, TURKISH_CITIES
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine, GlutenFreeRecipe, Category

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
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        empty_label="Kategori seçin",
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_category'}),
        label="Kategori"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['brand'].required = True
        self.fields['category'].required = True
        self.fields['name'].error_messages = {'required': 'İsim alanı zorunludur.'}
        self.fields['brand'].error_messages = {'required': 'Marka alanı zorunludur.'}
        self.fields['category'].error_messages = {'required': 'Kategori alanı zorunludur.'}
        self.fields['category'].initial = None
        self.fields['category'].choices = [('', 'Kategori seçin')] + list(self.fields['category'].choices)[1:]

    class Meta:
        model = GlutenFreeFood
        fields = ['name', 'category', 'brand', 'description', 'is_approved']
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
        self.fields['name'].required = True
        self.fields['city'].required = True
        # İlçe artık zorunlu değil, şehir seçildikten sonra dolacak
        self.fields['district'].required = False
        self.fields['name'].error_messages = {'required': 'Mekan adı zorunludur.'}
        self.fields['city'].error_messages = {'required': 'Şehir alanı zorunludur.'}

    class Meta:
        model = GlutenFreeVenue
        # Formda gösterilecek alanlar
        fields = ['name', 'city', 'district', 'gluten_free_products', 'contact', 'address', 'website', 'description', 'is_approved']
        # Alanların etiketleri
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
        # Alanların HTML widget'ları ve özellikleri
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # ID'ler JavaScript kodunda kullanılacak
            'city': forms.Select(attrs={'class': 'form-select', 'id': 'id_city'}, choices=[('', 'İl seçiniz')] + list(TURKISH_CITIES)),
            'district': forms.Select(attrs={'class': 'form-select', 'id': 'id_district'}, choices=[('', 'İlçe seçiniz')]),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'gluten_free_products': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class GlutenFreeHotelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['city'].required = True
        self.fields['district'].required = True
        self.fields['name'].error_messages = {'required': 'Otel adı zorunludur.'}
        self.fields['city'].error_messages = {'required': 'Şehir alanı zorunludur.'}
        self.fields['district'].error_messages = {'required': 'İlçe alanı zorunludur.'}
        # city için empty_label ve initial kaldırıldı (CharField olduğu için)

    def clean(self):
        cleaned_data = super().clean()
        city = cleaned_data.get('city')
        custom_city = self.data.get('custom_city_name') if self.data else None
        if city == 'Diğer' and custom_city:
            cleaned_data['city'] = custom_city
        return cleaned_data

    class Meta:
        model = GlutenFreeHotel
        fields = ['name', 'city', 'district', 'contact', 'address', 'website', 'description', 'is_approved']
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
            'city': forms.Select(attrs={'class': 'form-select', 'id': 'id_city'}),
            'district': forms.Select(attrs={'class': 'form-select', 'id': 'id_district'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }

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
            'is_approved': 'Onaylı mı?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-select', 'id': 'id_brand'}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class GlutenFreeRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['name'].error_messages = {'required': 'Tarif adı zorunludur.'}

    class Meta:
        model = GlutenFreeRecipe
        exclude = ['approved_at', 'added_by']
        labels = {
            'name': 'Tarif Adı',
            'description': 'Açıklama',
            'created_at': 'Oluşturulma Tarihi',
            'is_approved': 'Onaylı mı?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
