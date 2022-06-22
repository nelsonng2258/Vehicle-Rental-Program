#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:34:48 2022

@author: nelsonng
"""

class VehicleCost: 
    
    '''VehicleCost class.''' 

    def __init__(self, vehicle_type, daily_rate, weekly_rate, per_mile_chrg, insur_rate):
        self.vehicle_type = vehicle_type
        self.daily_rate = daily_rate
        self.weekly_rate = weekly_rate
        self.per_mile_chrg = per_mile_chrg
        self.insur_rate = insur_rate
    
    def get_vehicle_type(self):  
        
        '''Return vehicle type.'''
        
        return self.vehicle_type
    
    def get_daily_rate(self):
        
        '''Return vehicle's daily rental rate.'''
        
        return self.daily_rate
        
    def get_weekly_rate(self):
        
        '''Return vehicle's weekly rental rate.'''
        
        return self.weekly_rate
    
    def get_per_mile_chrg(self):
        
        '''Return vehicle's mileage cost.'''
        
        return self.per_mile_chrg
    
    def get_insur_rate(self):
        
        '''Return vehicle's insurance rate.'''
        
        return self.insur_rate 
    
    def calcrentalcost(self, vehicle_type, rental_period, want_insurance, miles_driving):
        
        '''Calculation of rental cost based on a given vehicle type, rental period, opt for insurance and miles.'''
        
        # Calculation of base rate. 
        rental_weeks = rental_period // 7
        remaining_days = rental_period % 7  
        
        # If rental period is less than 7 days -> daily rate applies. 
        if rental_weeks == 0: 
            base_rate = rental_period * self.daily_rate
        
        # If rental period is more than 7 days -> weekly rate + daily rate applies (e.g. 9 days -> 1 week + 2 day). 
        elif rental_weeks >= 0:
            base_rate = (rental_weeks * self.weekly_rate) + (remaining_days * self.daily_rate)
        
        # Calculation of mileage rate.  
        miles_rate = self.per_mile_chrg * miles_driving
        
        # Calculation of insurance cost. 
        insurance_cost = want_insurance * self.insur_rate * rental_period # want_insurance = 1 (true) or 0 (false)
        
        # Calculation of total rental cost. 
        totalrentalcost = base_rate + miles_rate + insurance_cost
        
        return round(totalrentalcost,2) 