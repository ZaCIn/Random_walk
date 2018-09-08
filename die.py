# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:45:23 2018

@author: ZJ
"""

from random import randint

class Die():
    '''创建一个6面的骰子'''
    
    def __init__(self, sides=6):
        self.sides = sides
       
        
    def roll_die(self):
        return randint(1,self.sides)
    
    