from django.contrib import admin
from .models import User, FoodBrand, MedicineBrand, Category, GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine, GlutenFreeRecipe
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Kişisel Bilgiler', {'fields': ('first_name', 'last_name', 'role')}),
        ('Yetkiler', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Önemli Tarihler', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

@admin.register(FoodBrand)
class FoodBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(MedicineBrand)
class MedicineBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(GlutenFreeFood)
class GlutenFreeFoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_brand', 'get_category', 'is_approved', 'approved_at', 'added_by')
    list_filter = ('is_approved', 'brand', 'category')
    search_fields = ('name', 'brand__name', 'category__name')
    autocomplete_fields = ['brand', 'category']
    actions = ['make_approved']
    def get_brand(self, obj):
        return obj.brand.name if obj.brand else '-'
    get_brand.short_description = 'Marka'
    def get_category(self, obj):
        return obj.category.name if obj.category else '-'
    get_category.short_description = 'Kategori'
    def make_approved(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} kayıt onaylandı.")
    make_approved.short_description = "Seçili ürünleri onayla"

@admin.register(GlutenFreeVenue)
class GlutenFreeVenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'district', 'is_approved', 'approved_at', 'added_by')
    list_filter = ('city', 'district', 'is_approved')
    search_fields = ('name', 'city', 'district', 'address')
    actions = ['make_approved']
    def make_approved(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} mekan onaylandı.")
    make_approved.short_description = "Seçili mekanları onayla"

@admin.register(GlutenFreeHotel)
class GlutenFreeHotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'district', 'is_approved', 'approved_at', 'added_by')
    list_filter = ('city', 'district', 'is_approved')
    search_fields = ('name', 'city', 'district', 'address')
    actions = ['make_approved']
    def make_approved(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} otel onaylandı.")
    make_approved.short_description = "Seçili otelleri onayla"

@admin.register(GlutenFreeMedicine)
class GlutenFreeMedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'is_approved', 'approved_at', 'added_by')
    list_filter = ('brand', 'is_approved')
    search_fields = ('name', 'brand__name')
    actions = ['make_approved']
    def make_approved(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} ilaç onaylandı.")
    make_approved.short_description = "Seçili ilaçları onayla"

@admin.register(GlutenFreeRecipe)
class GlutenFreeRecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_approved', 'created_at', 'approved_at', 'added_by')
    list_filter = ('is_approved',)
    search_fields = ('name', 'description')
    actions = ['make_approved']
    def make_approved(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} tarif onaylandı.")
    make_approved.short_description = "Seçili tarifleri onayla"

# Türkçeleştirme için verbose_name ve verbose_name_plural alanları modelde zaten ayarlıysa admin panelinde otomatik Türkçe görünür. Ekstra bir şey gerekirse modelde güncelleme yapılabilir.
