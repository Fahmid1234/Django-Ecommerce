from django.urls import path
from shop import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('product-details/<int:pk>', views.productdetails, name='productdetail'),
    path('register/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
    path('plus_cart/', views.plus_cart),
    path('minus_cart/', views.minus_cart),
    path('remove_cart/', views.remove_cart),
    path('empty_cart/', views.emptycart, name='empty_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('billing_info/', views.billing_info, name='billing_info'),
    path('process_order/', views.process_order, name='process_order'),
    path('about/', views.about, name='about'),
    path('shop/', views.home, name='shop'),
    path('fan/', views.fanPage, name='fan'),
    path('smartwatch/', views.smartwatchPage, name='smartwatch'),
    path('powerbank/', views.powerbankPage, name='powerbank'),
]
