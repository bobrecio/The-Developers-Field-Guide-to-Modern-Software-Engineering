class Shape: ... 

class Circle(Shape): ... 

class Square(Shape): ... 

 

def shape_factory(shape_type): 

    if shape_type == "circle": return Circle() 

    if shape_type == "square": return Square() 

    raise ValueError("Unknown shape") 

 

shape = shape_factory("circle") 