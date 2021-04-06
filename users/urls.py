"""Users URLS"""
#Django
from django.urls import path, include
from django.views.generic import TemplateView
#Views
from users import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('me/profile/', views.UpdateProfileView.as_view(), name='update'),
    path(
        route = '<str:username>/',
        view = views.UserDetailView.as_view(),
        name = 'detail'
    ),
]