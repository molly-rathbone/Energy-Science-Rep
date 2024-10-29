#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:36:01 2024

@author: mollyrathbone
"""

#importing functions 
import numpy as np

#defining variable inputs
building_length = 28
building_width = 8
roof_angle = 22
pv_width = 1690
pv_height = 1046
pv_power = 400

#defining formulas 
angled_buildingwidth = (building_width/(np.cos(np.deg2rad(roof_angle))))/2
pv_w = np.floor(angled_buildingwidth/(pv_width/1000))
pv_l = np.floor(building_length/(pv_height/1000))

#calculating number of pv panels
pv_side = (pv_w * pv_l)
pv_total = (pv_side * 2)
print("pv total is", pv_total)

#calculating total power output in kWp
