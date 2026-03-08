from django.urls import path
from .views import ContactDetailCreateView, ContactDetailDeleteView

urlpatterns = [
    path('', ContactDetailCreateView.as_view(), name='home'),
    path('delete/<int:pk>/', ContactDetailDeleteView.as_view(), name='contact-delete'),
]

