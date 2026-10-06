# Base class representing a rectangle and its operations
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Creates a text-based picture of the rectangle
    def get_picture(self):
        picture = ""

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        for _ in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    # Calculates how many times another shape can fit inside the rectangle
    def get_amount_inside(self, shape):
        if shape.width == 0 or shape.height == 0:
            return 0

        width_count = self.width // shape.width
        height_count = self.height // shape.height

        return width_count * height_count


# Square class inheriting rectangle behavior while keeping equal dimensions
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width

    def set_height(self, height):
        self.width = height
        self.height = height
        self.side = height

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"


# Tests the Rectangle and Square classes
rect = Rectangle(10, 5)
print(rect.get_area())

rect.set_height(3)
print(rect.get_perimeter())

print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())

sq.set_side(4)
print(sq.get_diagonal())

print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))