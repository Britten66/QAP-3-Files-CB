
#=======================================
#Comment Like A Semi-Pro
#Author: Christopher Britten
# SD-15
#Date: 2025-07-10
#Description: "Honest" Harry's Used Car Sales Tracker
#This program is designed to assist Harry in keeping track of his car sales.
#It Will collect customer data, vehicle info & calculate the fee's/HST, Total Cost & finally a payment plan
#This will be written using a loop for reusablitlity 
# ( END ) can be entered as the first name to exit program.
#=======================================

#=====
#Imports here. 
#=====

import datetime

#=====
#Current Date Here
#=====
CURRENT_DATE = datetime.datetime.now() 

#=====
#Constants Listed Here. 
#=====

HST_RATE = .15

LOW_LICENSE_FEE = 75.00 

HIGH_LICENSE_FEE = 165.00

LICENSE_PRICE_LIM = 15000.00

MAX_SELLING_PRICE = 50000.00

MONTHLY_INTERET = 39.99

MAX_YEARS = 4 

# MAX LENGTH FOR USED CAR LOAN 


#=====
#Here The Functions Are Listed. 
#=====
# formatting the phone number funciton here

def Format_phone(Phone):

    area = Phone[0:3]
    middle = Phone[3:6]
    end = Phone[6:10]
    return "(" + area + ")" + middle + "-" + end 

# receipt ID here 
def Receipt_gen_id():

    FirstName = "Duffy" #input("Enter Your First Name: ")
    LastName = "McDufferson" #input("Enter Your Last Name: ")
    Plate = "Duff4588" #input("Enter Your Plate Number: ")
    Phone = "7095365548" #input("Enter Your Phone Number: ")
    Formatted = format_phone(Phone)
    

    Initials = FirstName[0].upper() + LastName[0].upper()
    LastThreePlate = Plate[-3:]

def CalcTotal(Selling, TradeInAmount):
    
#=====
#User Input Starts Here. 
#=====

#Validation For Phone Numer Entery
    if len(Phone) == 10 and Phone.isdigit():
        LastFourPhone = Phone[-4:]
    else:
        print("Phone Nuymber Is invalid. Please try again")
        return
    
    ReceiptID = Initials + "-" + LastThreePlate + "-" + LastFourPhone 

    print("Receipt ID : " , ReceiptID)
    print(Formatted)


    




#=====
#Calulations Here. 
#=====


#=====
#Loop Entry Here.
#=====


#=====
#Output Starts Right Here.
#=====
