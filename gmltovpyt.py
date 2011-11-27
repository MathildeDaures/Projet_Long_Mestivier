#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import re
from visual import *

# Récuperation des données de parsing du fichier gml
filin = open("parsedata.dat")
res = pickle.load(filin)
filin.close() 

# Découpage du fichier
creator = res[0][1]
version = res[1][1]

node = []
edge = []
other = []
for li in res:
    if li[0] == "node":
        node.append(li)
    elif li[0] == "edge":
        edge.append(li)
    else:
        other.append(li)         


# Traitement des nodes
print node[0][1][1][1]    
rule_regex = re.compile("^R+[0-9]")
rules = []
species = []
for li in node:
    if rule_regex.search(li[1][1][1]):
        rules.append(li)
    else:
        species.append(li)     
    
print rules[0]
   
    
#rules = box (pos=(15,3148,1), length=1, height=30, width=30, color=color.blue)
#ball = sphere (pos=(0,4,0), radius=1, color=color.red)
#ball.velocity = vector(0,-1,0)
#dt = 0.01

while 1:
    rules = box (pos=(15,3148,1), length=300, height=300, width=300, color=color.blue)
#    rate (20)
#    ball.pos = ball.pos + ball.velocity*dt
#    if ball.y < ball.radius:
#        ball.velocity.y = abs(ball.velocity.y)
#    else:
#        ball.velocity.y = ball.velocity.y - 9.8*dt    
    
    
    
    
    
    
    
    
    
    
