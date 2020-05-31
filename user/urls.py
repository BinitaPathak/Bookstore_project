from django.urls import path

from user import views
from user.views import UserRegistration

urlpatterns = [
    path('registration/', UserRegistration.as_view(), name="registration"),
    path('buyerlogin/', views.buyerlogin, name="buyerlogin"),
    path('sellerlogin/', views.buyerlogin, name="sellerlogin"),
]
