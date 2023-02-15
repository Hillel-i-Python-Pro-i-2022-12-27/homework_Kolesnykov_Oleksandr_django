from faker import Faker


class Human:
    def __init__(self):
        self.name = Faker().first_name()


def create_one_human():
    return Human()


def create_generator_of_humans(amount: int = 10):
    for _ in range(amount):
        yield create_one_human()
