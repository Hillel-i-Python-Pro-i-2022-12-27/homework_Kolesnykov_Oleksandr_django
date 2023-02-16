from django.urls import path
from apps.contacts import views


app_name = "contacts"

urlpatterns = [
    path("contacts_list", views.list_of_contacts, name="contacts_list"),
    path("contact_details/<int:pk>", views.ContactDetailView.as_view(), name="contact_detail"),
    path("contact_create", views.ContactCreateView.as_view(), name="contact_create"),
    path("contact_update/<int:pk>", views.ContactUpdateView.as_view(), name="contact_update"),
    path("contact_delete/<int:pk>", views.ContactDeleteView.as_view(), name="contact_delete"),
]
