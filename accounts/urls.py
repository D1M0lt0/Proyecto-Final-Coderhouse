from django.urls import path
from .views import signup, user_login, view_profile, edit_profile, delete_profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]

