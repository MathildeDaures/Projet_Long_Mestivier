#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import re
from visual import *
import csv
import time

#autocenter()

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
rule_regex = re.compile("^R+[0-9]")
rules = []
species = []
for li in node:
    if rule_regex.search(li[1][1][1]):
        rules.append(li)
    else:
        species.append(li)     
    
#print rules[0]
#print rules[0][1][2][1][0][1]

# Affichage des nodes 
node_id = {}
labels = {}
for li in rules:
    coord = {}
    #rule = box(pos=(li[1][2][1][0][1],li[1][2][1][1][1]), length=30, height=30, width=30, color=color.blue)
    coord['x'] = li[1][2][1][0][1]
    coord['y'] = li[1][2][1][1][1]
    node_id[li[1][0][1]] = coord
    labels[li[1][1][1]] = li[1][0][1]
for li in species:
    coord = {}
    #rule = sphere(pos=(li[1][2][1][0][1],li[1][2][1][1][1]), radius=20, color=color.green) 
    coord['x'] = li[1][2][1][0][1]
    coord['y'] = li[1][2][1][1][1]
    node_id[li[1][0][1]] = coord
    labels[li[1][1][1]] = li[1][0][1]



# Traitement et affichage des edges
for li in edge:
    #print li[1][1][1]    
    source = li[1][0][1] 
    target = li[1][1][1]
    #print node_id[source]['x']
    x_source = node_id[source]['x']
    y_source = node_id[source]['y']
    x_target = node_id[target]['x']
    y_target = node_id[target]['y']
    #pointer = arrow(pos=(x_source, y_source, 0), axis=(x_target - x_source, y_target - y_source, 0), shaftwidth=10)

# Récupération des valeurs de simulation pour les species
POE = csv.reader(open("./Visu/Simulations/res_mutation_nwin_100_winsize_500000_nsim_500_Ri_96.poe","rb"), delimiter='\t', quotechar='.')
species_list = csv.reader(open("./Visu/Modele/model_14_03_2010_listOfSpecies.csv", "rb"))

species = []
for specie in species_list:
    species.append(specie)

#print species

POE_value = {}
cpt = 1
for row in POE:
    POE_ok = {}
    column = 0
    for specie in species:     
        POE_ok[specie[0]] = row[column]
        column = column + 1
    POE_value[cpt] = POE_ok
    cpt = cpt + 1

#print POE_value
    
# Modification par temps de simulation --  POE

#nb_simul = len(POE_value.keys())
#print nb_simul

#incr = 1
#tps = time.clock()
#while incr <= nb_simul-1:
#    print incr
#    print tps
#    for specie in POE_value[incr]:
#        value = POE_value[incr][specie]
        #print value  
#        if specie != 'nOfEvents' and specie != 'time' and specie != 'NONE':
#            id_tochange = labels[specie]
#            if float(value) < 10:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(0, 100, 0))      #Dark green
#            elif float(value) >= 10 and float(value) < 20:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(34, 139, 34))    #Forest green              
#            elif float(value) >= 20 and float(value) < 30:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(50, 205, 50))    #Lime green
#            elif float(value) >= 30 and float(value) < 40:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(173, 255, 47))   #Green Yellow
#            elif float(value) >= 40 and float(value) < 50:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(255, 255, 0))    #Yellow            
#            elif float(value) >= 50 and float(value) < 60:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(255, 165, 47))   #Orange
#            elif float(value) >= 60 and float(value) < 70:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(255, 69, 0))     #Orange Red
#            elif float(value) >= 70 and float(value) < 80:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(255, 0, 0))      #Red
#            elif float(value) >= 80 and float(value) < 90:
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(205, 0, 0))      #Red 3
#            elif float(value) >= 90:  
#                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(139, 0, 0))      #Red 4
        
#        newtime = time.clock()        
#        if newtime >= tps + 2:
#            print "in time!"
#            incr = incr + 1
#            tps = newtime      

# Récupération des valeurs de simulation pour les rules
POR = csv.reader(open("./Visu/Simulations/res_mutation_nwin_100_winsize_500000_nsim_500_Ri_96.por","rb"), delimiter='\t', quotechar='.')
rules_list = csv.reader(open("./Visu/Modele/model_14_03_2010_listOfRules_modified.csv", "rb"))

rule_list = []
for ru in rules_list:
    rule_list.append(ru)

#print rule_list

POR_value = {}
cpt = 1
for row in POR:
    POR_ok = {}
    column = 0
    for ru in rule_list:     
        POR_ok[ru[0]] = row[column]
        column = column + 1
    POR_value[cpt] = POR_ok
    cpt = cpt + 1

#print POR_value

# Modification par temps de simulation --  POR
nb_simul = len(POE_value.keys())
print nb_simul

incr = 1
tps = time.clock()
while incr <= nb_simul-1:
    print incr
    print tps
    for rule in POR_value[incr]:
        value = POR_value[incr][rule]
        #print value  
        if rule != 'nOfEvents' and rule != 'time' and rule != 'NONE':
            id_tochange = labels[rule]
            if float(value) < 0.0001:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.1)     
            elif float(value) >= 0.0001 and float(value) < 0.0005:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.2)               
            elif float(value) >= 0.0005 and float(value) < 0.001:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.3)  
            elif float(value) >= 0.001 and float(value) < 0.005:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.4)  
            elif float(value) >= 0.005 and float(value) < 0.01:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.5)             
            elif float(value) >= 0.01 and float(value) < 0.05:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.6)  
            elif float(value) >= 0.05 and float(value) < 0.1:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.7)  
            elif float(value) >= 0.1 and float(value) < 0.5:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.8)  
            elif float(value) >= 0.5 and float(value) < 1:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=0.9)   
            else:  
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.blue, opacity=1)   
        
        newtime = time.clock()
        print newtime        
        if newtime >= tps + 2:
            print "in time!"
            incr = incr + 1
            tps = newtime      













