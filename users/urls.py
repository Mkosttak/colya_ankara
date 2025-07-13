from django.urls import path
from .views import (
    CustomLoginView, new_user, change_password,
    admin_food_list, admin_food_create, admin_food_update, admin_food_delete,
    admin_venue_list, admin_venue_create, admin_venue_update, admin_venue_delete,
    admin_hotel_list, admin_hotel_create, admin_hotel_update, admin_hotel_delete,
    admin_medicine_list, admin_medicine_create, admin_medicine_update, admin_medicine_delete,
    admin_recipe_list, admin_recipe_create, admin_recipe_update, admin_recipe_delete,
    add_brand, add_category, admin_users_list, admin_user_delete, add_medicine_brand
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('new-user/', new_user, name='new_user'),
    path('change-password/', change_password, name='change_password'),
    # Admin gluten-free foods
    path('admin/foods/', admin_food_list, name='admin_food_list'),
    path('admin/foods/create/', admin_food_create, name='admin_food_create'),
    path('admin/foods/<int:pk>/update/', admin_food_update, name='admin_food_update'),
    path('admin/foods/<int:pk>/delete/', admin_food_delete, name='admin_food_delete'),
    # Admin gluten-free venues
    path('admin/venues/', admin_venue_list, name='admin_venue_list'),
    path('admin/venues/create/', admin_venue_create, name='admin_venue_create'),
    path('admin/venues/<int:pk>/update/', admin_venue_update, name='admin_venue_update'),
    path('admin/venues/<int:pk>/delete/', admin_venue_delete, name='admin_venue_delete'),
    # Admin gluten-free hotels
    path('admin/hotels/', admin_hotel_list, name='admin_hotel_list'),
    path('admin/hotels/create/', admin_hotel_create, name='admin_hotel_create'),
    path('admin/hotels/<int:pk>/update/', admin_hotel_update, name='admin_hotel_update'),
    path('admin/hotels/<int:pk>/delete/', admin_hotel_delete, name='admin_hotel_delete'),
    # Admin gluten-free medicines
    path('admin/medicines/', admin_medicine_list, name='admin_medicine_list'),
    path('admin/medicines/create/', admin_medicine_create, name='admin_medicine_create'),
    path('admin/medicines/<int:pk>/update/', admin_medicine_update, name='admin_medicine_update'),
    path('admin/medicines/<int:pk>/delete/', admin_medicine_delete, name='admin_medicine_delete'),
    # Admin gluten-free recipes
    path('admin/recipes/', admin_recipe_list, name='admin_recipe_list'),
    path('admin/recipes/create/', admin_recipe_create, name='admin_recipe_create'),
    path('admin/recipes/<int:pk>/update/', admin_recipe_update, name='admin_recipe_update'),
    path('admin/recipes/delete/<int:pk>/', admin_recipe_delete, name='admin_recipe_delete'),
    path('ajax/add-brand/', add_brand, name='add_brand_ajax'),
    path('ajax/add-category/', add_category, name='add_category_ajax'),
]

urlpatterns += [
    path('ajax/add-brand/', add_brand, name='add_brand_ajax'),
    path('ajax/add-category/', add_category, name='add_category_ajax'),
    path('ajax/add-medicine-brand/', add_medicine_brand, name='add_medicine_brand_ajax'),
    path('admin/users/', admin_users_list, name='admin_users_list'),
    path('admin/users/<int:pk>/delete/', admin_user_delete, name='admin_user_delete'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
