#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
 
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



lbrack = Literal("[").suppress()
rbrack = Literal("]").suppress()
pound = ("#")

comment = pound + Optional( restOfLine )

integer = Word(nums+'-').setParseAction(lambda s,l,t: [int(t[0])])
real = Regex(r"[+-]?\d+\.\d*([eE][+-]?\d+)?").setParseAction(
    lambda s,l,t: [float(t[0])])
dblQuotedString.setParseAction( removeQuotes )

key = Word(alphas,alphanums+'_')

value_atom = (real | integer | Word(alphanums) | dblQuotedString) 
value = Forward()   # to be defined later with << operator
keyvalue = Group(key+value)

value << (value_atom | Group( lbrack + ZeroOrMore(keyvalue) + rbrack ))
node = Group(Literal("node") + lbrack + Group(OneOrMore(keyvalue)) + rbrack)
edge = Group(Literal("edge") + lbrack + Group(OneOrMore(keyvalue)) + rbrack)

creator = Group(Literal("Creator")+ Optional( restOfLine ))
version = Group(Literal("Version")+ Optional( restOfLine ))
graphkey = Literal("graph").suppress()

graph = Dict (Optional(creator)+Optional(version)+\
    graphkey + lbrack + ZeroOrMore( (node|edge|keyvalue) ) + rbrack )
graph.ignore(comment)

res = graph.parseString(data)

for li in res:
    print li

fileout = open("parsedata.dat","w")
pickle.dump(res,fileout)
fileout.close()












