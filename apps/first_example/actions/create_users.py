from faker import Faker
from string import ascii_letters
from random import choice, randint


def create_email_for_user(human=None):
    if human is None:
        human = create_one_human()

    mailboxes = ["@ukr.net", "@hillel.ua", "@gmail.com", "@git.com", "@hotmail.com"]
    adjectives = ["angry", "beautiful", "brave", "clever", "crazy", "dangerous", "evil", "happy", "funny"]

    return f"{choice(adjectives)}_{human.name}{choice(mailboxes)}"


def create_password():
    password = ""
    for letter in range(randint(6, 8)):
        password += choice(ascii_letters)
    return f"{password.capitalize()}{randint(10,999)}"


class Human:
    def __init__(self):
        self.name = Faker().first_name()
        self.user_email = create_email_for_user(self)
        self.password = create_password()


def create_one_human():
    return Human()


def create_generator_of_humans(amount: int = 10):
    for _ in range(amount):
        yield create_one_human()
