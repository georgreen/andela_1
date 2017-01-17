#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:06:15 2017

@author: manu
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Car(): 
  def __init__(self, name = 'General', model = 'GM',Type = ''):
    self.name = name
    self.model = model 
    self.speed = 0
    self.Type = Type
    self.num_of_doors = 4
    self.set_door(name)
      
    self.num_of_wheels = 4
    self.set_wheels(Type)
    
    return 
    
  def set_door(self, name):
    if name == 'Porshe' or name == 'Koenigsegg':
      self.num_of_doors = 2
      
  def set_wheels(self, Type):
    if Type == 'trailer':
        self.num_of_wheels = 8
      
      
  def drive(self,speed):
    car = Car(self.name, self.model, self.Type)
    if speed == 7:
      car.speed = 77
      self.speed = 77
    elif speed == 3:
      car.speed = 1000
      self.speed = 100
    return car
    
  def set_speed(self, n):
    self.speed = n
    
    
  def is_saloon(self):
    if self.Type== 'trailer':
      return False
    return True
  
