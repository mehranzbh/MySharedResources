import turtle
from random import randint


#initiating Point class
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rec(self , Rectangle):
        if Rectangle.lowleft.x < self.x < Rectangle.upright.x  \
            and Rectangle.lowleft.y < self.y < Rectangle.upright.y:
            return True
        else:
            return False



#initiating Rectangle class
class Rectangle:

    def __init__(self , lowleft , upright):
        self.lowleft = lowleft        
        self.upright = upright

    def area(self):
        cal_area = (self.upright.x- self.lowleft.x) * (self.upright.y - self.lowleft.y)
        return cal_area

#initiating GuiRectangle class
class GuiRectangle(Rectangle):

    def draw(self , canvas):

        canvas=turtle.Turtle()

        canvas.penup()
        canvas.goto((self.lowleft.x , self.lowleft.y))

        l1=self.upright.x - self.lowleft.x
        l2=self.upright.y - self.lowleft.y

        canvas.pendown()
        canvas.forward(l1)
        canvas.left(90)
        canvas.forward(l2)
        canvas.left(90)
        canvas.forward(l1)
        canvas.left(90)
        canvas.forward(l2)

        turtle.done()

        

#creating a Rectangle
p1 = Point(randint(0,50),(randint(0,50)))
p2 = Point(randint(51,500),randint(51,700))
print('The rectangle coordinators are ', (p1.x,p1.y) , 'and ', (p2.x,p2.y))


#creating a user_point
upx = float(input('please enter the X coordinate of your desired point'))
upy = float(input('please enter the Y coordinate of your desired point'))
user_point = Point(upx,upy)


#creating the objects50
rectangle = GuiRectangle(p1,p2)
myturtle=turtle.Turtle()
rectangle.draw(canvas=myturtle)


#checking whether user_point is inside the rec
if user_point.falls_in_rec(rectangle):
    print('The point is inside the rectangle')
else:
    print('The point is outside the rectangle')


# printing out the rectangle area
print('The rectangle area is : ' ,rectangle.area() )