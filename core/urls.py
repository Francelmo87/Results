from django.urls import path
from django.contrib.auth import views as auth_views
from core import views as v
from core.views import GeneratePdf

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('list/', v.result_list, name='list'),
    path('pdf/', GeneratePdf.as_view(), name='pdf'),

]
