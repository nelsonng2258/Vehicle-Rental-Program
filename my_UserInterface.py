#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:37:16 2022

@author: nelsonng
"""

# Import python libraries. 
import json 
import time 

# Import customized class packages.
from my_package import Car
from my_package import Van
from my_package import Truck
from my_package import VehicleCost 

#-----------------------------------------------------------------------------
# Inputs for user-interface 
#-----------------------------------------------------------------------------

# Vehicle # 
# Read vehicle data from txt files of car, van and truck - structured as a dictionary with list for each list.
with open('./Data/vehicle_car_data.txt') as json_cardata:
    vehiclecardata = json.load(json_cardata)
   
with open('./Data/vehicle_van_data.txt') as json_vandata:
    vehiclevandata = json.load(json_vandata)
    
with open('./Data/vehicle_truck_data.txt') as json_truckdata:
    vehicletruckdata = json.load(json_truckdata)

# Car (Vehicle) #  
# Cars c1 to c7 are created from vehicle_car_data.txt file. 
c1 = Car(vehiclecardata["make_model"][0],
         vehiclecardata["mpg"][0],
         vehiclecardata["numPassengers"][0],
         vehiclecardata["numDoors"][0], 
         vehiclecardata["vin"][0])

c2 = Car(vehiclecardata["make_model"][1],
         vehiclecardata["mpg"][1],
         vehiclecardata["numPassengers"][1],
         vehiclecardata["numDoors"][1],
         vehiclecardata["vin"][1])

c3 = Car(vehiclecardata["make_model"][2],
         vehiclecardata["mpg"][2],
         vehiclecardata["numPassengers"][2],
         vehiclecardata["numDoors"][2],
         vehiclecardata["vin"][2])

c4 = Car(vehiclecardata["make_model"][3],
         vehiclecardata["mpg"][3],
         vehiclecardata["numPassengers"][3],
         vehiclecardata["numDoors"][3],
         vehiclecardata["vin"][3])

c5 = Car(vehiclecardata["make_model"][4],
         vehiclecardata["mpg"][4],
         vehiclecardata["numPassengers"][4],
         vehiclecardata["numDoors"][4],
         vehiclecardata["vin"][4])

c6 = Car(vehiclecardata["make_model"][5],
         vehiclecardata["mpg"][5],
         vehiclecardata["numPassengers"][5],
         vehiclecardata["numDoors"][5],
         vehiclecardata["vin"][5])

c7 = Car(vehiclecardata["make_model"][6],
         vehiclecardata["mpg"][6],
         vehiclecardata["numPassengers"][6],
         vehiclecardata["numDoors"][6],
         vehiclecardata["vin"][6])

# Van (Vehicle) # 
# Cars v1 to v7 are created from vehicle_van_data.txt file. 
v1 = Van(vehiclevandata["make_model"][0],
         vehiclevandata["mpg"][0],
         vehiclevandata["numPassengers"][0],
         vehiclevandata["vin"][0])

v2 = Van(vehiclevandata["make_model"][1],
         vehiclevandata["mpg"][1],
         vehiclevandata["numPassengers"][1],
         vehiclevandata["vin"][1])

v3 = Van(vehiclevandata["make_model"][2],
         vehiclevandata["mpg"][2],
         vehiclevandata["numPassengers"][2],
         vehiclevandata["vin"][2])

v4 = Van(vehiclevandata["make_model"][3],
         vehiclevandata["mpg"][3],
         vehiclevandata["numPassengers"][3],
         vehiclevandata["vin"][3])

v5 = Van(vehiclevandata["make_model"][4],
         vehiclevandata["mpg"][4],
         vehiclevandata["numPassengers"][4],
         vehiclevandata["vin"][4])

v6 = Van(vehiclevandata["make_model"][5],
         vehiclevandata["mpg"][5],
         vehiclevandata["numPassengers"][5],
         vehiclevandata["vin"][5])

v7 = Van(vehiclevandata["make_model"][6],
         vehiclevandata["mpg"][6],
         vehiclevandata["numPassengers"][6],
         vehiclevandata["vin"][6])

# Truck (Vehicle) # 
# Trucks t1 to t7 are created from vehicle_truck_data.txt file. 
t1 = Truck(vehicletruckdata["mpg"][0],
           vehicletruckdata["length"][0],
           vehicletruckdata["num_rooms"][0],
           vehicletruckdata["vin"][0])

t2 = Truck(vehicletruckdata["mpg"][1],
           vehicletruckdata["length"][1],
           vehicletruckdata["num_rooms"][1],
           vehicletruckdata["vin"][1])

t3 = Truck(vehicletruckdata["mpg"][2],
           vehicletruckdata["length"][2],
           vehicletruckdata["num_rooms"][2],
           vehicletruckdata["vin"][2])

t4 = Truck(vehicletruckdata["mpg"][3],
           vehicletruckdata["length"][3],
           vehicletruckdata["num_rooms"][3],
           vehicletruckdata["vin"][3])

t5 = Truck(vehicletruckdata["mpg"][4],
           vehicletruckdata["length"][4],
           vehicletruckdata["num_rooms"][4],
           vehicletruckdata["vin"][4])

t6 = Truck(vehicletruckdata["mpg"][5],
           vehicletruckdata["length"][5],
           vehicletruckdata["num_rooms"][5],
           vehicletruckdata["vin"][5])

t7 = Truck(vehicletruckdata["mpg"][6],
           vehicletruckdata["length"][6],
           vehicletruckdata["num_rooms"][6],
           vehicletruckdata["vin"][6]) 

#-----------------------------------------------------------------------------

# Vehicle cost #  
# Read vehicle cost text - structured as a dictionary with list for each list. 
with open('./Data/vehicle_cost.txt') as json_vehcost:
    vehiclecostdata = json.load(json_vehcost)

# Get the index of car from the vehicle cost txt. 
carcostindex = vehiclecostdata['Vehicle Type'].index('Car')

# Feed in the cost for car. 
car_cost = VehicleCost(vehiclecostdata['Vehicle Type'][carcostindex], 
                       vehiclecostdata['Daily Rate'][carcostindex], 
                       vehiclecostdata['Weekly Rate'][carcostindex], 
                       vehiclecostdata['Per Mile Charge'][carcostindex],
                       vehiclecostdata['Insurance Charge'][carcostindex])

# Get the index of van from the vehicle cost txt. 
vancostindex = vehiclecostdata['Vehicle Type'].index('Van') 

# Feed in the cost for van.  
van_cost = VehicleCost(vehiclecostdata['Vehicle Type'][vancostindex], 
                       vehiclecostdata['Daily Rate'][vancostindex], 
                       vehiclecostdata['Weekly Rate'][vancostindex], 
                       vehiclecostdata['Per Mile Charge'][vancostindex],
                       vehiclecostdata['Insurance Charge'][vancostindex])

# Get the index of truck from the vehicle cost txt. 
truckcostindex = vehiclecostdata['Vehicle Type'].index('Truck') 

# Feed in the cost for truck. 
truck_cost = VehicleCost(vehiclecostdata['Vehicle Type'][truckcostindex], 
                         vehiclecostdata['Daily Rate'][truckcostindex], 
                         vehiclecostdata['Weekly Rate'][truckcostindex], 
                         vehiclecostdata['Per Mile Charge'][truckcostindex],
                         vehiclecostdata['Insurance Charge'][truckcostindex]) 

# Create a vin list to store all the valid vin. 
vin_list = []

# Iterate over all elements within the car's vin list to build a compiled vin list. 
for k1 in vehiclecardata["vin"]:
    vin_list.append(k1)
    
# Iterate over all elements within the van's vin list to build a compiled vin list.   
for k2 in vehiclevandata["vin"]:
    vin_list.append(k2) 
    
# Iterate over all elements within the truck's vin list to build a compiled vin list. 
for k3 in vehicletruckdata["vin"]:
    vin_list.append(k3)

#-----------------------------------------------------------------------------

# Reservation List# 
# Read reservation text - structured as a dictionary with list for each keys [to append later on]. 
with open('./Data/listofreservation.txt') as json_reservationlist:
    reservationdata = json.load(json_reservationlist)

#-----------------------------------------------------------------------------
# User interfaces 
#-----------------------------------------------------------------------------

def menu(): 

    '''User Interface: Main Menu - display options in main menu.'''
    
    print("*************************************************")
    print("* Welcome to the Friendly Vehicle Rental Agency *")
    print("*************************************************\n")
    print("<<< MAIN MENU >>>")
    print("[1] Display vehicle types")
    print("[2] Check rental costs")
    print("[3] Check available vehicles")
    print("[4] Get cost of specific rental")
    print("[5] Make a reservation")
    print("[6] View / Cancel a reservation")
    print("[7] Quit\n")

def vehtype():
    
    '''User Interface: [1] Vehicle Types - display vehicle types and return to main menu.'''
    
    print("------ Types of Vehicles Available for Rent ------")
    print("[1] Car")
    print("Recommended for: Casual drives down the town, short getaways or running errands over the weekends.\n")
    print("[2] Van")
    print("Recommended for: Road trip adventures.\n")
    print("[3] Truck")
    print("Recommended for: Transportation of large and bulky items for house moving or business needs.")
    print("--------------------------------------------------\n")
    print("Returning back to the main menu ......\n")
    
    # Time delay of 3 second then return to main menu as not required to do any input/function in [1]. 
    time.sleep(3)
    menu() 

def vehrentalcost():
    
    '''User Interface: [2] Vehicle rental costs - display rental costs for each vehicle type selection.'''
    
    print("Please enter the type of vehicle. ")
    print("[1] Car")
    print("[2] Van")
    print("[3] Truck\n")
    
    bool_flag = True 
    
    # while loop for input validity on vehicle type. 
    while bool_flag:
    
        vehicle_type = input("Enter: ")
        
        # Display car rental cost. 
        if vehicle_type == "1":
            bool_flag = False
            print("---------- Rental Charges for Cars ----------\n")
            print("Daily     Weekly     Per Mile     Daily")
            print("Rate      Rate       Charges      Insurance")
            print("(S$)      (S$)       (S$)         (S$)\n")
            print("{}     {}        {}         {}".format(car_cost.daily_rate, 
                                                          car_cost.weekly_rate, 
                                                          car_cost.per_mile_chrg, 
                                                          car_cost.insur_rate)) 
            print("---------------------------------------------\n")
        
        # Display van rental cost. 
        elif vehicle_type == "2":
            bool_flag = False
            print("---------- Rental Charges for Vans ----------\n")
            print("Daily     Weekly     Per Mile     Daily")
            print("Rate      Rate       Charges      Insurance")
            print("(S$)      (S$)       (S$)         (S$)\n")
            print("{}        {}        {}          {}".format(van_cost.daily_rate, 
                                                              van_cost.weekly_rate, 
                                                              van_cost.per_mile_chrg, 
                                                              van_cost.insur_rate))
            print("---------------------------------------------\n")
        
        # Display truck rental cost. 
        elif vehicle_type == "3":
            bool_flag = False
            print("--------- Rental Charges for Trucks ---------\n")
            print("Daily     Weekly     Per Mile     Daily")
            print("Rate      Rate       Charges      Insurance")
            print("(S$)      (S$)       (S$)         (S$)\n")
            print("{}     {}        {}         {}".format(truck_cost.daily_rate, 
                                                          truck_cost.weekly_rate, 
                                                          truck_cost.per_mile_chrg, 
                                                          truck_cost.insur_rate))
            print("---------------------------------------------\n")
        
        else:
            print("Invalid option. Please try again.") 

def checkavailvehicle():
    
    '''User Interface: [3] Check available vehicle.'''
    
    print("Please enter the type of vehicle. ")
    print("[1] Car")
    print("[2] Van") 
    print("[3] Truck\n")
    
    bool_flag = True 
    
    # while loop for input validity on vehicle type. 
    while bool_flag:            
        
        vehicle_type2 = input("Enter: ") 
        
        if vehicle_type2 == "1":
            bool_flag = False
            print("---------------------------- Available Cars ----------------------------\n")
            print("Make /              Mileage     Number of     Number of    Vehicle")
            print("Model               (mpg)       Passengers    Doors        ID Number\n")
            
            # If c1 - C7 are not in reservationdata -> means they are not reserved and should be reflected as available. 
            if c1.vin not in reservationdata['Vehicle ID Number']:  
                print("{}    {}          {}             {}            {}".format(c1.make_model, 
                                                                                 c1.mpg, 
                                                                                 c1.numPassengers,
                                                                                 c1.numDoors, 
                                                                                 c1.vin))  
                
            if c2.vin not in reservationdata['Vehicle ID Number']: 
                print("{}    {}          {}             {}            {}".format(c2.make_model, 
                                                                                 c2.mpg, 
                                                                                 c2.numPassengers,
                                                                                 c2.numDoors, 
                                                                                 c2.vin))
                
            if c3.vin not in reservationdata['Vehicle ID Number']: 
                print("{}         {}          {}             {}            {}".format(c3.make_model, 
                                                                                      c3.mpg, 
                                                                                      c3.numPassengers,
                                                                                      c3.numDoors, 
                                                                                      c3.vin))
                
            if c4.vin not in reservationdata['Vehicle ID Number']:
                print("{}  {}          {}             {}            {}".format(c4.make_model, 
                                                                               c4.mpg, 
                                                                               c4.numPassengers,
                                                                               c4.numDoors, 
                                                                               c4.vin))
                
            if c5.vin not in reservationdata['Vehicle ID Number']:
                print("{}  {}          {}             {}            {}".format(c5.make_model, 
                                                                               c5.mpg, 
                                                                               c5.numPassengers,
                                                                               c5.numDoors, 
                                                                               c5.vin))
                
            if c6.vin not in reservationdata['Vehicle ID Number']: 
                print("{}    {}          {}             {}            {}".format(c6.make_model, 
                                                                                 c6.mpg, 
                                                                                 c6.numPassengers,
                                                                                 c6.numDoors, 
                                                                                 c6.vin))
                
            if c7.vin not in reservationdata['Vehicle ID Number']: 
                print("{}    {}          {}             {}            {}".format(c7.make_model, 
                                                                                 c7.mpg, 
                                                                                 c7.numPassengers,
                                                                                 c7.numDoors, 
                                                                                 c7.vin))
            
            print("\n------------------------------------------------------------------------\n")
            
        elif vehicle_type2 == "2":
            bool_flag = False
            print("---------------------------- Available Vans ----------------------------\n")
            print("Make /                    Mileage     Number of     Vehicle")
            print("Model                     (mpg)       Passengers    ID Number\n")
            
            # If v1 - v7 are not in reservationdata -> means they are not reserved and should be reflected as available. 
            if v1.vin not in reservationdata['Vehicle ID Number']:
                print("{}     {}          {}             {}".format(v1.make_model, 
                                                                    v1.mpg, 
                                                                    v1.numPassengers,
                                                                    v1.vin))  
                
            if v2.vin not in reservationdata['Vehicle ID Number']:
                print("{}     {}          {}             {}".format(v2.make_model, 
                                                                    v2.mpg, 
                                                                    v2.numPassengers,
                                                                    v2.vin))
                
            if v3.vin not in reservationdata['Vehicle ID Number']:
                print("{}     {}          {}             {}".format(v3.make_model, 
                                                                    v3.mpg, 
                                                                    v3.numPassengers,
                                                                    v3.vin))
                
            if v4.vin not in reservationdata['Vehicle ID Number']:
                print("{}             {}          {}             {}".format(v4.make_model, 
                                                                            v4.mpg, 
                                                                            v4.numPassengers,
                                                                            v4.vin))
                
            if v5.vin not in reservationdata['Vehicle ID Number']:
                print("{}             {}          {}             {}".format(v5.make_model, 
                                                                            v5.mpg, 
                                                                            v5.numPassengers,
                                                                            v5.vin))
                
            if v6.vin not in reservationdata['Vehicle ID Number']:
                print("{}           {}          {}             {}".format(v6.make_model, 
                                                                          v6.mpg, 
                                                                          v6.numPassengers,
                                                                          v6.vin))
                
            if v7.vin not in reservationdata['Vehicle ID Number']:
                print("{}           {}          {}             {}".format(v7.make_model, 
                                                                          v7.mpg, 
                                                                          v7.numPassengers,
                                                                          v7.vin)) 
            
            print("\n------------------------------------------------------------------------\n")
        
        elif vehicle_type2 == "3":
            bool_flag = False
            print("---------------------------- Available Trucks ----------------------------\n")
            print("Make /               Mileage     Cargo     Vehicle")
            print("Model                (mpg)       Space     ID")            
            print("                                (Bedroom)  Number\n")
            
            # If t1 - t7 are not in reservationdata -> means they are not reserved and should be reflected as available. 
            if t1.vin not in reservationdata['Vehicle ID Number']:
                print("{}             {}          {}         {}".format(t1.length, 
                                                                        t1.mpg, 
                                                                        t1.num_rooms,
                                                                        t1.vin))  
                
            if t2.vin not in reservationdata['Vehicle ID Number']:
                print("{}             {}          {}         {}".format(t2.length, 
                                                                        t2.mpg, 
                                                                        t2.num_rooms,
                                                                        t2.vin)) 
                
            if t3.vin not in reservationdata['Vehicle ID Number']:
                print("{}       {}          {}         {}".format(t3.length, 
                                                                  t3.mpg, 
                                                                  t3.num_rooms,
                                                                  t3.vin))
                
            if t4.vin not in reservationdata['Vehicle ID Number']: 
                print("{}       {}          {}         {}".format(t4.length, 
                                                                  t4.mpg, 
                                                                  t4.num_rooms,
                                                                  t4.vin))
                
            if t5.vin not in reservationdata['Vehicle ID Number']:
                print("{}     {}           {}         {}".format(t5.length, 
                                                                 t5.mpg, 
                                                                 t5.num_rooms,
                                                                 t5.vin))
                
            if t6.vin not in reservationdata['Vehicle ID Number']:
                print("{}     {}           {}         {}".format(t6.length, 
                                                                 t6.mpg, 
                                                                 t6.num_rooms,
                                                                 t6.vin))
                
            if t7.vin not in reservationdata['Vehicle ID Number']:
                print("{}     {}           {}         {}".format(t7.length, 
                                                                 t7.mpg, 
                                                                 t7.num_rooms,
                                                                 t7.vin))
            
            print("\n------------------------------------------------------------------------\n")
            
        else:
            print("Invalid option. Please try again.") 

def calculaterentalcost():
    
    '''User Interface: [4]  Get cost of specific rental: Main calculate rental cost for all vehicle.'''
    
    print("Please enter the type of vehicle. ")
    print("[1] Car")
    print("[2] Van")
    print("[3] Truck\n") 
    
    bool_flag = True 
    
    # while loop for input validity on vehicle type. 
    while bool_flag:            
        
        vehicle_type2 = input("Enter: ")
        
        if vehicle_type2 == "1":
            bool_flag = False
            subfunc_calculaterentalcost("Car")
            
        elif vehicle_type2 == "2":
            bool_flag = False
            subfunc_calculaterentalcost("Van")
        
        elif vehicle_type2 == "3":
            bool_flag = False
            subfunc_calculaterentalcost("Truck")
            
        else:
            print("Invalid option. Please try again.")   

def subfunc_calculaterentalcost(vehicle_type):
    
    '''User Interface: [4]  Get cost of specific rental: Sub-calculate rental cost for all vehicle.'''
    
    bool_flag = True 
    
    # while loop for input validity. 
    while bool_flag: 

        rental_period = input("How many days do you need the vehicle for? ")
    
        # Input validity on rental days -> must be numeric. 
        if rental_period.isdigit() == True: 
            miles_driving = input("How many miles do you expect to drive for? ")
        
            # Input validity on rental miles -> must be numeric. 
            if miles_driving.isdigit() == True:
            
                # Convert input of rental period and miles into integer for calculation.  
                rental_period = int(rental_period)
                miles_driving = int(miles_driving) 
                insurance_opt = input("Would you like to opt for insurance coverage? (Y/N)")
                
                # Segregate based on insurance_opt. 
                if insurance_opt == "Y":
                    want_insurance = 1
                    
                    if vehicle_type == "Car":
                        totalcost = car_cost.calcrentalcost(vehicle_type, rental_period, 
                                                            want_insurance, miles_driving)
                        charge_per_mile = car_cost.per_mile_chrg
                        
                    elif vehicle_type == "Van": 
                        totalcost = van_cost.calcrentalcost(vehicle_type, rental_period, 
                                                            want_insurance, miles_driving)
                        charge_per_mile = van_cost.per_mile_chrg
                        
                    elif vehicle_type == "Truck":
                        totalcost = truck_cost.calcrentalcost(vehicle_type, rental_period, 
                                                              want_insurance, miles_driving)
                        charge_per_mile = truck_cost.per_mile_chrg
                    
                    print("\n---------- Estimated Rental Charges ----------\n")
                    print("Vehicle type: {}".format(vehicle_type))
                    print("Rental period: {} days".format(rental_period))
                    print("Estimated driving miles: {} miles".format(miles_driving))
                    print("Charge per mile: S${}".format(charge_per_mile))
                    print("Insurance coverage: Opted in\n")
                    print("Your estimated total rental cost would be S${}.".format(totalcost))
                    bool_flag = False
                
                elif insurance_opt == "N":
                    want_insurance = 0
                    
                    if vehicle_type == "Car":
                        totalcost = car_cost.calcrentalcost(vehicle_type, rental_period, 
                                                            want_insurance, miles_driving)
                        charge_per_mile = car_cost.per_mile_chrg
                        
                    elif vehicle_type == "Van": 
                        totalcost = van_cost.calcrentalcost(vehicle_type, rental_period, 
                                                            want_insurance, miles_driving)
                        charge_per_mile = van_cost.per_mile_chrg
                        
                    elif vehicle_type == "Truck":
                        totalcost = truck_cost.calcrentalcost(vehicle_type, rental_period, 
                                                              want_insurance, miles_driving)
                        charge_per_mile = truck_cost.per_mile_chrg
                    
                    print("\n---------- Estimated Rental Charges ----------\n")
                    print("Vehicle type: {}".format(vehicle_type))
                    print("Rental period: {} days".format(rental_period))
                    print("Estimated driving miles: {} miles".format(miles_driving))
                    print("Charge per mile: S${}".format(charge_per_mile))
                    print("Insurance coverage: Opted out\n")
                    print("Your estimated total rental cost would be S${}.".format(totalcost))
                    bool_flag = False
                
                # Input validity on insurance coverage choice -> must be "Y" or "N". 
                else: 
                    print("Invalid input choice. Please re-enter all the inputs again.")
            
            else: 
                print("Invalid number of miles. Please re-enter all the inputs again.")
            
        else: 
            print("Invalid days of rental. Please re-enter days of rental.")

def reservevehicle(): 
    
    '''User Interface: [5]  Reserve a particular vehicle.'''
    
    while True: 
        
        # Input vin of vehicle to reserve it. 
        vehicle_reserved = input("Please enter the Vehicle ID Number to reserve: ")
        
        # vin must be a valid vin in the compiled list in order to be reserved. 
        if vehicle_reserved in vin_list:
            
            # Input vin must not be reserved (in the reserved list) so it can be reserved. 
            if vehicle_reserved not in reservationdata['Vehicle ID Number']:
            
                # Input customer details for reservation. 
                print("Please enter your details as follows: ")
                firstname = input("First name: ") 
                lastname = input("Last name: ")
                address = input("Address: ")
                
                while True: 
                    mobileno = input("Mobile number:")
                    
                    # Input validity check for mobile no (8 digits). 
                    if (mobileno.isdigit()) and (len(mobileno) == 8) and (mobileno[0] == 9 or 8):
                
                        while True:
                            credit_card = input("16-digits Credit card number without spaces: ")
                            
                            # Input validity check for credit card number (16 digits)
                            if credit_card.isdigit() and len(credit_card) == 16:
                                
                                if credit_card not in reservationdata['Credit Card']:
                                
                                    print("\nReservation successfully made!\n")
                                       
                                    # Append reservation details into reservationdata.
                                    reservationdata['Vehicle ID Number'].append(vehicle_reserved)
                                    reservationdata['First Name'].append(firstname)
                                    reservationdata['Last Name'].append(lastname)
                                    reservationdata['Address'].append(address)
                                    reservationdata['Credit Card'].append(credit_card)
                                    reservationdata['Mobile Number'].append(mobileno)
                                    
                                    # Update reservation text file. 
                                    with open('./Data/listofreservation.txt', 'w') as outfile:
                                        json.dump(reservationdata, outfile)
                                    
                                    break
                                    
                                else: 
                                     print("Only one unique credit card number for each vehicle reservation. Please enter another credit card number.")   
                                
                            else: 
                                print("Credit card number is invalid. Please try again.")
                        
                        break
                        
                    else:
                        print("Mobile number is invalid. Please try again.")
                    
                break
            
            else:
                print("Vehicle ID Number is already reserved. Please try an available Vehicle ID Number.")
                
        else: 
            print("Invalid Vehicle ID Number. Please try again.")
   
def cancelreservation(): 
    
    '''User Interface: [6]  View / cancel a reservation.'''
    
    while True: 
        
        # Input credit card number. 
        ccnum_reserved = input("Please enter the credit card number used in reservation: ")
            
        # Search for reservation using credit card number in the reservationdata. 
        if ccnum_reserved in reservationdata['Credit Card']:
                
            # Use the credit card no to find the index of the credit card. 
            index_to_remove = reservationdata['Credit Card'].index(ccnum_reserved)
                
            # View reservation details. 
            print("------------------- Reservation Information -------------------\n")
            print("Vehicle ID Number: {}".format(reservationdata['Vehicle ID Number'][index_to_remove]))
            print("Name: {} {}".format(reservationdata['First Name'][index_to_remove], reservationdata['Last Name'][index_to_remove]))
            print("Address: {}".format(reservationdata['Address'][index_to_remove]))
            print("Credit Card: {}".format(reservationdata['Credit Card'][index_to_remove]))
            print("Mobile Number: {}".format(reservationdata['Mobile Number'][index_to_remove]))
                
            # Ask user if he wants to cancel his reservation. 
            while True:
                    
                cancel_reservation = input("\nWould you like to cancel your reservation? (Y/N)")
                    
                if cancel_reservation == "Y":
                    
                    # Delete all the values at the index position where the credit card no above is found. 
                    for k in reservationdata:
                        del(reservationdata[k][index_to_remove])
                        
                    print("Reservation successfully cancelled.")
                        
                    # Update reservation text file.
                    with open('./Data/listofreservation.txt', 'w') as outfile:
                        json.dump(reservationdata, outfile)
                        
                    break
                    
                elif cancel_reservation == "N":
                        
                    print("No changes made to reservation.")
                        
                    break
                    
                # Test for input validity. 
                else: 
                    print("Invalid input entered. Please try again.")
                
            break
                
        else: 
            print("No reservation records found based on the credit card number provided.")
            break 
            # Required to break loop here or else will be stuck in an infinite loop until correct credit card is input.

