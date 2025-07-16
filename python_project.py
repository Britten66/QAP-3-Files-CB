
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

TRANS_FEE_RATE = 0.01

MAX_SELLING_PRICE = 50000.00

MONTHLY_INTERET = 39.99

MAX_YEARS = 4 

# MAX LENGTH FOR USED CAR LOAN 


#=====
#Here The Functions Are Listed. 
#=====


def format_phone(Phone):

    area = Phone[0:3]
    middle = Phone[3:6]
    end = Phone[6:10]
    return "(" + area + ")" + middle + "-" + end 

def first_payment_date():
    one_month = datetime.timedelta(days=30)
    return (CURRENT_DATE + one_month).strftime("%b %d, %Y")


# receipt ID here 
def Receipt_gen_id():

    FirstName = "Duffy" #input("Enter Your First Name: ")
    LastName = "McDufferson" #input("Enter Your Last Name: ")
    Plate = "Duff4588" #input("Enter Your Plate Number: ")
    Phone = "7095365548" #input("Enter Your Phone Number: ")
    CarDetail = input("Please Enter The Car Make: ")
     
    if len(Phone) == 10 and Phone.isdigit():
     LastFourPhone = Phone[-4:]

    else:
            print("Phone Number Is invalid. Please try again")
            return

    Initials = FirstName[0].upper() + LastName[0].upper()
    LastThreePlate = Plate[-3:]
   
   # formatting the phone number funciton here


#=====
#Calulations Here. 
#=====

    SalePrice = input("Confirm Sale Price ($) : ")
    SalePrice = float(SalePrice)
    TradeAllow = 5000.00
    TradeAllow = float(TradeAllow)
    PriceAfterTrade = SalePrice - TradeAllow
    TransFee = SalePrice * TRANS_FEE_RATE
    TransFee = float(TransFee)

    if PriceAfterTrade < LICENSE_PRICE_LIM:
        LicenseFee = LOW_LICENSE_FEE
    else:
        LicenseFee = HIGH_LICENSE_FEE
    
    SubTot = SalePrice - PriceAfterTrade + LicenseFee
    SubTot = float(SubTot)
    #Subtotal finished. Now Here is the added Tax
    HST = PriceAfterTrade * HST_RATE
    HST = float(HST)
    #After Tax Added in here is Total Sales Price With Tax
    TotSalesPrice = PriceAfterTrade + LicenseFee + HST
    TotSalesPrice = float(TotSalesPrice)


    ReceiptID = Initials + "-" + LastThreePlate + "-" + LastFourPhone 

#=====
#Loop Entry Here.
#=====


#=====
#Output Starts Right Here.
#=====
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
    print(f"                                           Sale Price:          ${SalePrice:>5,.2f}")#Sale Price Here-
    print(F"Sold to:                                   Trade Allowance:     ${TradeAllow:>5,.2f}") #Add Trade Allowance Here-
    print("                                           -------------------------------------")
    print(f"{FirstName[0]}. {LastName}                             Price After Trade:   ${PriceAfterTrade:>5,.2f}") #Price after Trade needs to be added -
    print(f"{format_phone(Phone)}                              License Fee:         ${LicenseFee:>5,.2f}") # Print Out License Fee Here -
    print(f"                                           Transfer Fee:        ${TransFee:>5,.2f}")
    print("                                           -------------------------------------")
    print(f"Car Details:                               SubTotal:            ${SubTot:>5,.2f}  ") # make sure to add lux tax etc etc 
    print(f"                                           HST:                 ${HST:>5,.2f}")
    print("                                           -------------------------------------")
    # Ended Before Car Details 
    #Pick Up HEre
    print(f"                                           Total Sales Price:   ${TotSalesPrice:>5,.2f}")
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
    print(f"   First Payment Date:  {first_payment_date()}")
    print("-------------------------------------------------------------------------------")
    print("                            Best Used Cars In Town !! ")
    print()
    print()
    print()
    
    return ReceiptID, format_phone(Phone)
    



    


    


#Return Funciton 

Receipt_gen_id()