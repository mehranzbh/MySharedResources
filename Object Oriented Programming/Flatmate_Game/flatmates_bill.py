

class Bill:
    '''Bill Object contains data about the bill, such as
    total amount and period   
    '''

    def __init__ (self, period, total_amount):
        self.period = period
        self.total_amount = total_amount

class Flatmate:
    '''
    Flatmate Object contains information about each flatmate.
    The flatmate attributes are their name and the days each 
    flatmate lives in the house.
    '''

    def __init__(self, name, days_in_home):
        self.name = name
        self.days_in_home = days_in_home
    
    def pays(self, Bill):
        self.pays = Bill.total_amount \
                    * (self.days_in_home / 30)
        return self.pays


f1 = Flatmate('mamad',8)
f2 = Flatmate('akbar',22)
B1 = Bill('March 2021',300)       #float(input('Please enter total amount'))


            