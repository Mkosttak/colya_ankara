from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Türkiye'deki 81 ilin listesi
TURKISH_CITIES = [
    ('Adana', 'Adana'), ('Adıyaman', 'Adıyaman'), ('Afyonkarahisar', 'Afyonkarahisar'), ('Ağrı', 'Ağrı'),
    ('Amasya', 'Amasya'), ('Ankara', 'Ankara'), ('Antalya', 'Antalya'), ('Artvin', 'Artvin'),
    ('Aydın', 'Aydın'), ('Balıkesir', 'Balıkesir'), ('Bilecik', 'Bilecik'), ('Bingöl', 'Bingöl'),
    ('Bitlis', 'Bitlis'), ('Bolu', 'Bolu'), ('Burdur', 'Burdur'), ('Bursa', 'Bursa'),
    ('Çanakkale', 'Çanakkale'), ('Çankırı', 'Çankırı'), ('Çorum', 'Çorum'), ('Denizli', 'Denizli'),
    ('Diyarbakır', 'Diyarbakır'), ('Edirne', 'Edirne'), ('Elazığ', 'Elazığ'), ('Erzincan', 'Erzincan'),
    ('Erzurum', 'Erzurum'), ('Eskişehir', 'Eskişehir'), ('Gaziantep', 'Gaziantep'), ('Giresun', 'Giresun'),
    ('Gümüşhane', 'Gümüşhane'), ('Hakkari', 'Hakkari'), ('Hatay', 'Hatay'), ('Isparta', 'Isparta'),
    ('Mersin', 'Mersin'), ('İstanbul', 'İstanbul'), ('İzmir', 'İzmir'), ('Kars', 'Kars'),
    ('Kastamonu', 'Kastamonu'), ('Kayseri', 'Kayseri'), ('Kırklareli', 'Kırklareli'), ('Kırşehir', 'Kırşehir'),
    ('Kocaeli', 'Kocaeli'), ('Konya', 'Konya'), ('Kütahya', 'Kütahya'), ('Malatya', 'Malatya'),
    ('Manisa', 'Manisa'), ('Kahramanmaraş', 'Kahramanmaraş'), ('Mardin', 'Mardin'), ('Muğla', 'Muğla'),
    ('Muş', 'Muş'), ('Nevşehir', 'Nevşehir'), ('Niğde', 'Niğde'), ('Ordu', 'Ordu'),
    ('Rize', 'Rize'), ('Sakarya', 'Sakarya'), ('Samsun', 'Samsun'), ('Siirt', 'Siirt'),
    ('Sinop', 'Sinop'), ('Sivas', 'Sivas'), ('Tekirdağ', 'Tekirdağ'), ('Tokat', 'Tokat'),
    ('Trabzon', 'Trabzon'), ('Tunceli', 'Tunceli'), ('Şanlıurfa', 'Şanlıurfa'), ('Uşak', 'Uşak'),
    ('Van', 'Van'), ('Yozgat', 'Yozgat'), ('Zonguldak', 'Zonguldak'), ('Aksaray', 'Aksaray'),
    ('Bayburt', 'Bayburt'), ('Karaman', 'Karaman'), ('Kırıkkale', 'Kırıkkale'), ('Batman', 'Batman'),
    ('Şırnak', 'Şırnak'), ('Bartın', 'Bartın'), ('Ardahan', 'Ardahan'), ('Iğdır', 'Iğdır'),
    ('Yalova', 'Yalova'), ('Karabük', 'Karabük'), ('Kilis', 'Kilis'), ('Osmaniye', 'Osmaniye'),
    ('Düzce', 'Düzce')
]

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Kullanıcı adı zorunludur')
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('role', User.Role.ADMIN)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        EDITOR = 'editor', 'Editör'
        ADMIN = 'admin', 'Yönetici'

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.EDITOR)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Brand Name")
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    def __str__(self):
        return self.name

class FoodBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class MedicineBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class GlutenFreeFood(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(FoodBrand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Brand")
    category = models.ManyToManyField(Category, blank=True, verbose_name="Category")
    is_approved = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    approved_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Added By')
    def __str__(self):
        return self.name

class GlutenFreeVenue(models.Model):
    name = models.CharField(max_length=100)
    # Şehir alanı, yukarıdaki listeden seçim yapılacak şekilde güncellendi
    city = models.CharField(max_length=30, choices=TURKISH_CITIES, default='Ankara', verbose_name="Şehir")
    # İlçe alanı güncellendi
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name="İlçe")
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    website = models.URLField(blank=True, null=True, verbose_name="Web Sitesi")
    gluten_free_products = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Added By')
    def __str__(self):
        return self.name

class GlutenFreeHotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=30, verbose_name="City")
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name="District")
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    website = models.URLField(blank=True, null=True, verbose_name="Website")
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Added By')
    def __str__(self):
        return self.name

class GlutenFreeMedicine(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(MedicineBrand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Brand")
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Added By')
    def __str__(self):
        return self.name

class GlutenFreeRecipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Added By')
    def __str__(self):
        return self.name
