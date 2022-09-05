from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from account.views import (
    MyObtainPairView,
    RegisterView,
    UserListApiView,
    UserDetailAPIView
)

urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/', UserListApiView.as_view(), name='list'),
    path('detail/<int:id>', UserDetailAPIView.as_view(), name='detail'),
]
