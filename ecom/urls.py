from django.urls import path
from . import views


urlpatterns=[
    path('login', views.loginuser, name = 'login'),
    path('', views.home, name = 'home'),
    path('logout', views.logoutuser, name = 'logout'),
    path('create-user', views.createuser, name = 'create-user'),
    path('go-to-item/<str:pk>/', views.go_to_item, name = 'go-to-item'),
    path('add-to-cart/<str:item_name>/', views.add_to_cart, name = 'add-to-cart'),
    path('view-cart', views.view_cart, name = 'view_cart'),
    path('user_page/<str:pk>/', views.user_page, name = 'user_page'),
    path('minus_item/<str:item_id>/', views.minus_item, name = 'minus_item'),
    path('empty_cart', views.empty_cart, name = 'empty_cart'),
    # path('remove/<int:cart_item_id/', views.remove_from_cart, name = 'remove_from_cart'),
    path('about', views.about, name = 'about'),
    path('help', views.help, name = 'help'),
    path('more', views.more, name = 'more'),
    path('contacts', views.contacts, name = 'contacts'),
]