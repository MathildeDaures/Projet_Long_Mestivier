#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

#def read_color(colors_txt):
  
def poe_value_modif(poe_values, labels, spheres, no_simulation):    
    """ Prend les valeurs de POE par espece pour un temps de simulation donné
        Modifie le graph en modifiant la couleur de l'objet
         0 -  10    Dark_green
        10 -  20    Forest_green
        20 -  30    Lime_green
        30 -  40    Green_Yellow
        40 -  50    Yellow
        50 -  60    Orange
        60 -  70    Orange_Red
        70 -  80    Red
        80 -  90    Red_3
        90 - 100    Red_4
    """
    for specie in poe_values[no_simulation]:
        if specie != 'nOfEvents' and specie != 'time' and specie != 'NONE':
            id_specie = labels[specie]
            sphere_to_change = spheres[id_specie]
            value = float(poe_values[no_simulation][specie])    
        
            if value < 10:
                sphere_to_change.color = (0, 0.392, 0)
            elif value >= 10 and value < 20: 
                sphere_to_change.color = (0.133, 0.545, 0.133)
            elif value >= 20 and value < 30:
                sphere_to_change.color = (0.196, 0.804, 0.196)    
            elif value >= 30 and value < 40:
                sphere_to_change.color = (0.678, 1, 0.184)
            elif value >= 40 and value < 50:
                sphere_to_change.color = (1, 1, 0)
            elif value >= 50 and value < 60:
                sphere_to_change.color = (1, 0.647, 0)
            elif value >= 60 and value < 70:
                sphere_to_change.color = (1, 0.271, 0)
            elif value >= 70 and value < 80:
                sphere_to_change.color = (1, 0, 0)
            elif value >= 80 and value < 90:
                sphere_to_change.color = (0.804, 0, 0)
            elif value >= 90:            
                sphere_to_change.color = (0.545, 0, 0)  


def por_value_modif(por_values, labels, boxes, no_simulation):    
    """ Prend les valeurs de POE par espece pour un temps de simulation donné
        Modifie le graph en modifiant la couleur de l'objet
               -  0.0001    Pale_turquoise
        0.0001 -  0.0005    Powder_blue
        0.0005 -  0.001     Ligh_blue
        0.001  -  0.005     Ligh_sky_blue
        0.005  -  0.01      Deep_sky_blue
        0.01   -  0.05      Dodger_blue
        0.05   -  0.1       Royal_blue
        0.1    -  0.5       Slate_blue
        0.5    -  1         Darl_slate_blue
        1      -            Navy
    """
    for rule in por_values[no_simulation]:
        id_rule = labels[rule]
        box_to_change = boxes[id_rule]
        value = float(por_values[no_simulation][rule])    
        
        if value < 0.0001:
            box_to_change.color = (0.686, 0.933, 0.933)
        elif value >= 0.0001 and value < 0.0005: 
            box_to_change.color = (0.69, 0.878, 0.902)
        elif value >= 0.0005 and value < 0.001:
            box_to_change.color = (0.678, 0.847, 0.902) 
        elif value >= 0.001 and value < 0.005:
            box_to_change.color = (0.529, 0.808, 0.98)
        elif value >= 0.005 and value < 0.01:
            box_to_change.color = (0, 0.749, 0.922)
        elif value >= 0.01 and value < 0.05:
            box_to_change.color = (0.117, 0.0565, 0.922)
        elif value >= 0.05 and value < 0.1:
            box_to_change.color = (0.255, 0.0412, 0.922)
        elif value >= 0.1 and value < 0.5:
            box_to_change.color = (0.416, 0.353, 0.804)
        elif value >= 0.5 and value < 1:
            box_to_change.color = (0.282, 0.239, 0.545)
        elif value >= 1:            
            box_to_change.color = (0, 0, 0.502)           



