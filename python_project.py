
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

HST_RATE = 0.15

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

def format_phone(Phone):

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
     
    if len(Phone) == 10 and Phone.isdigit():
     LastFourPhone = Phone[-4:]

    else:
        print("Phone Number Is invalid. Please try again")


    Initials = FirstName[0].upper() + LastName[0].upper()
    LastThreePlate = Plate[-3:]




    ReceiptID = Initials + "-" + LastThreePlate + "-" + LastFourPhone 

        #Here comments are used to help line up my invoice output details
    print()
    print()
    print()#Kept format as per the QAP instructions in this part. Refraining from any kind of change that is not needed
                    #1        #2        #3        #4        #5        #6        #7         #8
                    #         #         #         #         #         #         #         #
    print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
    print()                                                                                             #adding dates like this allowed "/" ??
    print("Honest Harry's Car Sales                         Invoice Date:",CURRENT_DATE.strftime("%a %m, %Y"))
    print("Used Car Salles and Receipt                      Receipt No:   ",   ReceiptID)
    print()                                           
    print("                                           Sale Price:",)#Sale Price Here-
    print("Sold to:                                   Trade Allowance:",)#Add Trade Allowance Here-
    print("                                           -------------------------------------")
    print(f"{FirstName[0]}. {LastName}                             Price After Trade:") #Price after Trade needs to be added -
    print(f"{format_phone(Phone)}                              License Fee:",) # Print Out License Fee Here -
    print("                                           Transfer Fee:")
    print("                                           -------------------------------------")
    print("Car Details:                               SubTotal:")
    print("                                           HST:")
    print("                                           -------------------------------------")
            # Ended Before Car Details 
        #Pick Up HEre
    print("                                           Total Sales Price: ")
    print()
    print("--------------------------------------------------------------------------------")
    print()
    print("                                 Financing        Total          Monthly ")
    print("  # Years      # Payments           Fee           Price          Payment")
    print("   ---------------------------------------------------------------------")
    print("      1              12           $999.99       $99,999.99     $9,999.99")
    print("      2              22           $999.99       $99,999.99     $9,999.99")
    print("      3              36           $999.99       $99,999.99     $9,999.99")
    print("      4              48           $999.99       $99,999.99     $9,999.99")
    print("   ---------------------------------------------------------------------")
    print("   First Payment Date: ")
    print("--------------------------------------------------------------------------------")
    return ReceiptID, format_phone
    



    


    



#=====
#Calulations Here. 
#=====


#=====
#Loop Entry Here.
#=====


#=====
#Output Starts Right Here.
#=====
Receipt_gen_id()