from math import sqrt


class Rectangle:
    """Parent class representing any rectangle"""
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.height * self.width

    def get_perimeter(self) -> int:
        return 2 * (self.height + self.width)

    def get_diagonal(self) -> float:
        return sqrt(self.height ** 2 + self.width ** 2)

    def get_picture(self) -> str:
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'

        return '\n'.join('*' * (self.width) for _ in range(self.height)) + '\n'

    def get_amount_inside(self, shape: "Rectangle") -> int:
        # Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations)
        return (self.height // shape.height) * (self.width // shape.width)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    """Child class representing any rectangle"""
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def set_width(self, width: int) -> None:
        self.width = width
        self.height = width

    def set_height(self, height: int) -> None:
        self.width = height
        self.height = height

    def set_side(self, side: int) -> None:
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'
