class r_calculator():
    def __init__(self):
        self.income_dict =  {}
        self.expenses_dict = {}
        self.investment_dict = {}
     
    

    def income(self):
        action = input("What is the source of income")#Uber
        income_1 = input ("What's your monthly income")#6800
        self.income_dict[action]=float(income_1)
        return self.income_dict
    


    def add_cash(self): 
        action = input("What is the source of extra income?")#rental income
        add_cash_1 =input("How much?")#2000
        self.income_dict[action]= float(add_cash_1)
        return self.income_dict

    def expenses(self):
        action = input("What are your expenses?")#utilities, hoa, repairs, property management, mortgage
        expenses_1= input("How much?")#1750
        self.expenses_dict[action]= -float(expenses_1)
        
    

    def investment(self):
        action = input("What type investment?")#down payment, closing cost, repair budget
        investment_1= input("How much?")#50000cd
        self.investment_dict[action]=float(investment_1)
        

    def roi(self):
        total_roi = 0
        for value in self.income_dict.values():
            total_roi = total_roi + value
        for value in self.expenses_dict.values():
            total_roi = total_roi - 12*value 

        investment = 0
        for value in self.investment_dict.values():
            investment = investment + value 

        total_roi = 100*total_roi /investment
        print(f"The ROI is {total_roi}%.")
        
Troy = r_calculator()
def run():
    print(f'Welcome to my rental calculator.')

    
    Troy.income()
    Troy.add_cash()
    Troy.expenses()
    Troy.investment()
    Troy.roi()

                
print(run())#None becasue there is nothing to return