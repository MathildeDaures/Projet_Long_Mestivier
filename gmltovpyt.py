#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import re
from visual import *
import csv
import time

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
    
# Modification par temps de simulation

nb_simul = len(POE_value.keys())
print nb_simul

incr = 1
tps = time.clock()
while incr <= nb_simul:
    print incr
    print tps
    for specie in POE_value[incr]:
        value = POE_value[incr][specie]
        #print value  
        if specie != 'nOfEvents' and specie != 'time' and specie != 'NONE':
            id_tochange = labels[specie]
            if float(value) <= 20:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(255, 255, 0))
            elif float(value) > 80:  
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=(255, 0, 0))
            else:
                rule = sphere(pos=(node_id[id_tochange]['x'], node_id[id_tochange]['y']), radius=15, color=color.green)
        newtime = time.clock()        
        if newtime >= tps + 2:
            print "in time!"
            incr = incr + 1
            tps = newtime      














