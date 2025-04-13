from django.urls import path
from lazarus import views


urlpatterns = [
    path('',views.Homeview  , name = "homeview"),
    path('login/',views.loginpage,name='login'),
    path('register/',views.registration,name= 'Register'),
    path('posting/<str:pk>/',views.JobView,name='Jobview'),
    path('logout/',views.logoutfunction,name='logout'),
    path('updateUser',views.UpdateUser,name='UpdateUser'),
]
