
from fpdf import FPDF       # importing library to generate pdf
import webbrowser

class Bill:                 # defining Bill Object
    '''Bill Object contains data about the bill, such as
    total amount and period   
    '''

    def __init__ (self, period, total_amount):
        self.period = period
        self.total_amount = total_amount


class Flatmate:             # defining Flatmate Object
    '''
    Flatmate Object contains information about each flatmate.
    The flatmate attributes are their name and the days each 
    flatmate lives in the house.
    '''

    def __init__(self, name, days_in_home):     
        self.name = name
        self.days_in_home = days_in_home
        
    def pays(self, Bill, Flatmate):     # calculates how much each flatmate should pay
        
        to_pay = Bill.total_amount \
                    * (self.days_in_home / (self.days_in_home + Flatmate.days_in_home))
                    
        return to_pay


class PdfReport:            # defining PdfReport Object to generate pdf

    def __init__(self, Bill):
        self.Bill = Bill
        self.filename = Bill.period+ ' ' + f1.name + '-' + f2.name      # creating the filename based on the inputs
        
                
    def generate(self):
        pdf = FPDF(orientation='P', unit='pt' ,format='A4')     # initial setup
        pdf.add_page()

        pdf.set_font(family='Times', size=24 , style='B')       # initial setup
        pdf.cell(w=200,h=80, txt='Flatmates Bill' , border = 1 , align='C' , ln=1)      # ln=1 add a line after this line of code
        pdf.cell(w=100,h=60, txt='Period' , border=1)
        pdf.cell(w=200,h=60, txt='  '+ str(self.Bill.period) , border=1 , ln=1)

        #inserting the flatmates data
        pdf.set_font(family='Times', size=20)

        pdf.cell(w=100,h=80, txt=f1.name , border=0)

        pdf.cell(w=100,h=80, txt=str(f1.pays(self.Bill,f2)) , border=0 , ln=1)

        pdf.cell(w=100,h=80, txt=f2.name , border=0)

        pdf.cell(w=100,h=80, txt=str(f2.pays(self.Bill,f1)) , border=0 , ln=1)

        pdf.output(f"files/{f'{B1.period}.pdf'}")      # it's important to write the file name with f'{}'
        webbrowser.open(f"files/{f'{B1.period}.pdf'}")



#initating Static Objects       # to enter dynamic data uncomment the lines in the next following lines
f1name = 'Nima'
f2name = 'Mike'
f1days = 42
f2days = 28
f1 = Flatmate( f1name , f1days )
f2 = Flatmate( f2name , f2days )
totalbillamount = 70
B1 = Bill('March 2022', totalbillamount)

#initating Object for pdf report
pdf1 = PdfReport(B1)
print(pdf1.filename)
f1.pays(B1,f2)
pdf1.generate()


# #initating Dynamic Objects (user pass the data to the app)
# f1name = input('Enter the first Flatmate name : ')
# f2name = input('Enter the second Flatmate name : ')
# f1days = float(input('Enter the F1 Days'))
# f2days = float(input('Enter the F2 Days'))
# f1 = Flatmate( f1name , f1days )
# f2 = Flatmate( f2name , f2days )
# totalbillamount = float(input('Please enter total amount'))
# B1 = Bill('March 2021', totalbillamount)


















# to work on it later
#dependant variables (created for print function)

#print(f1.pay(B1,f2))       ''' TypeError: 'float' object is not callable '''

f1payy = f1.pays(B1,f2)
f2payy = f1.pays(B1,f2)

print('''
        {} stays {} and
        {} stays {} in house.'''.format(f1name,f1days,f2name,f2days))
        
print('''
        considering that total bill is {}
        {} share is {} and
        {} share is {} .format
        '''.format(totalbillamount,f1name,f1payy,f2name,f2payy))



