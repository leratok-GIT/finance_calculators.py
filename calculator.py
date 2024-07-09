# a program that allows the user to access two different financial calculators:
#  an investment calculator and a home loan repayment calculator.

import math

def output():
    # first output that the user sees when the program runs
    print("\n Choose either 'investment' or 'bond' from the  menu below to proceed: \n" )
    print("investment - to calculator the amount of interest you'll earn on interest")
    print("bond - to calculator the amount you'll have to pay on a home loan")
    
    # The user inputs which calculation they want to do
    selection = int(input('''Choose between 
    1: Investment
    2: Bond
    0: Exit \n>>> '''))
    return selection

def simple(deposit,rate,years):
    # the simple interets formular
    S = deposit * (1+rate/100*years)
    print("=====================================")
    print(f"Your amount is: {S}")
    print("=====================================")
def compound(deposit,rate,years):
    # The compount interest formular
    C = deposit * math.pow((1+rate/100),years)
    print("=====================================") 
    print(f"Your amount is: {C}")
    print("=====================================")

# this function call back the option that the user makes.
def calculations(mySelection):
    if mySelection == 1:
        investment()
    elif mySelection == 2:
        bond()
        
# This function is for the investment  
def investment():
    deposit = float(input("The amount of money you what to deposit: "))
    years = int(input("The number of years you planning on investing for: "))
    rate = float(input("At what rate do you want to invest in: "))

    choose = input(''' Do you want simple and compound interest:
    Insert 'S' for Simple interst and 
    Insert 'C' for Compound interst \n>>> ''').lower() # this make the users input laower case.

    if choose == "s":
         # simple interest formula
        simple(deposit,rate,years)
    elif choose == "c":
        # simple interst formula
        compound(deposit,rate,years)
    else:
        print(" invalid choice")
        
# this function is for the Bond part
def bond():
    P = float(input("Enter the present value: "))
    i = float(input("Enter the the monthly Interest: "))
    n = int(input("Enter the number of months: "))
    i = (i/100)
    repayment = (i*P)/(1 - math.pow((1+i),(-n)))
    print("=====================================")
    print(f"You will repay: R{repayment}")
    print("=====================================")


# this is the condition that well the slection of the input is still relevent it should continue.
while True:
    mySelection = output() 
    if mySelection == 1 or mySelection == 2: 
        calculations(mySelection)  
    elif mySelection == 0:
        print("dankie")     
        break





