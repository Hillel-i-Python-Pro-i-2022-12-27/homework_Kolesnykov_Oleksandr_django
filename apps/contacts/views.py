from django.shortcuts import render
from django.urls import reverse_lazy
from apps.contacts.models import Contact
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


def list_of_contacts(request):
    return render(
        request=request, template_name="contacts/contacts_list.html", context={"object_list": Contact.objects.all()}
    )


class ContactListView(ListView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "user_name",
        'department',
        "phone_number",
        "is_auto_generated",
    )

    success_url = reverse_lazy("contacts:contacts_list")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "user_name",
        'department',
        "phone_number",
        "is_auto_generated",
    )

    success_url = reverse_lazy("contacts:contacts_list")


class ContactDeleteView(DeleteView):
    model = Contact

    success_url = reverse_lazy("contacts:contacts_list")
