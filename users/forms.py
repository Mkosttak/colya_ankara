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
    # Manuel giriş için kullandığımız metin alanları
    city_other = forms.CharField(
        label="Şehir (Manuel Giriş)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Listede olmayan şehri buraya yazınız'})
    )
    district_other = forms.CharField(
        label="İlçe (Manuel Giriş)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İlçeyi buraya yazınız'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Eğer bir instance varsa (düzenleme durumu) ve şehir "Diğer" listede yoksa
        if self.instance and self.instance.pk:
            # Şehir değeri TURKISH_CITIES listesinde yoksa, "Diğer" seç ve manuel alanları doldur
            if self.instance.city and self.instance.city not in [city[0] for city in TURKISH_CITIES]:
                self.fields['city'].initial = 'Diğer'
                self.fields['city_other'].initial = self.instance.city
                self.fields['district_other'].initial = self.instance.district
        # İlçe alanını zorunlu yap
        self.fields['district'].required = True

    class Meta:
        model = GlutenFreeVenue
        # Formda gösterilecek alanların sırasını düzenliyoruz
        fields = [
            'name', 'city', 'city_other', 'district', 'district_other', 
            'gluten_free_products', 'contact', 'address', 'website', 
            'description', 'is_approved'
        ]
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
        """
        Bu metod artık sadece "Diğer" seçildiğinde manuel alanın boş olup olmadığını kontrol ediyor.
        Veri değiştirme işlemi yapmıyor.
        """
        cleaned_data = super().clean()
        city_choice = cleaned_data.get('city')
        city_other_value = cleaned_data.get('city_other', '').strip()
        district_choice = cleaned_data.get('district')
        district_other_value = cleaned_data.get('district_other', '').strip()

        # Şehir kontrolü
        if city_choice == 'Diğer' and not city_other_value:
            # Eğer "Diğer" seçilmiş ama manuel şehir alanı boş bırakılmışsa hata ver.
            self.add_error('city_other', '"Diğer" seçeneğini kullandığınızda şehir adını manuel olarak girmek zorunludur.')
        
        # İlçe kontrolü
        if city_choice == 'Diğer':
            # "Diğer" seçildiğinde manuel ilçe alanı zorunlu
            if not district_other_value:
                self.add_error('district_other', 'İlçe bilgisi zorunludur.')
        else:
            # Normal şehir seçildiğinde dropdown ilçe alanı zorunlu
            if not district_choice:
                self.add_error('district', 'İlçe bilgisi zorunludur.')
        
        return cleaned_data

    def save(self, commit=True):
        """
        Bu metod, form verisini veritabanına kaydeder.
        Hatanın çözüldüğü yer burasıdır.
        """
        # 1. Normal kaydetme işlemini başlat ama veritabanına gönderme (commit=False)
        # Bu bize doldurulmuş bir model nesnesi (instance) verir.
        instance = super().save(commit=False)

        # 2. Eğer kullanıcının dropdown'dan seçtiği değer "Diğer" ise:
        if self.cleaned_data.get('city') == 'Diğer':
            # Model nesnesinin 'city' alanını, manuel girilen 'city_other' değeriyle değiştir.
            instance.city = self.cleaned_data.get('city_other', '').strip()
            # Model nesnesinin 'district' alanını, manuel girilen 'district_other' değeriyle değiştir.
            instance.district = self.cleaned_data.get('district_other', '').strip()
        
        # 3. Eğer `commit` parametresi True ise (ki genelde öyledir),
        # tüm değişiklikler yapıldıktan sonra nesneyi veritabanına kaydet.
        if commit:
            instance.save()
            # Many-to-many alanlarınız olsaydı, bu satıra da ihtiyaç olurdu:
            # self.save_m2m()

        return instance

class GlutenFreeHotelForm(forms.ModelForm):
    # Manuel giriş için aynı metin alanlarını ekliyoruz
    city_other = forms.CharField(
        label="Şehir (Manuel Giriş)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Listede olmayan şehri buraya yazınız'})
    )
    district_other = forms.CharField(
        label="İlçe (Manuel Giriş)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İlçeyi buraya yazınız'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Eğer bir instance varsa (düzenleme durumu) ve şehir "Diğer" listede yoksa
        if self.instance and self.instance.pk:
            # Şehir değeri TURKISH_CITIES listesinde yoksa, "Diğer" seç ve manuel alanları doldur
            if self.instance.city and self.instance.city not in [city[0] for city in TURKISH_CITIES]:
                self.fields['city'].initial = 'Diğer'
                self.fields['city_other'].initial = self.instance.city
                self.fields['district_other'].initial = self.instance.district
        # İlçe alanını zorunlu yap
        self.fields['district'].required = True

    class Meta:
        model = GlutenFreeHotel
        # Alan listesini otel modeline göre düzenliyoruz
        fields = [
            'name', 'city', 'city_other', 'district', 'district_other', 
            'contact', 'address', 'website', 'description', 'is_approved'
        ]
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

    # Doğrulama metodu (Mekan formuyla birebir aynı)
    def clean(self):
        cleaned_data = super().clean()
        city_choice = cleaned_data.get('city')
        city_other_value = cleaned_data.get('city_other', '').strip()
        district_choice = cleaned_data.get('district')
        district_other_value = cleaned_data.get('district_other', '').strip()

        # Şehir kontrolü
        if city_choice == 'Diğer' and not city_other_value:
            self.add_error('city_other', '"Diğer" seçeneğini kullandığınızda şehir adını manuel olarak girmek zorunludur.')
        
        # İlçe kontrolü
        if city_choice == 'Diğer':
            # "Diğer" seçildiğinde manuel ilçe alanı zorunlu
            if not district_other_value:
                self.add_error('district_other', 'İlçe bilgisi zorunludur.')
        else:
            # Normal şehir seçildiğinde dropdown ilçe alanı zorunlu
            if not district_choice:
                self.add_error('district', 'İlçe bilgisi zorunludur.')
        
        return cleaned_data

    # Kaydetme metodu (Mekan formuyla birebir aynı)
    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get('city') == 'Diğer':
            instance.city = self.cleaned_data.get('city_other', '').strip()
            instance.district = self.cleaned_data.get('district_other', '').strip()
        
        if commit:
            instance.save()
            # self.save_m2m() # Eğer many-to-many alanınız olsaydı bu gerekli olurdu

        return instance

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
