

from django.urls import path
from . import views
from .views import sign_up_by_django, sign_up_by_html, HomeView, game_list, CartView, StoreView
from .views import home, cart, register

urlpatterns = [
    path('', HomeView.as_view(), name='main_page'),
    path('games/', game_list, name='games_list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('register/', sign_up_by_django, name='sign_up'),
    path('django_sign_up/', sign_up_by_html, name='django_sign_up'),
   # path('games/', game_list, name='games_list'),
]

# urlpatterns = [
#     path('', home, name='home'),
#     path('products/', product_list, name='product_list'),
#     path('cart/', cart, name='cart'),
#     path('register/', register, name='register'),
# ]