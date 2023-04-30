from django.urls import path
from .views import CreateUserView, LoginView, UserListView

urlpatterns = [
    path('', CreateUserView.as_view()),
    path('create-user/', CreateUserView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', UserListView.as_view()),
]
