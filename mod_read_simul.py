#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

def poe_treatment(poe_csv, species_csv):
    """ Récupération des valeurs de simulation pour les especes
        Création Dico (numéro de simulation -> (especes -> POE)) 
    """
    
    species_list = []
    
    for specie in species_csv:
        species_list.append(specie)

    poe_value = {}
    no_of_simul = 1
    
    for value_of_poe in poe_csv:
        poe_specie = {}
        no_of_specie = 0
        
        for specie in species_list:     
            poe_specie[specie[0]] = value_of_poe[no_of_specie]
            no_of_specie = no_of_specie + 1
        
        poe_value[no_of_simul] = poe_specie
        no_of_simul = no_of_simul + 1

    return poe_value


def por_treatment(por_csv, rules_csv):
    """ Récupération des valeurs de simulation pour les rules
        Création Dico (numéro de simulation -> (rule -> POR)) 
    """
    
    rules_list = []
    
    for rule in rules_csv:
        rules_list.append(rule)

    por_value = {}
    no_of_simul = 1
    
    for value_of_por in por_csv:
        por_rule = {}
        no_of_rule = 0
        
        for rule in rules_list:     
            por_rule[rule[0]] = value_of_por[no_of_rule]
            no_of_rule = no_of_rule + 1
        
        por_value[no_of_simul] = por_rule
        no_of_simul = no_of_simul + 1

    return por_value



