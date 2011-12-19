#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
 
from pyparsing import Literal, Word, Forward, ZeroOrMore, Group, Dict, \
                Optional, restOfLine, alphas, alphanums, nums, OneOrMore, \
                removeQuotes, dblQuotedString, Regex
             

# Import gml file
FILIN = open('./Visu/Graphs/model_14_03_2010_coordOrganic.gml', 'r') 
CONTENU = FILIN.readlines()
FILIN.close()

DATA = "".join(CONTENU)

#print data

LBRACK = Literal("[").suppress()
RBRACK = Literal("]").suppress()
POUND = ("#")

COMMENT = POUND + Optional( restOfLine )

INTEGER = Word(nums + '-').setParseAction(lambda s, l, t: [int(t[0])])
REAL = Regex(r"[+-]?\d+\.\d*([eE][+-]?\d+)?").setParseAction(
        lambda s, l, t: [float(t[0])])
dblQuotedString.setParseAction(removeQuotes)

KEY = Word(alphas, alphanums + '_')

VALUE_ATOM = (REAL | INTEGER | Word(alphanums) | dblQuotedString) 
VALUE = Forward() 
KEYVALUE = Group(KEY + VALUE)

VALUE << (VALUE_ATOM | Group(LBRACK + ZeroOrMore(KEYVALUE) + RBRACK))
NODE = Group(Literal("node") + LBRACK + Group(OneOrMore(KEYVALUE)) + RBRACK)
EDGE = Group(Literal("edge") + LBRACK + Group(OneOrMore(KEYVALUE)) + RBRACK)

CREATOR = Group(Literal("Creator") + Optional(restOfLine))
VERSION = Group(Literal("Version") + Optional(restOfLine))
GRAPHKEY = Literal("graph").suppress()

GRAPH = Dict(Optional(CREATOR) + Optional(VERSION) + \
                GRAPHKEY + LBRACK + \
                ZeroOrMore((NODE | EDGE | KEYVALUE)) + RBRACK)
GRAPH.ignore(COMMENT)

PARSING_RESULTS = GRAPH.parseString(DATA)

for li in PARSING_RESULTS:
    print li

FILOUT = open("parsedata.dat","w")
pickle.dump(PARSING_RESULTS, FILOUT)
FILOUT.close()












