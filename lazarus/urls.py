from django.urls import path
from lazarus import views


urlpatterns = [
    path('',views.Homeview  , name = "homeview"),
    path('login/',views.login,name='login'),
    path('register/',views.registration,name= 'Register')
]
