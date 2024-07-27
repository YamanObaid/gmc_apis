from django.urls import path
from .views import SignupView, LoginView, UserGroupsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('groups/', UserGroupsView.as_view(), name='user-groups'),
]
