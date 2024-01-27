from users.views import login, registration
from django.urls import path

from products.views import products
app_name = 'users'
urlpatterns = [
    path('login/' ,login , name='login'),
    path('registration/', registration, name='registration')
]
