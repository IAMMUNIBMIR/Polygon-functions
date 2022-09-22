class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height 

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self,width):
        self.width = width
        return self.width

    def get_height(self,height):
        self.height = height
        return self.height

    def get_area(self):
        Area = self.width * self.height
        return Area

    def get_perimeter(self):
        Perimeter = 2*(self.width + self.height)
        return Perimeter

    def get_diagonal(self):
        Diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return Diagonal
      
    def get_picture(self):

        if (self.width > 50):
            return "Too big for picture."

        if (self.height > 50):
            return "Too big for picture."

      
        line = "*" * self.width

        lines = [line for _ in range(self.height)]

        picture = '\n'.join(lines)

        return picture + "\n"

    def get_amount_inside(self, shape):
        
        W = self.width // shape.width
        H = self.height // shape.height

        return (W * H)

    def __str__(self):
      return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):

    def __init__(self,width):
        self.width = width
        self.height = width 

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
      return "Square(side=" + str(self.width) + ")"