# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#---
#--- Simulation du superhopf.
#---
#--- Mestivier Denis
#---
#-----------------------------------------------------------

from visual import *
import random
import os
import sys
import povexport

#--- flag
doPov = False

#--- necessaire pour l'export vers POV
if doPov:
	scene.range = 7

#--- fixe l'intervalle des variables
myLimit = 2.5
xmin = -myLimit
xmax =  myLimit
ymin = -myLimit
ymax =  myLimit

#--- fixe les parametres de la simulation
npts =  100  # le nombre de point par dimension (x,y)
sig  =  0.5 # le bruit
a    =  7.5 # le parametre de la bifurcation

t    =     0.000 # temps initial
tmax =     100.00 # temps final
dt   =     0.005  # pas d'integration

#------------------------------------------------------------------
#--- Les fonctions
#------------------------------------------------------------------

#--------------------------------------------
#--- Update un point
#--------------------------------------------

def updatePts( p, a, sig, rd, dt ):
    # recupere la coord.
    xcor = p.x
    ycor = p.y

    # calculs intermediaires
    rho  =   xcor*xcor + ycor*ycor
    dx   = - xcor*rho - ycor*( 1.0 + a*rho )
    dy   =   xcor*( 1.0 + a*rho ) - ycor*rho

    # new coord
    velocity = vector( dx, dy, 0 )
    p.pos = p.pos + dt*velocity + rd
   
#--------------------------------------------
#--- Modifie les coordonnees des points
#--------------------------------------------

def one_step( listOfPts, a, sig, dt ):

    rd = ( math.sqrt( dt ) * sig ) * random.gauss( 0.0, 1.0 )
    rd = vector( rd, 0, 0 )
    
    for p in listOfPts:
        updatePts( p, a, sig, rd, dt )

#----------------------------------
#--- Cree l'ensemble des points ---
#----------------------------------

def initPts( xmin, xmax, ymin, ymax, npts ):

    lPts= []

    n1 = npts - 1
    inv_n1 = 1.0/n1
    dx = ( xmax-xmin ) * inv_n1
    dy = ( ymax-ymin ) * inv_n1
   
    for i in range( 0, npts ):
        xi = xmin + i * dx
        for j in range( 0, npts ):
            yi = ymin + j * dy

            # choisi la couleur...
            ri = double(i * inv_n1 )
            gi = double(j * inv_n1 )

            # points not implemented in povexport : lPts.append( points( pos=(xi,yi,0), size=3, color=(ri,gi,0) ) )
            lPts.append( sphere( pos=(xi,yi,0), radius=0.02, color=(ri,gi,0) ) )

    return lPts

#----------------------------------------------------------
#---
#--- Programme principal
#---
#----------------------------------------------------------
#--- Modification de la fenetre graphique
#scene.stereo = "redcyan"    # pour anaglyp
scene.background = ( 1,1,1 ) # fond blanc
scene.title = "Superhopf-3D"
#scene.autoscale = False       # automatic scaling (default)
scene.userspin = True        # the user can rotate the scene
scene.userzoom = True        # user can zoom in and out of the scene.
scene.fullscreen = False
#scene.autocenter = True

#--- Creation des points dans l'espace
listOfPts = initPts( xmin, xmax, ymin, ymax, npts )
num_image = 1

while t<tmax:
    rate(500)
    one_step( listOfPts, a, sig, dt )

    t = t + dt
    print t

    # export vers POV
    if doPov:
        if num_image % 10 == 0:
	
	    outputRep = "/home/mestivier/Progs/SuperHopf/vPython/PovOutput"
            outputBasename = "sh%010i.pov" % num_image
    
            filename = os.path.join( outputRep, outputBasename )
            povexport.export( filename = filename )
            print filename
        num_image = num_image + 1

