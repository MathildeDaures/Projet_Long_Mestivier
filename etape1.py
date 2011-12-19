#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import re
from visual import box, color, sphere, arrow
#from random import randrange

# Récuperation des données de parsing du fichier gml
FILIN = open("parsedata.dat")
GML_CONTENT = pickle.load(FILIN)
FILIN.close() 

#------------------------------------------------------------------------------#
# Lecture de GML_CONTENT
#------------------------

# Découpage du fichier
CREATOT = GML_CONTENT[0][1]
VERSION = GML_CONTENT[1][1]

NODE_LIST_ALL_INFO = []
EDGE_LIST_ALL_INFO = []

for element in GML_CONTENT:
    if element[0] == "node":
        NODE_LIST_ALL_INFO.append(element)
    elif element[0] == "edge":
        EDGE_LIST_ALL_INFO.append(element)
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# NODES
#----------------------

# Traitement des nodes
RULE_REGEX = re.compile("^R+[0-9]")
RULES_LIST_ALL_INFO = []
SPECIES_LIST_ALL_INFO = []
for node in NODE_LIST_ALL_INFO:
    if RULE_REGEX.search(node[1][1][1]):
        RULES_LIST_ALL_INFO.append(node)
    else:
        SPECIES_LIST_ALL_INFO.append(node)   

# Affichage des nodes 
LABELS_TO_ID = {}
NODE_ID_COORD = {}

#--Affichage des rules (rectangle)
BOXES = {}
for rule in RULES_LIST_ALL_INFO:
    #z = randrange(0, 500)
    #rules = box(pos = (rule[1][2][1][0][1], rule[1][2][1][1][1], z) , \
    #            length=30, height=30, width=30, color=color.blue)
    rules = box(pos = (rule[1][2][1][0][1], rule[1][2][1][1][1]) , \
                length=30, height=30, width=30, color=color.blue)    
    BOXES[rule[1][0][1]] = rules    
    LABELS_TO_ID[rule[1][1][1]] = rule[1][0][1]
    coord = {}
    coord['x'] = rule[1][2][1][0][1]
    coord['y'] = rule[1][2][1][1][1]
    #coord['z'] = z    
    NODE_ID_COORD[rule[1][0][1]] = coord

#--Affichage des species (sphere)
SPHERES = {}    
for specie in SPECIES_LIST_ALL_INFO:
    #z = randrange(0, 500)    
    #species = sphere(pos = (specie[1][2][1][0][1], specie[1][2][1][1][1], z), \
    #        radius=20, color=color.green) 
    species = sphere(pos = (specie[1][2][1][0][1], specie[1][2][1][1][1]), \
            radius=20, color=color.green)    
    SPHERES[specie[1][0][1]] = species
    LABELS_TO_ID[specie[1][1][1]] = specie[1][0][1]
    coord = {}
    coord['x'] = specie[1][2][1][0][1]
    coord['y'] = specie[1][2][1][1][1]
    #coord['z'] = z    
    NODE_ID_COORD[specie[1][0][1]] = coord
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# EDGES
#----------------------
   
# Traitement et affichage des edges
POINTERS = {}
POINTERS_ID = {}
CPT = 0
for edge in EDGE_LIST_ALL_INFO:
    CPT = CPT + 1    
    coord = {}    
    source = edge[1][0][1] 
    target = edge[1][1][1]
    coord['source'] = source
    coord['target'] = target
    #pointer = arrow(\
   #          pos = (NODE_ID_COORD[source]['x'], \
   #                 NODE_ID_COORD[source]['y'], \
   #                 NODE_ID_COORD[source]['z']), \
   #          axis = (NODE_ID_COORD[target]['x'] - NODE_ID_COORD[source]['x'], \
   #                  NODE_ID_COORD[target]['y'] - NODE_ID_COORD[source]['y'], \
   #                  NODE_ID_COORD[target]['z'] - NODE_ID_COORD[source]['z']),\
   #          shaftwidth = 5, color = (0.5, 0.5, 0.5))
    pointer = arrow(\
              pos = (NODE_ID_COORD[source]['x'], \
                     NODE_ID_COORD[source]['y']), \
             axis = (NODE_ID_COORD[target]['x'] - NODE_ID_COORD[source]['x'], \
                     NODE_ID_COORD[target]['y'] - NODE_ID_COORD[source]['y']), \
              shaftwidth = 5, color = (0.5, 0.5, 0.5))
    POINTERS_ID[CPT] = coord
    POINTERS[CPT] = pointer 

#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# SUM-UP DATA
#----------------------

# Liste des éléments : LABELS_TO_ID = Name -> id
# Liste des rules : BOXES = id -> objet.visual.box
# Liste des species : SPHERES = id -> objet.visual.sphere
# Liste des liens : POINTERS_ID = numéro -> source_id, target_id
# Liste des arrows : POINTERS = numéro -> objet.visual.arrows













