from slist import views
from django.urls import path
urlpatterns = [
    path('', views.slist, name='list'),
    path('home', views.home, name='home'),
    path('delete/<product_id>', views.delete, name='delete'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
