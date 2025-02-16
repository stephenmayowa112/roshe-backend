from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views  # Import the JWT views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Existing user URLs
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT obtain token
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh token
]
