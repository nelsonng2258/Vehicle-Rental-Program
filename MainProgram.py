#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:00:15 2022

@author: nelsonng
""" 

import my_UserInterface as ui
import time 

#-----------------------------------------------------------------------------

def prog():  
    
    '''Main program.'''
    
    # User Interface: Main Menu. 
    ui.menu()  
    bool_flag = True
    
    while bool_flag:
        
        option = input("Enter Option: ")
        # Didn't convert to int for the option input as wanted to simplify input validity later on.
        # Only required to check for exact match, if failed, then will have to reinput via while loop (no need to test for isdigit())
        
        # User Interface: [1] Display vehicle types. 
        if option == "1": 
            print("Option 1 is selected.\n")
            ui.vehtype()
        
        # User Interface: [2] Check rental costs. 
        elif option == "2":
            print("Option 2 is selected.\n") 
            bool_flag = False # Stop loop for main menu option. 
            ui.vehrentalcost()
            
            returnmainmenu = input("Enter [R] to return to main menu.\nOtherwise, enter any key to exit program.\n")
            
            if returnmainmenu == "R": 
                bool_flag = True # Restart loop for main menu option. 
                print("Returning back to the main menu ......\n")
                
                # Time delay of 1 second then return to main menu. 
                time.sleep(1)
                ui.menu() 
                
            else:
                print("Thank you for using the Friendly Rental Agency. See you soon!")
        
        # User Interface: [3] Check available vehicles. 
        elif option == "3":  
            print("Option 3 is selected.\n")
            bool_flag = False # Stop loop for main menu option.  
            ui.checkavailvehicle()
            
            returnmainmenu = input("Enter [R] to return to main menu.\nOtherwise, enter any key to exit program.\n")
            
            if returnmainmenu == "R": 
                bool_flag = True # Restart loop for main menu option. 
                print("Returning back to the main menu ......\n")
                
                # Time delay of 1 second then return to main menu. 
                time.sleep(1)
                ui.menu()
                
            else:
                print("Thank you for using the Friendly Rental Agency. See you soon!")
        
        # User Interface: [4] Get cost of specific rental. 
        elif option == "4":  
            print("Option 4 is selected.\n")
            bool_flag = False # Stop loop for main menu option. 
            ui.calculaterentalcost()
            
            returnmainmenu = input("Enter [R] to return to main menu.\nOtherwise, enter any key to exit program.\n")
            
            if returnmainmenu == "R":
                bool_flag = True # Restart loop for main menu option. 
                print("Returning back to the main menu ......\n")
                #Time delay of 1 second then return to main menu 
                time.sleep(1)
                ui.menu()
                
            else:
                print("Thank you for using the Friendly Rental Agency. See you soon!")
        
        # User Interface: [5] Make a reservation. 
        elif option == "5": 
            print("Option 5 is selected.\n")
            bool_flag = False # Stop loop for main menu option. 
            ui.checkavailvehicle() 
            ui.reservevehicle()
            
            returnmainmenu = input("Enter [R] to return to main menu.\nOtherwise, enter any key to exit program.\n")
            
            if returnmainmenu == "R":
                bool_flag = True # Restart loop for main menu option. 
                print("Returning back to the main menu ......\n")
                # Time delay of 1 second then return to main menu. 
                time.sleep(1)
                ui.menu()
                
            else:
                print("Thank you for using the Friendly Rental Agency. See you soon!")
        
        # User Interface: [6] View / Cancel a reservation. 
        elif option == "6": 
            #do option 6 stuffs
            print("Option 6 is selected.\n")
            bool_flag = False # Stop loop for main menu option. 
            ui.cancelreservation()
            
            returnmainmenu = input("Enter [R] to return to main menu.\nOtherwise, enter any key to exit program.\n")
            
            if returnmainmenu == "R": 
                bool_flag = True # Restart loop for main menu option. 
                print("Returning back to the main menu ......\n")
                
                # Time delay of 1 second then return to main menu. 
                time.sleep(1)
                ui.menu()  
                
            else:
                print("Thank you for using the Friendly Rental Agency. See you soon!")
        
        # User Interface: [7] Quit. 
        elif option == "7":
            print("Thank you for using the Friendly Rental Agency. See you soon!")
            bool_flag = False # Stop loop for main menu option. 
            
        else: 
            print("Invalid option. Please try again.\n")

#-----------------------------------------------------------------------------
            
prog()