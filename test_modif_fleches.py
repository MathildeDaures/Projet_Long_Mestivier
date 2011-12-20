#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import re
from visual import display, label
#from random import randrange
import mod_create_graph as mcg
import csv
import mod_read_simul as mrs
import mod_modif_graph as mmg
import time

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
# Paramètres du graph
#------------------------
SCENE = display(title='Simulation', center=(1871.7626953125, 1621.0, 0), \
                userspin = False, background=(1, 1, 1))
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Création du graph
#------------------------

# Traitement des nodes
RULE_REGEX = re.compile("^R+[0-9]")
RULES_LIST_ALL_INFO = []
SPECIES_LIST_ALL_INFO = []
for node in NODE_LIST_ALL_INFO:
    if RULE_REGEX.search(node[1][1][1]):
        RULES_LIST_ALL_INFO.append(node)
    else:
        SPECIES_LIST_ALL_INFO.append(node)   

#---Récupération des labels-id
#   Liste des éléments : LABELS_TO_ID = Name -> id
LABELS_TO_ID = mcg.labels(RULES_LIST_ALL_INFO, SPECIES_LIST_ALL_INFO)[0]
REVERSE_LABELS = mcg.labels(RULES_LIST_ALL_INFO, SPECIES_LIST_ALL_INFO)[1]

#---Création des règles
#   Liste des rules : BOXES = id -> objet.visual.box
BOXES = mcg.affichage_rules(RULES_LIST_ALL_INFO)


#---Création des especes
#   Liste des species : SPHERES = id -> objet.visual.sphere
SPHERES = mcg.affichage_species(SPECIES_LIST_ALL_INFO)


# Traitement des edges
#---Récupération des positions de début et fin
NODE_ID_COORD = mcg.coordonnes(RULES_LIST_ALL_INFO, SPECIES_LIST_ALL_INFO)

#---Création des flèches
#   Liste des liens : POINTERS_ID = numéro -> source_id, target_id
#   Liste des arrows : POINTERS = numéro -> objet.visual.arrows
POINTERS = mcg.affichage_arrows(EDGE_LIST_ALL_INFO, NODE_ID_COORD)[1]
POINTERS_ID = mcg.affichage_arrows(EDGE_LIST_ALL_INFO, NODE_ID_COORD)[0]
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Lecture des simulation
#------------------------

# Lecture des POE
#---Import des données
POE = csv.reader(open\
 ("./Visu/Simulations/res_mutation_nwin_100_winsize_500000_nsim_500_Ri_96.poe",\
 "rb"), delimiter='\t', quotechar='.')
SPECIES_LIST_NAMES = csv.reader(open\
    ("./Visu/Modele/model_14_03_2010_listOfSpecies.csv", "rb"))

#---Traitement des données
POE_VALUE = mrs.poe_treatment(POE, SPECIES_LIST_NAMES)

# Lecture des POR
#---Import des données
POR = csv.reader(open\
 ("./Visu/Simulations/res_mutation_nwin_100_winsize_500000_nsim_500_Ri_96.por",\
 "rb"), delimiter='\t', quotechar='.')
RULES_LIST_NAMES = csv.reader(open\
    ("./Visu/Modele/model_14_03_2010_listOfRules_modified.csv", "rb"))

#---Traitement des données
POR_VALUE = mrs.por_treatment(POR, RULES_LIST_NAMES)










por_values = POR_VALUE
labels = LABELS_TO_ID
boxes = BOXES
no_simulation = 1
pointers = POINTERS
pointers_id = POINTERS_ID    
reverse_labels = REVERSE_LABELS

#print len(por_values[no_simulation])
#print len(pointers_id.keys())
#print por_values[no_simulation]['R499']
for rule in por_values[no_simulation].keys():
    #print rule
    id_rule = labels[rule]
    box_to_change = boxes[id_rule]
    value = float(por_values[no_simulation][rule])    
      

    arrows_to_change = []
    arrow = 1    
    while arrow <= len(pointers_id.keys()):
        if reverse_labels[pointers_id[arrow]['source']] == rule \
            or reverse_labels[pointers_id[arrow]['target']] == rule:
            arrows_to_change.append(pointers[arrow])    
        #    print '='        
        arrow = arrow + 1
    
    #print arrows_to_change
    if value < 0.0001:
        box_to_change.color = (1,0,0)#(0.686, 0.933, 0.933)
        for arrow in arrows_to_change:
            print arrow
            arrow.color = (1,0,0)#(0.686, 0.933, 0.933)
    elif value >= 0.0001 and value < 0.0005: 
        box_to_change.color = (0.69, 0.878, 0.902)
        for arrow in arrows_to_change:
            arrow.color = (0.69, 0.878, 0.902)
    elif value >= 0.0005 and value < 0.001:
        box_to_change.color = (0.678, 0.847, 0.902) 
        for arrow in arrows_to_change:
            arrow.color = (0.678, 0.847, 0.902) 
    elif value >= 0.001 and value < 0.005:
        box_to_change.color = (0.529, 0.808, 0.98)
        for arrow in arrows_to_change:
            arrow.color = (0.529, 0.808, 0.98)
    elif value >= 0.005 and value < 0.01:
        box_to_change.color = (0, 0.749, 0.922)
        for arrow in arrows_to_change:
            arrow.color = (0, 0.749, 0.922)
    elif value >= 0.01 and value < 0.05:
        box_to_change.color = (0.117, 0.0565, 0.922)
        for arrow in arrows_to_change:
            arrow.color = (0.117, 0.0565, 0.922)
    elif value >= 0.05 and value < 0.1:
        box_to_change.color = (0.255, 0.0412, 0.922)
        for arrow in arrows_to_change:
            arrow.color = (0.255, 0.0412, 0.922)
    elif value >= 0.1 and value < 0.5:
        box_to_change.color = (0.416, 0.353, 0.804)
        for arrow in arrows_to_change:
            arrow.color = (0.416, 0.353, 0.804)
    elif value >= 0.5 and value < 1:
        box_to_change.color = (0.282, 0.239, 0.545)
        for arrow in arrows_to_change:
            arrow.color = (0.282, 0.239, 0.545)
    elif value >= 1:            
        box_to_change.color = (0, 0, 0.502)           
        for arrow in arrows_to_change:
            arrow.color = (0, 0, 0.502) 
    
        
