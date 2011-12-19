#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Module permettant la creation d'objet vphyton et leur stockage dans des
    dico.
"""

import pickle
import re
from visual import box, color, sphere, arrow
#from random import randrange


def recuperation_labels(RULES_LIST_ALL_INFO, SPECIES_LIST_ALL_INFO):
    """ Récupère les labels
        Liste des éléments : LABELS_TO_ID = Name -> id
    """
    LABELS_TO_ID = {}
    
    for rule in RULES_LIST_ALL_INFO:
        LABELS_TO_ID[rule[1][1][1]] = rule[1][0][1]
    for specie in SPECIES_LIST_ALL_INFO:
        LABELS_TO_ID[specie[1][1][1]] = specie[1][0][1]

    return LABELS_TO_ID


def recupération_coordonnées(RULES_LIST_ALL_INFO, SPECIES_LIST_ALL_INFO):
    """ Récupération des coordonnées pour faire les flèches
    """
    NODE_ID_COORD = {}
    
    for rule in RULES_LIST_ALL_INFO:
        coord = {}
        coord['x'] = rule[1][2][1][0][1]
        coord['y'] = rule[1][2][1][1][1]
        #coord['z'] = z    
        NODE_ID_COORD[rule[1][0][1]] = coord
    for specie in SPECIES_LIST_ALL_INFO:
        coord = {}
        coord['x'] = specie[1][2][1][0][1]
        coord['y'] = specie[1][2][1][1][1]
        #coord['z'] = z    
        NODE_ID_COORD[specie[1][0][1]] = coord

    return NODE_ID_COORD

#------------------------------------------------------------------------------#
# NODES
#----------------------

def affichage_rules(RULES_LIST_ALL_INFO):
    """ Création des éléments pour les régles
        Liste des rules : BOXES = id -> objet.visual.box
    """    
    BOXES = {}
    
    for rule in RULES_LIST_ALL_INFO:
        #z = randrange(0, 500)
        #rules = box(pos = (rule[1][2][1][0][1], rule[1][2][1][1][1], z) , \
        #            length=30, height=30, width=30, color=color.blue)
        rules = box(pos = (rule[1][2][1][0][1], rule[1][2][1][1][1]) , \
                    length=30, height=30, width=30, color=color.blue)    
        BOXES[rule[1][0][1]] = rules

    return BOXES    


def affichage_species(SPECIES_LIST_ALL_INFO):
    """ Création des éléments pour les espèces
        Liste des species : SPHERES = id -> objet.visual.sphere
    """
    SPHERES = {}    

    for specie in SPECIES_LIST_ALL_INFO:
        #z = randrange(0, 500)    
        #species = sphere(pos = (specie[1][2][1][0][1], specie[1][2][1][1][1], z), \
        #        radius=20, color=color.green) 
        species = sphere(pos = (specie[1][2][1][0][1], specie[1][2][1][1][1]), \
                radius=20, color=color.green)    
        SPHERES[specie[1][0][1]] = species

    return SPHERES
        
#------------------------------------------------------------------------------#
# EDGES
#----------------------

def affichage_arrows(EDGE_LIST_ALL_INFO):
    """ Création des éléments pour les liens entre règles et espèces
        Liste des liens : POINTERS_ID = numéro -> source_id, target_id
        Liste des arrows : POINTERS = numéro -> objet.visual.arrows
    """   

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

    return POINTERS_ID, POINTERS







