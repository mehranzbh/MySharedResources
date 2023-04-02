
        
class Square:
    '''This is the sqaure shape an just needs to enter the side'''

    def __init__(self, xstart, ystart ,side):
        self.xstart = xstart            # x coordinator that shape starts
        self.ystart = ystart            # y coordinator that shape starts
        self.width = side
        self.height = side

    def draw(self, canvas):             # this function draws the shape in the canvas

        canvas.data[self.xstart:(self.xstart+self.width),self.ystart:(self.ystart+self.height)] = sqobjectcolor
    
        img = Image.fromarray(canvas.data, 'RGB')   #creating the image
        img.save(filepath)              #saving the image
            



class Rectangle:


    def __init__(self, xstart, ystart , recwidth, recheight):
        self.xstart = xstart            # x coordinator that shape starts
        self.ystart = ystart            # y coordinator that shape starts
        self.width = recwidth
        self.height = recheight

    
    def draw(self, canvas):             # this function draws the shape in the canvas

        canvas.data[self.xstart:(self.xstart+self.width),self.ystart:(self.ystart+self.height)] = recobjectcolor
        
        img = Image.fromarray(canvas.data, 'RGB')       # creating the image
        img.save(filepath)    # saving the image
