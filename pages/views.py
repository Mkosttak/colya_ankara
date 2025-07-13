from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from users.models import GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine, FoodBrand, Category
from .models import ContactMessage
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db import models
from django.http import JsonResponse

def home(request):
    return render(request, 'pages/home.html')

def hakkimizda(request):
    return render(request, 'pages/about.html')

def yonetim_kurulu(request):
    return render(request, 'pages/board.html')

def dernegin_amaci(request):
    return render(request, 'pages/purpose.html')

def tarihce(request):
    return render(request, 'pages/history.html')

def glutensiz_gida(request):
    foods = GlutenFreeFood.objects.filter(is_approved=True).select_related('brand').prefetch_related('category')
    brands = FoodBrand.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    
    q = request.GET.get('q')
    brand_id = request.GET.get('brand')
    category_id = request.GET.get('category')
    
    # Filtreleme
    if q:
        foods = foods.filter(
            models.Q(name__icontains=q) |
            models.Q(brand__name__icontains=q) |
            models.Q(category__name__icontains=q)
        ).distinct()
    if brand_id:
        foods = foods.filter(brand_id=brand_id)
    if category_id:
        foods = foods.filter(category__id=category_id)
    
    # Dinamik filtreleme seçenekleri
    if brand_id:
        filtered_categories = Category.objects.filter(
            glutenfreefood__brand_id=brand_id,
            glutenfreefood__is_approved=True
        ).distinct().order_by('name')
        categories = filtered_categories
    if category_id:
        filtered_brands = FoodBrand.objects.filter(
            glutenfreefood__category__id=category_id,
            glutenfreefood__is_approved=True
        ).distinct().order_by('name')
        brands = filtered_brands
    
    # Gruplama ve sıralama
    grouped_foods = None
    if brand_id and category_id:
        # Hem marka hem kategori seçiliyse, sadece ortak ürünleri düz liste olarak döndür
        selected_brand = brands.get(id=brand_id)
        selected_category = categories.get(id=category_id)
        foods_filtered = foods.order_by('name')
        grouped_foods = {
            'type': 'flat',
            'selected_brand': selected_brand,
            'selected_category': selected_category,
            'foods': foods_filtered
        }
    elif category_id:
        # Sadece seçili kategoriye ait ürünleri düz liste olarak döndür
        selected_category = categories.get(id=category_id)
        foods_in_category = foods.order_by('name')
        grouped_foods = {
            'type': 'flat',
            'selected_category': selected_category,
            'foods': foods_in_category
        }
    elif brand_id:
        # Sadece seçili markadaki ürünleri, kategoriye göre grupla
        selected_brand = brands.get(id=brand_id)
        foods_by_category = {}
        for food in foods.order_by('category__name', 'name'):
            for category in food.category.all():
                category_name = category.name
                if category_name not in foods_by_category:
                    foods_by_category[category_name] = []
                foods_by_category[category_name].append(food)
        grouped_foods = {
            'type': 'category',
            'selected_brand': selected_brand,
            'categories': foods_by_category
        }
    else:
        # Hiçbir filtre yoksa, kategoriye göre grupla
        foods_by_category = {}
        for food in foods.order_by('category__name', 'name'):
            for category in food.category.all():
                category_name = category.name
                if category_name not in foods_by_category:
                    foods_by_category[category_name] = []
                foods_by_category[category_name].append(food)
        grouped_foods = {
            'type': 'category',
            'categories': foods_by_category
        }
    
    return render(request, 'pages/gf_food.html', {
        'foods': foods, 
        'brands': brands, 
        'categories': categories,
        'grouped_foods': grouped_foods
    })

def glutensiz_mekanlar(request):
    venues = GlutenFreeVenue.objects.filter(is_approved=True)
    return render(request, 'pages/gf_places.html', {'venues': venues})

def glutensiz_oteller(request):
    hotels = GlutenFreeHotel.objects.filter(is_approved=True)
    return render(request, 'pages/gf_hotels.html', {'hotels': hotels})

def glutensiz_ilaclar(request):
    medicines = GlutenFreeMedicine.objects.filter(is_approved=True)
    return render(request, 'pages/gf_meds.html', {'medicines': medicines})

def glutensiz_tarifler(request):
    return render(request, 'pages/gf_recipes.html')

def basin_ve_yayinda_biz(request):
    return render(request, 'pages/press.html')

def uyelik(request):
    return render(request, 'pages/membership.html')

def iletisim(request):
    return render(request, 'pages/contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız başarıyla gönderildi. En kısa sürede sizinle iletişime geçilecektir.')
            return redirect('iletisim')
    else:
        form = ContactMessageForm()
    return render(request, 'pages/iletisim.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_contact_list(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'users/admin_contact_list.html', {'messages': messages})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_contact_delete(request, pk):
    from .models import ContactMessage
    msg = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        msg.delete()
        messages.success(request, 'Mesaj başarıyla silindi.')
        return redirect('admin_contact_list')
    return render(request, 'users/admin_contact_confirm_delete.html', {'msg': msg})

def get_filter_options(request):
    """AJAX endpoint for dynamic filter options"""
    brand_id = request.GET.get('brand')
    category_id = request.GET.get('category')
    
    if brand_id:
        # Marka seçilmişse, o markanın kategorilerini döndür
        categories = Category.objects.filter(
            glutenfreefood__brand_id=brand_id,
            glutenfreefood__is_approved=True
        ).distinct().order_by('name')
        return JsonResponse({
            'categories': list(categories.values('id', 'name'))
        })
    
    elif category_id:
        # Kategori seçilmişse, o kategorideki markaları döndür
        brands = FoodBrand.objects.filter(
            glutenfreefood__category__id=category_id,
            glutenfreefood__is_approved=True
        ).distinct().order_by('name')
        return JsonResponse({
            'brands': list(brands.values('id', 'name'))
        })
    
    return JsonResponse({'error': 'Invalid request'})
