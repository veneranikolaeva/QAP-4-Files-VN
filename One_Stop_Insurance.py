#Program to enter and calculate new insurance policy information for customers
#Date written - November 29, 2023
#Author - Venera Nikolaeva

import datetime
#Default values
next_policy_number = 1944
basic_premium = 869.00
discount_additional_cars = 0.25
cost_extra_liability = 130.00
cost_glass_coverage = 86.00
cost_loaner_car = 58.00
hst_rate = 0.15
processing_fee = 39.99

#Lists to store previous claims
claim_dates = []
claim_amounts = []

#Function to validate province
def validate_province(province):
    provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
    return province.upper() in provinces

#Function to calculate total premium
def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    total_premium = basic_premium + (basic_premium * discount_additional_cars * (num_cars - 1))
    total_extra_costs= 0

    if extra_liability == 'Y':
        total_extra_costs += cost_extra_liability * num_cars

    if glass_coverage == 'Y':
        total_extra_costs += cost_glass_coverage * num_cars

    if loaner_car == 'Y':
        total_extra_costs += cost_loaner_car * num_cars

    total_premium += total_extra_costs
    return total_premium

#Function to calculate total cost
def calculate_total_cost(total_premium):
    hst = total_premium * hst_rate
    total_cost = total_premium + hst
    return total_cost 

#Function to calculate monthly payment
def calculate_monthly_payment(total_cost, payment_method, down_payment=0):
    if payment_method == 'Full':
        monthly_payment = total_cost / 8
    elif payment_method == 'Monthly':
        monthly_payment = (total_cost + processing_fee) / 8
    elif payment_method == 'Down Pay':
        total_cost -=down_payment
        monthly_payment = (total_cost + processing_fee) / 8
    return monthly_payment

#Function to display receipt
def display_receipt(first_name, last_name, address, city, province, postal_code, phone_number, num_cars, extra_liability, glass_coverage, loaner_car, payment_method, down_payment, total_premium, total_cost):
    print("=====================================")
    print("       One Stop Insurance       ")

    print("=====================================")
    print("Customer Information:")
    print("Name: {}{}".format(first_name.title(), last_name.title()))
    print("Address: {}".format(address))
    print("City: {}".format(city.title()))
    print("Province: {}".format(province.upper()))
    print("Postal Code: {}".format(postal_code))
    print("Phone Number: {}".format(phone_number))
    print("Number of Cars: {}".format(phone_number))
    print("Extra Liability: {}".format(extra_liability))
    print("Glass Coverage: {}".format(glass_coverage))
    print("Loaner Car: {}".format(loaner_car))
    print("Payment Method: {}".format(payment_method))
    if payment_method == 'Down Pay':
        print("Down Payment: ${:2f}".format(down_payment))

    print("======================================")
    print("Premium Information:")
    print("Total Premium: ${:.2f}".format(total_premium))
    print("Total Cost: ${:.2f}".format(total_cost))

    print("======================================")
    print("Previous Claims:")
    print("Claim #      Claim Date      Amount")
    print("--------------------------------------")
    for i in range(len(claim_dates)):
        print("{}.{} ${:,.2f}".format(i+1, claim_dates[[i].strftime('%Y-%m-%d'), claim_amounts[i]]))
    
    print("======================================")

#Main program
while True:
    print("enter customer information:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    city = input("City: ")
    province = input("Province (2-letter code): ")
    while not validate_province(province):
        print("Invalid province. Please enter a valid 2-letter code.")
        province = input("Province (2-letter code): ")
        postal_code = input("Postal Code: ")
        phone_number = input("Phone Number: ")
        num_cars = int(input("Number of Cars: "))
        extra_liability = input("Extra Liability (Y/N): ").upper()
        glass_coverage = input("Glass Coverage (Y/N): ").upper()
        loaner_car = input("Loaner Car (Y/N): ").upper()
        payment_method = input("Payment Method (Full/Monthly/Down Pay): ").title()
        if payment_method == 'Down Pay':
            down_payment = float(input("Down Payment Amount: $"))
        else:
            down_payment = 0

        total_premium = calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car)
        total_cost = calculate_total_cost(total_premium)    
        monthly_payment = calculate_monthly_payment(total_cost, payment_method, down_payment)

        #Add current date as claim date
        claim_dates.append(datetime.date.today())
        claim_amounts.append(total_cost)

        display_receipt(first_name, last_name, address, city, province, postal_code, phone_number, num_cars, extra_liability, glass_coverage, loaner_car, payment_method, down_payment, total_premium, total_cost)

        repeat = input("Do you want to enter another customer? (Y/N): ").upper()
        if repeat != 'Y':
            break




