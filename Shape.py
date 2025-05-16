import random

class Color:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self, new_color):
        self.color = new_color

class Shape:
    def __init__(self):
        #This is called Composition, where class Shape stores an instance of another class Color
        self.color_obj = Color("White")

    def area(self):
        return "Shape area"
    
    def get_color(self):
        #call method get_color() from class Color 
        return self.color_obj.get_color()

    def get_random_color(self):
        #List of colors 
        list1 = ["Red", "Green", "Blue"]
        #create list of objects of class Color
        list_obj = [Color(i) for i in list1]
        #select a random object from the list and call get_color() method from the Color class
        return random.choice(list_obj).get_color()

class Rectangle(Shape):
    def __init__(self, width, height):
        #The initializer of the superclass9(person) is not called automatically 
        # when we create a new instance (unless we didn’t have __init__ in the subclass). 
        # In this case, we manually call the super().__init__ function.
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        if not (isinstance(self.width, int) and isinstance(self.height, int)):
            raise TypeError ("Please enter int")
        else:
            return self.width * self.height
    #__repr__ method is used to define a string representation of an object.
    def __repr__(self):
        return f"This is a rectangle of area {self.area()}"
    #__ge__ magic method used to compare two objects (greater than or eqaul)
    def __ge__(self, other):
        return self.area() >= other.area()
if __name__ == "__main__":

    r1 = Rectangle(2,4)
    print(r1.area())
    print(r1)
    r2 = Rectangle(3,4)
    print(r1 >= r2)
    print(r1.get_color())
    print(r1.get_random_color())






















'''import random
class Color:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self, new_color):
        self.color = new_color

class Shape:
    def __init__(self):
        self.color_obj = Color("White")
    def area(self):
        return "Shape area"
    def get_color(self):
        return self.color_obj.get_color()
    def get_random_color(self):
        list1 = ["Red", "blue", "Green"]
        objs_color = []
        for c in list1:
            objs_color.append(Color(c))
        return random.choice(objs_color).get_color()
    def __repr__(self):
        return "This is Rect"
        
s = Shape()
print(s.get_color())

class Rect(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        if not (isinstance(self.width, int) and isinstance(self.height, int)):
            raise TypeError ("please numbers")
    
    def area(self):
        return self.width * self.height
    
    def __ge__(self, other):
        return self.area() >= other.area()
    #def __ge

r = Rect(5,7)
print(r.area())
print(r.get_color())
print(r.get_random_color())
r2 = Rect(7,8)
print(r >=r2)

'''