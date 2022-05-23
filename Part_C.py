class Shapes:
    def __init__(self, shape, area_size):
        self.shape = shape
        self.area_size = area_size

square = Shapes("Square", 150.0)
rectangle_1 = Shapes("Rectangle", 80)
rectangle_2 = Shapes("Rectangles", 660)
circle = Shapes("Circle", 68.2)
triangle = Shapes("Triangle", 20)

print("1 - " + square.shape + " with area size " + str(square.area_size))
print("2 - " + rectangle_1.shape + " with area size " + str(rectangle_1.area_size))
print("3 - " + rectangle_2.shape + " with area size " + str(rectangle_2.area_size))
print("4 - " + circle.shape + " with area size " + str(circle.area_size))
print("5 - " + triangle.shape + " with area size " + str(triangle.area_size))

