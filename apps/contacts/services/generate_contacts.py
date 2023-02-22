from apps.contacts.models import Contact
from faker import Faker


def generate_contact(amount: int = 10, is_mark_as_autogenerated: bool = False):
    for _ in range(amount):
        yield Contact(
            user_name=Faker().name(), phone_number=Faker().phone_number(), is_auto_generated=is_mark_as_autogenerated
        )
