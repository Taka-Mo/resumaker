from django.urls import path
from .views import Register, Login, InputView, InputView2, InputView3, InputView4
from . import views
from django.contrib.auth.views import LoginView



urlpatterns = (
    path('', views.home, name='home'),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
#    path('login', LoginView.as_view(template_name='resume/login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('step1', InputView.as_view(), name='step1'),
    path('step2', InputView2.as_view(), name='step2'),
    path('step3', InputView3.as_view(), name='step3'),
    path('step4', InputView4.as_view(), name='step4'),
    path('profile', views.user_profile, name='profile'),
    path('create', views.createresume, name='create'),
    path('draft', views.draft, name='draft')
)
