# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:39:34 2018

@author: ZJ
"""

import matplotlib.pyplot as plt


from random_walk import RandomWalk

while True:

    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.flag, edgecolor='none', s=10)
    plt.show()
    
    keep_running = input("Make another walk? (yes/no) ")
    if keep_running == 'no':
        break