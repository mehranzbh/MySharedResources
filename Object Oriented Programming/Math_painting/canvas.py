class canvas:
    '''This is the object that nests all drawing'''

    def __init__(self,canvasw,canvash):     #passing number of pixels as dimmentions to the canvas
        
        data = np.zeros((canvasw,canvash,3),dtype=np.uint8)         #generating an aray the 3 is for RGB
        data[:] = [randint(0,250),randint(0,250),randint(0,250)]    # coloring all the canvas
               
        self.data = data

