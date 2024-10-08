"""Exploring lists and associations with animals"""
from enum import Enum, auto

class Color(Enum):
    """Possible animal colors."""
    RED = auto()
    BLUE = auto()
    YELLOW = auto()
    GREEN = auto()
    ORANGE = auto()
    PURPLE = auto()
    PINK = auto()
    WHITE = auto()
    BLACK = auto()
    GRAY = auto()


class Animal:
    """Animal class, assoiciates animal name, color and number of legs."""

    def __init__(self, name: str, color=Color.BLACK, num_legs=4):
        """Class initializer.

        Args:
            name (str): Name of animal.
            color (Color, optional): Color of animal. Defaults to Color.BLACK.
            num_legs (int, optional): Number of legs on animal. Defaults to 4.
        """
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def __str__(self):
        """Print details of animal."""
        return f"animal = {self.name}, color = {self.color.name}, numLegs = {self.num_legs}"


# build a list of animals
Animals = [
    Animal("elephant", Color.GRAY, 4),
    Animal("flamingo", Color.PINK, 2),
    Animal("pig", Color.PINK, 4),
]

# print the list of animals
for animal in Animals:
    print(animal)
