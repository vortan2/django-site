from users.views import login, registration, profile, logout
from django.urls import path

from products.views import products
app_name = 'users'
urlpatterns = [
    path('login/' ,login , name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout')

]
