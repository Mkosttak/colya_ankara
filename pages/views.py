from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from users.models import GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine, Brand, Category
from .models import ContactMessage
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db import models

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
    brands = Brand.objects.all()
    categories = Category.objects.all()
    q = request.GET.get('q')
    brand_id = request.GET.get('brand')
    category_id = request.GET.get('category')
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
    return render(request, 'pages/gf_food.html', {'foods': foods, 'brands': brands, 'categories': categories})

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
