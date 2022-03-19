from django.urls import path
from django.contrib.auth import views as auth_views
from core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('list/', v.ResultList.as_view(), name='result_list'),

]
