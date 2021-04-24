from django.urls import path

from .views import CustomUserCreate

urlpatterns = [
   path('register/', CustomUserCreate.as_view(), name="create_user")
]
