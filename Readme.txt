Vehicle Rental Program - Readme

1.	About The Project
The program was developed to serve the interests of a vehicle rental agency which rents out three different types of vehicles – cars, vans and trucks. The program allows the users to (1) check the different vehicles available for rent, (2) display and get cost estimates on specific vehicle rentals and (3) manage their vehicle reservations. The program also provides the vehicle rental agency a list of real-time reservation summary.


2.	Getting Started
Installation
- main: 1. MainProgram.py, 2.my_UserInterface, 
- Data folder: 1. vehicle_car_data.txt, 2. vehicle_van_data.txt, 3. vehicle_truck_data.txt, 4. vehicle_cost.txt and 5. listofreservation.txt 
- my_package folder: 1. __init__.py, 2. my_Vehicle.py, 3. my_VehicleCost.py
- program executed via MainProgram.py
- reservation summary data stored in listofreservation.txt


3.	Software Usage
Upon program run, user will be presented with a main menu with 7 different options: 
1. Display vehicle types 
2. Check rental costs
3. Check available vehicles
4. Get cost of specific rental 
5. Make a reservation
6. View / Cancel a reservation
7. Quit

[1] Display vehicle types
- Users would be able to view the 3 different types of vehicles (i.e. car, van, truck) available for rent and the recommended usage for each vehicle type. 
- User would be automatically brought back to the main menu screen upon the display of the different vehicle types

[2] Check rental costs
- Users can find out the rental related rates (i.e. daily rate, weekly rate, per mile charges and daily insurance) for each vehicle type

[3] Check available vehicles
- Users can view the available vehicles and its specifications for each vehicle type available for rent
- Only vehicles available for rent are displayed, vehicles that are reserved will not be displayed in this menu

[4] Get cost of specific rental
- Based on the users’ input on the vehicle type, rental period, driving miles and insurance, the program will calculate the estimated rental charges based on the rental rates reflected in [2] check rental costs

[5] Make a reservation
- Users can make a reservation on any of the available vehicles displayed on the screen 
- The program will guide the user on the necessary information (i.e. vehicle ID number, name, address, mobile, credit card number) required for the reservation 

[6] View / cancel a reservation
- Users are able to view their existing reservation via the input of the credit card number used in the reservation
- After which, users have the option to cancel their reservation 

[7] Quit
- Allows users to exit the program


4.	Software Design
[1] Object oriented design and implementation 
- Classes: (1) vehicle and (2) vehicle cost 
- Inheritance: vehicle and vehicle types (i.e. car, van, truck)
- Unified Modeling Language (UML): Kindly refer to UML class diagram.pdf

[2] Data structures 
- Vehicle reservation data: implementation of dictionary data types (key-value pairs) for reservation data and list data types for reservation data values

[3] Modularisation and composition
- Modular code design using functions and classes
- Functions: subfunctions implemented for the 7 different options in the main menu as part of the main program function definition
- Classes: (1) Vehicle and (2) VehiclCost

[4] File I/O
- read / write using JSON package 
- JSON data used due to (1) key-value pairs format preferred, (2) language independent and (3) human readable data 

Vehicle (Car, Van, Truck) data and Vehicle cost data
- Vehicle and vehicle cost data are stored in separate text files and will be read when program executed

Vehicle reservation data
- Vehicle reservation data is stored in a separate listofreservation.txt file
- Allows retrieval of reservation data each time the program is run as data within text file will be read when program executed


5.	Contributions 
Developer: Nelson Ng
