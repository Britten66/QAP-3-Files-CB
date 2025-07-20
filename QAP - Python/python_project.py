
#=======================================
#Comment Like A Semi-Pro
#Author: Christopher Britten
# SD-15 - Study Group 1
#Date: 2025-07-10
#Description: "Honest" Harry's Used Car Sales Tracker
#This program is designed to assist Harry in keeping track of his car sales.
#It Will collect customer data, vehicle info & calculate the fee's/HST, Total Cost & finally a payment plan
#This will be written using a loop for reusablitlity 
# ( END ) can be entered as the first name to exit program.
#=======================================

#=====
#Imports here. added formnat values 
#=====

import datetime

import FormatValues

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

LUX_TAX_RATE = 0.016


# MAX LENGTH FOR USED CAR LOAN 


#=====
#main program starts here
#=====
while True:
    #here is for the first name 
        while True:
            FirstName = input("Enter Your First Name ( Enter END To Cancel ): ")
            if FirstName == "END":
                print("Exiting now... Goodbye  ")
                exit()
            elif FirstName != "":
                FirstName = FirstName.title()
                break
            else:
             print("First Name Must Be Entered. ")

            #here is the validation for last name 
        while True:
            LastName = input("Enter Your Last Name: ")
            if LastName != "":
                LastName = LastName.title()
                break
            
            else:
                print("LAast Name Must Be Entered. ")

        #Phone Number Validation Here

        while True:
            Phone = input("Enter Your Phone Number (Max 10 Digits) ")
            if len(Phone) == 10 and Phone.isdigit():
                break
            else:
                print("Phone Number Must Be Exactly 10 Digits. ")
            
        while True:
            Plate = input("Enter Plate Number (XXX999) ").upper()
            if len(Plate) == 6 and Plate[:3].isalpha() and Plate[3:].isdigit(): # This was added and researched, to make sure the plate will be alphanumeric and digit 
                break
            else:
                print("Plate Must be 6 Characters long in the frmat XXX999 ")

      


        while True:
            CarYear =  input("Enter Car Year (e.x 2010) ")
            if CarYear.isdigit() and len(CarYear) == 4:
                break
            else:
                print("Please Enter Valid 4-digit Year")

        while True: 
            CarMake = input("Enter The Vehicle Make (E.x Toyota) ")
            if CarMake:
                break
            else:
                print("Car Model Must Be Entred ")

        while True: 
             CarMod = input("Enter The Vehicle Model (E.x LandCruiser) ")
             if CarMod:
                   break
             else:
              print("Car Make Must Be Entred ")
            #Selling Pirce Validation

        while True:
            mileage_input = input("Enter Kilometers (km): ")
            if mileage_input.isdigit():
                mileage = FormatValues.mileage_valid(mileage_input)
                break
            else:
                print("Please Enter Whole Number Mileage. ")

        while True: 
             try:
              SalePrice = 25000 #input("Enter Selling Price ( Up to $50,000 ) ")
              SalePrice = float(SalePrice)
              if SalePrice <= 50000:
                    
                    break
                    
              else:
                        print("Selling Price Must Be Less Than 50000")
             except ValueError:
                 print("Value Error Please Try Again")
            
        
        #Trade In Val - Validations

        while True:
            TradeVal = "1500" #input("Enter The Trade In Amount ( Cannot Exceed Sale Price ) : ")
            if TradeVal.isdigit():
                TradeVal = float(TradeVal)
                if TradeVal <= SalePrice:
                    break
                print("Trade in must be anumber no higher than the selling price. ")
        
        while True:
            SalePerson = "Craig" #input("Enter The Sales Person Name: ")
            if SalePerson != "":
                SalePerson = SalePerson.title()
                break
            else:   
                print("Sale Person Name Must Be Entered. ")
       




    #=====
    #Calulations Here. 
    #=====

  

        PriceAfterTrade = SalePrice - TradeVal
        TransFee = SalePrice * TRANS_FEE_RATE
        TransFee = float(TransFee)

        if PriceAfterTrade < LICENSE_PRICE_LIM:
            LicenseFee = LOW_LICENSE_FEE
        else:
            LicenseFee = HIGH_LICENSE_FEE

        SubTot = PriceAfterTrade + LicenseFee + TransFee
        SubTot = float(SubTot)


        #Subtotal finished. Now Here is the added Tax
        HST = PriceAfterTrade * HST_RATE
        HST = float(HST)

        #After Tax Added in here is Total Sales Price With Tax
        TotSalesPrice = PriceAfterTrade + LicenseFee + TransFee + HST
        TotSalesPrice = float(TotSalesPrice)

        #Lux Tax Here

        LuxTax = SalePrice * LUX_TAX_RATE
        TotSalesPrice += LuxTax


        print("Imported from:", FormatValues.Receipt_gen_id)
        
        ReceiptID = FormatValues.Receipt_gen_id(FirstName, LastName, Plate, Phone)

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
       # print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
        print()                                                                                             #adding dates like this allowed "/" ??
        print(f"Honest Harry's Car Sales                         Invoice Date:  {CURRENT_DATE.strftime('%a %d, %Y')}")
        print(f"Used Car Salles and Receipt                      Receipt No:    {ReceiptID} ")
        print()                                           
        print(f"                                           Sale Price:          ${SalePrice:>5,.2f}")#Sale Price Here-
        print(F"Sold to:                                   Trade Allowance:     ${TradeVal:>5,.2f}") #Add Trade Allowance Here-
        print("                                           -------------------------------------")
        print(f"{FirstName[0]}. {LastName}                                    Price After Trade:   ${PriceAfterTrade:>6,.2f}") #Price after Trade needs to be added -
        print(f"{FormatValues.format_phone(Phone)}                              License Fee:         ${LicenseFee:>5,.2f}") # Print Out License Fee Here -
        print(f"                                           Transfer Fee:        ${TransFee:>5,.2f}")
        print("                                           -------------------------------------")
        print(f" Car Details:                              SubTotal:            ${SubTot:>5,.2f}  ") # make sure to add lux tax etc etc 
        print(f" {CarYear} {CarMake}  {CarMod}                        HST:                 ${HST:>5,.2f}")
        print(f" Mileage: {mileage:<5,d}km                        -------------------------------------")
        # Ended Before Car Details 
        #Pick Up HEre
        print(f"                                           Total Sales Price:   ${TotSalesPrice:>5,.2f}")
        print()
        print("--------------------------------------------------------------------------------")
        print()
        print("                                 Financing        Total          Monthly ")
        print("  # Years      # Payments           Fee           Price          Payment")
        print("   ---------------------------------------------------------------------")

        for year in range(1,5):
            PayNum = year * 12
            FinFee = year * MONTHLY_INTERET
            TotalPrice = TotSalesPrice + FinFee
            MonthPay = TotalPrice / PayNum

            print(f"      {year:<11}  {PayNum:<16}${FinFee:<2,.2f}       ${TotalPrice:<2,.2f}      ${MonthPay:<4,.2f}")

        print("   ---------------------------------------------------------------------")
        print(f"                        First Payment Date:  {FormatValues.first_payment_date()}")
        print("-------------------------------------------------------------------------------")
        print("                            Best Used Cars In Town !! ")
        print()
        print()
       
        print()

        wait = input("Press Enter To Try Again")
