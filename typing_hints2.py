from typing import Sequence, Iterable, Any, List, Set, Dict, Tuple, Union, Final
from sys import getsizeof


people: List = ['Mario', 'Luigi']
coordinates: Tuple[int, str] = (1, '2')


def display_size(user_input: Any) -> None:
    print((f'{user_input} -> {getsizeof(user_input)} bytes'))


display_size([1, 2, 3])


CONSTANT: Final[str] = 'I am a constant'

print(CONSTANT * 2)
CONSTANT = 'Hello, world'  # notice type hint
print(CONSTANT)


def list_elements(elements: Iterable[str]) -> None:
    for i, element in enumerate(elements, start=1):
        print(i, element, sep=': ')


people: list[str] = ['Mario', 'Luigi', 'James']
list_elements(people)
list_elements('Hello')
numbers: list[int] = [1,2,3]
list_elements(numbers)


