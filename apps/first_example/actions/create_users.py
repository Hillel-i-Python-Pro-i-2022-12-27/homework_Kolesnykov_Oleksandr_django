from random import choice, randint
from string import ascii_letters

from faker import Faker


def create_email_for_user(user_name):

    mailboxes = ["@ukr.net", "@hillel.ua", "@gmail.com", "@git.com", "@hotmail.com"]
    adjectives = ["angry", "beautiful", "brave", "clever", "crazy", "dangerous", "evil", "happy", "funny"]

    return f"{choice(adjectives)}_{user_name}{choice(mailboxes)}"


def create_password():
    password = ""
    for letter in range(randint(6, 8)):
        password += choice(ascii_letters)
    return f"{password.capitalize()}{randint(10,999)}"


class Human:
    def __init__(self, name, email, password):
        self.name = name
        self.user_email = email
        self.password = password


def create_one_human():

    name = Faker().first_name()
    email = create_email_for_user(name)
    password = create_password()

    return Human(name, email, password)


def create_generator_of_humans(amount: int = 10):
    for _ in range(amount):
        yield create_one_human()
