from django.urls import path
from . import views
from .views import contact_view
from .views import admin_contact_list
from .views import admin_contact_delete

urlpatterns = [
    path('', views.home, name='home'),
    # Derneğimiz
    path('dernegimiz/hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('dernegimiz/yonetim-kurulu/', views.yonetim_kurulu, name='yonetim_kurulu'),
    path('dernegimiz/dernegin-amaci/', views.dernegin_amaci, name='dernegin_amaci'),
    path("dernegimiz/tarihce/", views.tarihce, name="tarihce"),
    # Glutensiz
    path('glutensiz/gida/', views.glutensiz_gida, name='glutensiz_gida'),
    path('glutensiz/mekanlar/', views.glutensiz_mekanlar, name='glutensiz_mekanlar'),
    path('glutensiz/oteller/', views.glutensiz_oteller, name='glutensiz_oteller'),
    path('glutensiz/ilaclar/', views.glutensiz_ilaclar, name='glutensiz_ilaclar'),
    path('glutensiz/tarifler/', views.glutensiz_tarifler, name='glutensiz_tarifler'),
    # Diğer
    path('basin-ve-yayinda-biz/', views.basin_ve_yayinda_biz, name='basin_ve_yayinda_biz'),
    path('uyelik/', views.uyelik, name='uyelik'),
]
urlpatterns += [
    path('iletisim/', contact_view, name='iletisim'),
    path('yonetim/contacts/', admin_contact_list, name='admin_contact_list'),
    path('yonetim/contacts/<int:pk>/delete/', admin_contact_delete, name='admin_contact_delete'),
] 