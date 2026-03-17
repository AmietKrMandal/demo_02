from django.urls import path
from .views import ContactDetailCreateView, ContactDetailDeleteView, ContactDetailUpdateView

urlpatterns = [
    path('', ContactDetailCreateView.as_view(), name='home'),
    path('update/<int:pk>/', ContactDetailUpdateView.as_view(), name='contact-update'),
    path('delete/<int:pk>/', ContactDetailDeleteView.as_view(), name='contact-delete'),
]

