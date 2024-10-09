# In your crop_monitoring_app/urls.py
from django.urls import path,include
from .views import home, crop_prediction, signup_view, dashboard,analyze,prices,logout_view
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin

urlpatterns = [
    path('', home, name='home'),
    path('crop-prediction/', crop_prediction, name='crop_prediction'),
    path('analyze', analyze, name='analyze'),
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('prices/', prices, name='prices'),
    path('admin/', admin.site.urls),

]

