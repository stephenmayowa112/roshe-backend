from django.urls import path
from .views import MentorListView, MentorDetailView, MenteeListView, MenteeDetailView
from .views import SessionListView, SessionDetailView, ReviewListView, ReviewDetailView
from .views import UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mentors/', MentorListView.as_view(), name='mentor-list'),
    path('mentors/<int:pk>/', MentorDetailView.as_view(), name='mentor-detail'),
    path('mentees/', MenteeListView.as_view(), name='mentee-list'),
    path('mentees/<int:pk>/', MenteeDetailView.as_view(), name='mentee-detail'),
    path('sessions/', SessionListView.as_view(), name='session-list'),
    path('sessions/<int:pk>/', SessionDetailView.as_view(), name='session-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
