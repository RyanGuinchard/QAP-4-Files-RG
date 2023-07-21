# Program description: A program for the One Stop Insurance Company insurance policies
# Written by: Ryan Guinchard
# Written on: 07-18-2023

# Import libraries needed
import datetime as dt
import FormatValues as fv

# Define Constants / Read from file
f = open('OSICDef.dat', 'r')

POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_CARS = float(f.readline())
EXTRA_LIABILITY = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR_COV = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE_RATE = float(f.readline())

f.close()

# Main program

while True:

    # Grabbing user inputs
    firstName = input("Enter the customers first name: ").title()
    lastName = input("Enter the customers last name: ").title()

    address = input("Enter the customers address: ")
    city = input("Enter the customers city: ").title()

    provList = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
    while True:
        prov = input("Enter the customers province(LL): ").upper()

        if prov == "":
            print("Error - Province cannot be blank")
        elif prov not in provList:
            print("Error - Province not valid")
        else:
            break
    postCode = input("Enter the customer postal code(A1A1A1): ")
    phoneNum = input("Enter the customer phone number(9999999999): ")
    numCars = int(input("Enter the number of cars being insured: "))
    extraLiab = input("Enter if extra liability is wanted(Y/N): ").upper()
    glassInsur = input("Enter if glass insurance is wanted(Y/N): ").upper()
    loanerCar = input("Enter if loaner car is wanted(Y/N): ").upper()

    payMethList = ['Full', 'Monthly']
    while True:
        payMethod = input("Enter the payment method(Monthly/Full): ").title()
        if payMethod == "":
            print("Error - Payment method cannot be blank")
        elif payMethod not in payMethList:
            print("Error - Payment method must be Monthly or Full")
        else:
            break
    
    # Provide needed calculations
    if numCars > 1:
        discount = BASIC_PREM * ADD_CARS
        discCars = (numCars - 1) * discount
        insurPrem =  BASIC_PREM + discCars
    else:
        insurPrem = BASIC_PREM

    extraCosts = 0
    if extraLiab == "Y":
        extraCosts += EXTRA_LIABILITY * numCars

    if glassInsur == "Y":
        extraCosts+= GLASS_COV * numCars

    if loanerCar == "Y":
        extraCosts += LOANER_CAR_COV *numCars
    

    totalPrem = insurPrem + extraCosts
    hst = totalPrem * HST_RATE
    totalCost = totalPrem + hst

    # Calculating if customer wants to pay monthly or up front
    
    if payMethod == "Monthly":
        monthlyPay = (totalCost + PROCESS_FEE_RATE) / 8
    else:
        monthlyPay = 0
        pass
    
    # Grabbing current date and getting the next payment date
    currDate = dt.datetime.now().date()
    currDateStr = fv.FDateS(currDate)

    nextMonth = currDate + dt.timedelta(days=30)
    nextPay = nextMonth.replace(day=1)

    # Printing the results
    print()
    print("One Stop Insurance - Policy Receipt")
    print("=" * 35)
    print(f"Invoice date:  {currDateStr}")
    print(f"Policy Number: {POLICY_NUM:>4d}")
    print(f"Customer: {firstName} {lastName}")
    print(f"Address:  {address}")
    print(f"          {city}, {prov} {postCode}")
    print(f"Phone Number: {phoneNum}")
    print("=" * 35)
    print(f"Number of Cars:     {numCars:>15d}")
    print(f"Insurance Premium:        {fv.FDollar2(insurPrem):>9s}")
    print(f"Extra Liability:                  {extraLiab}")
    print(f"Glass Insurance:                  {glassInsur}")
    print(f"Extra Costs:              {fv.FDollar2(extraCosts):>9s}")
    print("=" * 35)
    print(f"Total Insurance Premium:  {fv.FDollar2(totalPrem):>9s}")
    print(f"HST:                      {fv.FDollar2(hst):>9s}")
    print(f"Total:                    {fv.FDollar2(totalCost):>9s}")
    print("=" * 35)
    print(f"Payment Method:           {payMethod:>9s}")
    if payMethod == "Monthly":
        print(f"Monthly Payment:          {fv.FDollar2(monthlyPay):>9s}")
        print(f"Next Payment:            {nextPay}")
    else:
        print(f"Upfront Payment:         {fv.FDollar2(BASIC_PREM):>9s}")
    print("=" * 35)

    print()
    print()
    print("Saving policy information...")

    # Write the policy information to a file
    f = open('Policies.dat', 'a')
    f.write(f"{POLICY_NUM}, {firstName}, {lastName}, {address}, {city}, {prov}, {postCode}, {phoneNum}, {numCars}, {extraLiab}, {glassInsur}, {loanerCar}, {payMethod}, {totalPrem}\n")
    f.close()
    print("Policy information processed and saved.")

    # Updating policy number
    POLICY_NUM += 1


    # Updating default file
    f = open('OSICDef.dat', 'w')
    f.write(f"{POLICY_NUM}\n")
    f.write(f"{BASIC_PREM}\n")
    f.write(f"{ADD_CARS}\n")
    f.write(f"{EXTRA_LIABILITY}\n")
    f.write(f"{GLASS_COV}\n")
    f.write(f"{LOANER_CAR_COV}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_FEE_RATE}\n")
    f.close()

    # Giving option to end invoice adding
    Continue = input("Would you like to enter another customer? (Y/N): ").upper()
    if Continue == "N":
        break