from typing import NamedTuple, Iterator
from app.services import faker


class User(NamedTuple):
    name: str
    email: str


def generate_user() -> User:
    return User(
        name=faker.first_name(),
        email=faker.email()
    )


def generate_users(amount: int) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
