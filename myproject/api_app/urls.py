from django.urls import path
from .views import get_data, create_users,user_data

urlpatterns = [
    path('user/', get_data, name='get_data'),
    path('user/create', create_users, name='create_users'),
    path('user/user_data/<int:pk>', user_data, name='user_data'),
]