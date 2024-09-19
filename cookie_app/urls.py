from django.urls import path
from .views import set_cookie, get_cookie, delete_cookie

urlpatterns = [
    path('set_cookie/', set_cookie, name='set_cookie'),
    path('get_cookie/', get_cookie, name='get_cookie'),
    path('delete_cookie/', delete_cookie, name='delete_cookie')
    ]