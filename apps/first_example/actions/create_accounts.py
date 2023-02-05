from apps.first_example.actions.create_users import create_one_human, create_generator_of_humans
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


def create_account_for_one_user(user=None):
    if user is None:
        user = create_one_human()
    user_email = create_email_for_user(user)
    user_password = create_password()

    return f"""
name: {user.name}
email: {user_email}
password: {user_password}"""


def create_account_for_users_from_generator(amount=10, generator=None):
    if generator is None:
        generator = create_generator_of_humans(amount)

    for user in generator:
        yield create_account_for_one_user(user)
