#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
from pyparsing import Literal, CaselessLiteral, Word, Forward,\
             ZeroOrMore, Group, Dict, Optional, Combine,\
             ParseException, restOfLine, White, alphas, alphanums, nums,\
             OneOrMore,quotedString,removeQuotes,dblQuotedString, Regex, oneOf

# Import gml file
filin = open('./graph/model_14_03_2010_coordOrganic.gml', 'r') 
contenu = filin.readlines()
filin.close()

data = "".join(contenu)

#print data

# Define GML Grammar
digit = Word(nums)
sign = Optional(oneOf("+ -"))
mantissa = Optional("E"+sign+digit)   
real = sign + ZeroOrMore(digit) + Literal(".") + ZeroOrMore(digit) + mantissa
integer = sign + OneOrMore(digit)

key = Word(alphas, alphanums)
string = dblQuotedString

lcro = Literal("[").suppress()
rcro = Literal("]").suppress()

value_atom = (integer | real | string | Word(alphanums))

value = Forward() 
keyvalue = Group(key + value)
value << (value_atom | Group(lcro + ZeroOrMore(keyvalue) + rcro)) 

node = Group(Literal("node") + lcro + Group(OneOrMore(keyvalue)) + rcro)
edge = Group(Literal("edge") + lcro + Group(OneOrMore(keyvalue)) + rcro)

creator = Group(Literal("Creator") + Optional(restOfLine))
version = Group(Literal("Version") + Optional(restOfLine))

graph = Optional(creator) + Optional(version) + Literal("graph") + lcro + ZeroOrMore((node | edge | keyvalue)) + rcro

#Parse gml file
try:
    res = graph.parseString(data)
except ParseException, pe:
    print pe
    



