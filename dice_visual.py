# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:51:34 2018

@author: ZJ
"""
import pygal
from die import Die

die1 = Die()
die2 = Die(sides=10)

results = []
for roll_num in range(1000):
    result = die1.roll_die() + die2.roll_die()
    results.append(result)

frequencies = []
max_result = die1.sides + die2.sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6  + D10',frequencies)
hist.render_to_file('dice_visual.svg')