from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from users.models import GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine
from .models import ContactMessage
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

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
    foods = GlutenFreeFood.objects.filter(is_approved=True)
    return render(request, 'pages/gf_food.html', {'foods': foods})

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
    return render(request, 'pages/admin_contact_list.html', {'messages': messages})
