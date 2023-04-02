import numpy as np
from PIL import Image
from random import randint
from shapes import Square, Rectangle
from canvas import canvas
filepath = f'files/test{randint(0,1000)}.png'

#creating canvas class


# class canvas:
#     '''This is the object that nests all drawing'''

#     def __init__(self,canvasw,canvash):     #passing number of pixels as dimmentions to the canvas
        
#         data = np.zeros((canvasw,canvash,3),dtype=np.uint8)         #generating an aray the 3 is for RGB
#         data[:] = [randint(0,250),randint(0,250),randint(0,250)]    # coloring all the canvas
               
#         self.data = data


     

# class Square:
#     '''This is the sqaure shape an just needs to enter the side'''

#     def __init__(self, xstart, ystart ,side):
#         self.xstart = xstart            # x coordinator that shape starts
#         self.ystart = ystart            # y coordinator that shape starts
#         self.width = side
#         self.height = side

#     def draw(self, canvas):             # this function draws the shape in the canvas

#         canvas.data[self.xstart:(self.xstart+self.width),self.ystart:(self.ystart+self.height)] = sqobjectcolor
    
#         img = Image.fromarray(canvas.data, 'RGB')   #creating the image
#         img.save(filepath)              #saving the image
            
    

# class Rectangle:


#     def __init__(self, xstart, ystart , recwidth, recheight):
#         self.xstart = xstart            # x coordinator that shape starts
#         self.ystart = ystart            # y coordinator that shape starts
#         self.width = recwidth
#         self.height = recheight

    
#     def draw(self, canvas):             # this function draws the shape in the canvas

#         canvas.data[self.xstart:(self.xstart+self.width),self.ystart:(self.ystart+self.height)] = recobjectcolor
        
#         img = Image.fromarray(canvas.data, 'RGB')       # creating the image
#         img.save(filepath)    # saving the image

    

# passing data needed to app
recobjectcolor = [randint(0,250), randint(0,250),randint(0,250)]
sqobjectcolor = [randint(0,250), randint(0,250),randint(0,250)]
canvas1 = canvas(400,500)
rectangle = Rectangle(100,200, 100, 200)
square = Square (randint(0,400), randint(0,500), 75)

#passing data to the fuction to draw the shapes
rectangle.draw(canvas1)
square.draw(canvas1)


