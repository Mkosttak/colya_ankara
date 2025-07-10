from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

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
    name = models.CharField(max_length=100, unique=True, verbose_name="Marka Adı")
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Kategori Adı")
    def __str__(self):
        return self.name

class GlutenFreeFood(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Marka")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategori")
    is_approved = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    approved_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Ekleyen Kullanıcı')
    def __str__(self):
        return self.name

class GlutenFreeVenue(models.Model):
    name = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    gluten_free_products = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Ekleyen Kullanıcı')
    def __str__(self):
        return self.name

class GlutenFreeHotel(models.Model):
    name = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Ekleyen Kullanıcı')
    def __str__(self):
        return self.name

class GlutenFreeMedicine(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Marka")
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Ekleyen Kullanıcı')
    def __str__(self):
        return self.name

class GlutenFreeRecipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, related_name='added_%(class)s_items', verbose_name='Ekleyen Kullanıcı')
    def __str__(self):
        return self.name
