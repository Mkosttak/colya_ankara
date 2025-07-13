from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash
from .forms import UserPasswordChangeForm
from .models import GlutenFreeFood, GlutenFreeVenue, GlutenFreeHotel, GlutenFreeMedicine, GlutenFreeRecipe, FoodBrand, Category
from .forms import GlutenFreeFoodForm, GlutenFreeVenueForm, GlutenFreeHotelForm, GlutenFreeMedicineForm, GlutenFreeRecipeForm
from django.http import JsonResponse, HttpRequest
from .models import Brand, Category
from django.db.models import Q, QuerySet
from .models import User
from typing import Any
from .models import MedicineBrand
# Yeni oluşturduğumuz turkey_data.py dosyasından fonksiyonu import ediyoruz
from .turkey_data import get_districts

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm
    def get_success_url(self):
        from django.urls import reverse
        return reverse('home')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def new_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yeni kullanıcı başarıyla oluşturuldu.')
            return redirect('admin_users_list')
    else:
        form = UserCreateForm()
    return render(request, 'users/new_users.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz başarıyla değiştirildi.')
            return redirect('change_password')
    else:
        form = UserPasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

# Superuser kontrolü
def superuser_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_superuser)(view_func))
    return decorated_view_func

# GlutenFreeFood CRUD
@superuser_required
def admin_food_list(request):
    foods = GlutenFreeFood.objects.all()  # type: ignore
    q = request.GET.get('q')
    brand_id = request.GET.get('brand')
    category_id = request.GET.get('category')
    is_approved = request.GET.get('is_approved')
    if q:
        foods = foods.filter(
            Q(name__icontains=q) |
            Q(brand__name__icontains=q) |
            Q(category__name__icontains=q)
        )
    if brand_id:
        foods = foods.filter(brand_id=brand_id)
    if category_id:
        foods = foods.filter(category_id=category_id)
    if is_approved in ['true', 'false']:
        foods = foods.filter(is_approved=(is_approved == 'true'))
    brands = Brand.objects.all()  # type: ignore
    categories = Category.objects.all()  # type: ignore
    return render(request, 'users/admin_food_list.html', {'foods': foods, 'brands': brands, 'categories': categories, 'request': request})

@superuser_required
def admin_food_create(request):
    if request.method == 'POST':
        form = GlutenFreeFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_food_list')
    else:
        form = GlutenFreeFoodForm()
    return render(request, 'users/admin_food_form.html', {'form': form})

@superuser_required
def admin_food_update(request, pk):
    food = get_object_or_404(GlutenFreeFood, pk=pk)
    if request.method == 'POST':
        form = GlutenFreeFoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('admin_food_list')
    else:
        form = GlutenFreeFoodForm(instance=food)
    return render(request, 'users/admin_food_form.html', {'form': form})

@superuser_required
def admin_food_delete(request, pk):
    food = get_object_or_404(GlutenFreeFood, pk=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('admin_food_list')
    return render(request, 'users/admin_food_confirm_delete.html', {'food': food})

# GlutenFreeVenue CRUD
@superuser_required
def admin_venue_list(request):
    venues = GlutenFreeVenue.objects.all()
    q = request.GET.get('q')
    city = request.GET.get('city')
    district = request.GET.get('district')
    is_approved = request.GET.get('is_approved')
    if q:
        venues = venues.filter(
            Q(name__icontains=q) |
            Q(contact__icontains=q) |
            Q(address__icontains=q)
        )
    if city:
        venues = venues.filter(city=city)
    if district:
        venues = venues.filter(district=district)
    if is_approved in ['true', 'false']:
        venues = venues.filter(is_approved=(is_approved == 'true'))
    return render(request, 'users/admin_venue_list.html', {'venues': venues, 'request': request})

@superuser_required
def admin_venue_create(request):
    if request.method == 'POST':
        form = GlutenFreeVenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_venue_list')
    else:
        form = GlutenFreeVenueForm()
    return render(request, 'users/admin_venue_form.html', {'form': form})

@superuser_required
def admin_venue_update(request, pk):
    venue = get_object_or_404(GlutenFreeVenue, pk=pk)
    if request.method == 'POST':
        form = GlutenFreeVenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('admin_venue_list')
    else:
        form = GlutenFreeVenueForm(instance=venue)
    return render(request, 'users/admin_venue_form.html', {'form': form})

@superuser_required
def admin_venue_delete(request, pk):
    venue = get_object_or_404(GlutenFreeVenue, pk=pk)
    if request.method == 'POST':
        venue.delete()
        return redirect('admin_venue_list')
    return render(request, 'users/admin_venue_confirm_delete.html', {'venue': venue})

# GlutenFreeHotel CRUD
@superuser_required
def admin_hotel_list(request):
    hotels = GlutenFreeHotel.objects.all()
    q = request.GET.get('q')
    city = request.GET.get('city')
    district = request.GET.get('district')
    is_approved = request.GET.get('is_approved')
    if q:
        hotels = hotels.filter(
            Q(name__icontains=q) |
            Q(contact__icontains=q) |
            Q(address__icontains=q)
        )
    if city:
        hotels = hotels.filter(city=city)
    if district:
        hotels = hotels.filter(district=district)
    if is_approved in ['true', 'false']:
        hotels = hotels.filter(is_approved=(is_approved == 'true'))
    return render(request, 'users/admin_hotel_list.html', {'hotels': hotels, 'request': request})

@superuser_required
def admin_hotel_create(request):
    if request.method == 'POST':
        form = GlutenFreeHotelForm(request.POST)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.added_by = request.user
            hotel.save()
            return redirect('admin_hotel_list')
    else:
        form = GlutenFreeHotelForm()
    return render(request, 'users/admin_hotel_form.html', {'form': form})

@superuser_required
def admin_hotel_update(request, pk):
    hotel = get_object_or_404(GlutenFreeHotel, pk=pk)
    if request.method == 'POST':
        form = GlutenFreeHotelForm(request.POST, instance=hotel)
        if form.is_valid():
            hotel = form.save(commit=False)
            if not hotel.added_by:
                hotel.added_by = request.user
            hotel.save()
            return redirect('admin_hotel_list')
    else:
        form = GlutenFreeHotelForm(instance=hotel)
    return render(request, 'users/admin_hotel_form.html', {'form': form})

@superuser_required
def admin_hotel_delete(request, pk):
    hotel = get_object_or_404(GlutenFreeHotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        return redirect('admin_hotel_list')
    return render(request, 'users/admin_hotel_confirm_delete.html', {'hotel': hotel})

# GlutenFreeMedicine CRUD
@superuser_required
def admin_medicine_list(request):
    medicines = GlutenFreeMedicine.objects.all()
    q = request.GET.get('q')
    brand_id = request.GET.get('brand')
    is_approved = request.GET.get('is_approved')
    if q:
        medicines = medicines.filter(
            Q(name__icontains=q) |
            Q(brand__name__icontains=q)
        )
    if brand_id:
        medicines = medicines.filter(brand_id=brand_id)
    if is_approved in ['true', 'false']:
        medicines = medicines.filter(is_approved=(is_approved == 'true'))
    brands = Brand.objects.all()
    return render(request, 'users/admin_medicine_list.html', {'medicines': medicines, 'brands': brands, 'request': request})

@superuser_required
def admin_medicine_create(request):
    if request.method == 'POST':
        form = GlutenFreeMedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_medicine_list')
    else:
        form = GlutenFreeMedicineForm()
    return render(request, 'users/admin_medicine_form.html', {'form': form})

@superuser_required
def admin_medicine_update(request, pk):
    medicine = get_object_or_404(GlutenFreeMedicine, pk=pk)
    if request.method == 'POST':
        form = GlutenFreeMedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('admin_medicine_list')
    else:
        form = GlutenFreeMedicineForm(instance=medicine)
    return render(request, 'users/admin_medicine_form.html', {'form': form})

@superuser_required
def admin_medicine_delete(request, pk):
    medicine = get_object_or_404(GlutenFreeMedicine, pk=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('admin_medicine_list')
    return render(request, 'users/admin_medicine_confirm_delete.html', {'medicine': medicine})

# GlutenFreeRecipe CRUD
@superuser_required
def admin_recipe_list(request):
    recipes = GlutenFreeRecipe.objects.all()
    q = request.GET.get('q')
    is_approved = request.GET.get('is_approved')
    if q:
        recipes = recipes.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q)
        )
    if is_approved in ['true', 'false']:
        recipes = recipes.filter(is_approved=(is_approved == 'true'))
    return render(request, 'users/admin_recipe_list.html', {'recipes': recipes, 'request': request})

@superuser_required
def admin_recipe_create(request):
    if request.method == 'POST':
        form = GlutenFreeRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_recipe_list')
    else:
        form = GlutenFreeRecipeForm()
    return render(request, 'users/admin_recipe_form.html', {'form': form})

@superuser_required
def admin_recipe_update(request, pk):
    recipe = get_object_or_404(GlutenFreeRecipe, pk=pk)
    if request.method == 'POST':
        form = GlutenFreeRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('admin_recipe_list')
    else:
        form = GlutenFreeRecipeForm(instance=recipe)
    return render(request, 'users/admin_recipe_form.html', {'form': form})

@superuser_required
def admin_recipe_delete(request, pk):
    item = get_object_or_404(GlutenFreeRecipe, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Tarif başarıyla silindi.')
        return redirect('admin_recipe_list')
    return render(request, 'users/admin_recipe_confirm_delete.html', {'item': item})

@superuser_required
def admin_users_list(request):
    users = User.objects.all().order_by('-is_active', 'username')
    return render(request, 'users/admin_users_list.html', {'users': users})

@superuser_required
def admin_user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user == request.user:
        messages.error(request, 'Kendi hesabınızı silemezsiniz!')
        return redirect('admin_users_list')
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Kullanıcı başarıyla silindi.')
        return redirect('admin_users_list')
    messages.error(request, 'Geçersiz istek.')
    return redirect('admin_users_list')

@superuser_required
def add_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            brand, created = FoodBrand.objects.get_or_create(name=name)
            return JsonResponse({'success': True, 'id': brand.id, 'name': brand.name})
        return JsonResponse({'success': False, 'error': 'İsim gerekli.'})
    return JsonResponse({'success': False, 'error': 'Sadece POST.'})

@superuser_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category, created = Category.objects.get_or_create(name=name)
            return JsonResponse({'success': True, 'id': category.id, 'name': category.name})
        return JsonResponse({'success': False, 'error': 'İsim gerekli.'})
    return JsonResponse({'success': False, 'error': 'Sadece POST.'})

@superuser_required
def add_medicine_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            brand, created = MedicineBrand.objects.get_or_create(name=name)
            return JsonResponse({'success': True, 'id': brand.id, 'name': brand.name})
        return JsonResponse({'success': False, 'error': 'İsim gerekli.'})
    return JsonResponse({'success': False, 'error': 'Sadece POST.'})

# Şehir seçildiğinde ilçeleri getirecek olan yeni view
@login_required
def get_districts_ajax(request):
    # 'city' parametresini GET isteğinden alıyoruz
    city = request.GET.get('city')
    # get_districts fonksiyonu ile o şehre ait ilçeleri alıyoruz
    districts = get_districts(city)
    # İlçeleri JSON formatında geri döndürüyoruz
    return JsonResponse({'districts': districts})
