uncaught_list: list[str] = [10, None, 4.8, [2, '5'], 'Khosro']

# in tuples order matters unless we use Union |
coordinates: tuple[int | str, ...] = ('magazine', 10, 'Khosro')

mixed_letters: set[str | int] = {'a', 1, 'b'}

my_dict: dict[str, int] = {'a': 10, None: 'text'}  # mypy throws error


def print_it(some_dict: dict[int, str]):
    for value in some_dict.values():
        print(value.title())


person: str | None = 'Luigi'


def greet(name: str | None = None):
    if name is None:
        print('No one is here...')
    else:
        print(f'Hello, {name}!')


greet(person)


def add_numbers(a: int, b: int) -> int:
    return a + b


print(add_numbers(10, 10))


def nasa() -> None:
    print('Nasa is a person!')


nasa()

import requests
from requests import Response


def get_user(url: str) -> int:
    request: Response = requests.get(url)
    status_code: int = request.status_code
    return status_code


def analyze_response(response: Response) -> None:
    print(response.content)


print(get_user('https://www.google.com'))
