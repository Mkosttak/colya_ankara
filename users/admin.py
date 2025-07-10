from django.contrib import admin
from .models import GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine, GlutenFreeRecipe, Brand, Category, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'is_active', 'is_superuser', 'last_login')
    list_filter = ('role', 'is_active', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('-is_active', 'username')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Kişisel Bilgiler', {'fields': ('first_name', 'last_name', 'role')}),
        ('Yetkiler', {'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Önemli Tarihler', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'role', 'password1', 'password2', 'is_active', 'is_superuser'),
        }),
    )
    list_per_page = 25
    verbose_name = 'Kullanıcı'
    verbose_name_plural = 'Kullanıcılar'

# Diğer admin kayıtları (önceki kodlarınız)
@admin.register(GlutenFreeFood)
class GlutenFreeFoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'is_approved', 'approved_at', 'added_by')
    search_fields = ('name', 'brand__name', 'category__name')
    list_filter = ('is_approved',)
    verbose_name = 'Glutensiz Gıda'
    verbose_name_plural = 'Glutensiz Gıdalar'

@admin.register(GlutenFreeVenue)
class GlutenFreeVenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_approved', 'approved_at', 'added_by')
    search_fields = ('name', 'address', 'contact')
    list_filter = ('is_approved',)
    verbose_name = 'Glutensiz Mekan'
    verbose_name_plural = 'Glutensiz Mekanlar'

@admin.register(GlutenFreeHotel)
class GlutenFreeHotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_approved', 'approved_at', 'added_by')
    search_fields = ('name', 'address', 'contact')
    list_filter = ('is_approved',)
    verbose_name = 'Glutensiz Otel'
    verbose_name_plural = 'Glutensiz Oteller'

@admin.register(GlutenFreeMedicine)
class GlutenFreeMedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'is_approved', 'approved_at', 'added_by')
    search_fields = ('name', 'brand__name')
    list_filter = ('is_approved',)
    verbose_name = 'Glutensiz İlaç'
    verbose_name_plural = 'Glutensiz İlaçlar'

@admin.register(GlutenFreeRecipe)
class GlutenFreeRecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_approved', 'approved_at', 'created_at', 'added_by')
    search_fields = ('name',)
    list_filter = ('is_approved',)
    verbose_name = 'Glutensiz Tarif'
    verbose_name_plural = 'Glutensiz Tarifler'

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name = 'Marka'
    verbose_name_plural = 'Markalar'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name = 'Kategori'
    verbose_name_plural = 'Kategoriler'
