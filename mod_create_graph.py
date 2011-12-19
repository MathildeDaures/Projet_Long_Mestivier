#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Module permettant la creation d'objet vphyton et leur stockage dans des
    dico.
"""

from visual import box, color, sphere, arrow
#from random import randrange


def labels(rules, species):
    """ Récupère les labels
        Liste des éléments : LABELS_TO_ID = Name -> id
    """
    labels_to_id = {}
    
    for rule in rules:
        labels_to_id[rule[1][1][1]] = rule[1][0][1]
    for specie in species:
        labels_to_id[specie[1][1][1]] = specie[1][0][1]

    return labels_to_id


def coordonnes(rules, species):
    """ Récupération des coordonnées pour faire les flèches
    """
    node_id_coord = {}
    
    for rule in rules:
        coord = {}
        coord['x'] = rule[1][2][1][0][1]
        coord['y'] = rule[1][2][1][1][1]
        #coord['z'] = z    
        node_id_coord[rule[1][0][1]] = coord
    for specie in species:
        coord = {}
        coord['x'] = specie[1][2][1][0][1]
        coord['y'] = specie[1][2][1][1][1]
        #coord['z'] = z    
        node_id_coord[specie[1][0][1]] = coord

    return node_id_coord

#------------------------------------------------------------------------------#
# NODES
#----------------------

def affichage_rules(rules):
    """ Création des éléments pour les régles
        Liste des rules : BOXES = id -> objet.visual.box
    """    
    boxes = {}
    
    for rule in rules:
        #z = randrange(0, 500)
        #regles = box(pos = (rule[1][2][1][0][1], rule[1][2][1][1][1], z) , \
        #            length=30, height=30, width=30, color=color.blue)
        regles = box(pos = (rule[1][2][1][0][1], rule[1][2][1][1][1]) , \
                    length=30, height=30, width=30, color=color.blue)    
        boxes[rule[1][0][1]] = regles

    return boxes    


def affichage_species(species):
    """ Création des éléments pour les espèces
        Liste des species : SPHERES = id -> objet.visual.sphere
    """
    spheres = {}    

    for specie in species:
       #z = randrange(0, 500)    
   #especes = sphere(pos = (specie[1][2][1][0][1], \specie[1][2][1][1][1], z), \
   #        radius=20, color=color.green) 
        especes = sphere(pos = (specie[1][2][1][0][1], specie[1][2][1][1][1]), \
                radius=20, color=color.green)    
        spheres[specie[1][0][1]] = especes

    return spheres
        
#------------------------------------------------------------------------------#
# EDGES
#----------------------

def affichage_arrows(edges, node_coord):
    """ Création des éléments pour les liens entre règles et espèces
        Liste des liens : POINTERS_ID = numéro -> source_id, target_id
        Liste des arrows : POINTERS = numéro -> objet.visual.arrows
    """   

    pointers = {}
    pointers_id = {}    
    cpt = 0

    for edge in edges:
        cpt = cpt + 1    
        coord = {}    
        source = edge[1][0][1] 
        target = edge[1][1][1]
        coord['source'] = source
        coord['target'] = target
        #pointer = arrow(\
   #          pos = (node_coordD[source]['x'], \
   #                 node_coord[source]['y'], \
   #                 node_coord[source]['z']), \
   #          axis = (node_coord[target]['x'] - node_coord[source]['x'], \
   #                  node_coord[target]['y'] - node_coord[source]['y'], \
   #                  node_coord[target]['z'] - node_coord[source]['z']),\
   #          shaftwidth = 5, color = (0.5, 0.5, 0.5))
        pointer = arrow(\
                  pos = (node_coord[source]['x'], \
                         node_coord[source]['y']), \
                 axis = (node_coord[target]['x'] - \
                            node_coord[source]['x'], \
                         node_coord[target]['y'] - \
                            node_coord[source]['y']), \
                  shaftwidth = 5, color = (0.5, 0.5, 0.5))
        pointers_id[cpt] = coord
        pointers[cpt] = pointer 

    return pointers_id, pointers







