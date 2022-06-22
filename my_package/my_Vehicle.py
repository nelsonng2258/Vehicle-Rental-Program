#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:30:32 2022

@author: nelsonng
"""

class Vehicle:
    
    '''Vehicle class.''' 
    
    def __init__(self, mpg, vin): 
        self.mpg = mpg
        self.vin = vin 
        
    def get_vin(self):
        
        '''Return vehicle's id number.'''
        
        return self.vin

    def get_type(self): 
        
        '''Returns vehicle type.''' 
        
        if isinstance(self, Car): 
            return "Car"
        if isinstance(self, Van):
            return "Van" 
        if isinstance(self, Truck): 
            return "Truck"
    
    def get_description(self):
        
        '''Return text format of vehicle's mpg and id number.'''
        
        return F"mpg: {self.mpg} and vin: {self.vin}" 

class Car(Vehicle):
    
    '''Car class is a child of vehicle class.'''  
    
    def __init__(self, make_model, mpg, numPassengers, numDoors, vin):
        
        # Inherit mpg and vin from parent class.
        super().__init__(mpg, vin)
        
        # Unique attributes related to child class. 
        self.make_model = make_model
        self.numPassengers = numPassengers 
        self.numDoors = numDoors

    def get_description(self): 
        
        '''Return text format of car's make model, passenger limit, number of doors, mpg and id number.'''
        
        return F"{self.make_model}  passengers: {self.numPassengers}  doors: {self.numDoors}  mpg: {self.mpg}  vin: {self.vin}"     

class Van(Vehicle):
    
    '''Van class.'''  
    
    def __init__(self,make_model,mpg,numPassengers,vin): 
        
        # Inherit mpg and vin from parent class.
        super().__init__(mpg, vin)
        
        # Unique attributes related to child class. 
        self.make_model = make_model
        self.numPassengers = numPassengers 

    def get_description(self): 
        
        '''Return text format of van's make model, passenger limit, mpg and id number.'''
        
        return F"{self.make_model}  passengers: {self.numPassengers}  mpg: {self.mpg}  vin: {self.vin}"     

class Truck(Vehicle):
    
    '''Truck class.''' 
    
    def __init__(self,mpg,length,num_rooms,vin):
        
        # Inherit mpg and vin from parent class. 
        super().__init__(mpg, vin)
        
        # Unique attributes related to child class. 
        self.length = length
        self.num_rooms = num_rooms

    def get_description(self):
        
        '''Return text format of truck's length, cargo space, mpg and id number.'''
    
        return F"{self.length}  Cargo space: {self.num_rooms}  mpg: {self.mpg}  vin: {self.vin}"      


