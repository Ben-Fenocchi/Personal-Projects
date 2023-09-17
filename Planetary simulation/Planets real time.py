    #found out:
#if mass of planet isnt negligible in comparison to the star then the axis of the elliptical orbit will shift(precession)
#Mass of a sattelite will not affect its orbit,(e.g. twice gravitational force but acceleration is halved if mass is twice as much, otherwise space walks would be dangerous)
#As closer to planet faster, gpe to ke
#conic sections
#things orbit about the combined center of gravity of whole system
import math
import matplotlib.pyplot as plt
import random
import pygame
win = pygame.display.set_mode((1000,1000))


#g = 6.67*(10**(-11))
g = 1
deltaT = 0.01

colours = [(255,0,0),(0,0,255),(0,255,0),(125,0,125),(125,25,0)]
planets = []
otherPlanets = []

#planets.append([[350,500],[0,-1.5],(600),"planet2"])
#planets.append([[650,500],[0,1.5],(600),"planet3"])

'''# binary star system
planets.append([[800,500],[0,0.6454972244],(375),"planet2"])#
planets.append([[200,500],[0,-0.3227486122],(750),"planet3"])#
'''
 # elliptical orbit
planets.append([[500,900],[25,5],(10),"planet1"]) #
planets.append([[750,500],[0,0],(750000),"planet2"])#

''' # larger elliptical orbit
planets.append([[500,900],[40,0],(10),"planet1"]) #
planets.append([[750,500],[0,0],(750000),"planet2"])#
'''
''' # even larger elliptical orbit
planets.append([[500,900],[45,0],(10),"planet1"]) #
planets.append([[750,500],[0,0],(750000),"planet2"])#
'''
run = True
counter = 0
while run:
    #win.fill((0,0,0))

    for i in range(len(planets)):
        totalForcex = 0
        totalForcey = 0
        otherPlanets = planets.copy()
        otherPlanets.remove(planets[i])#creates a list of all other planets so you can add up forces
        for j in range(len(otherPlanets)):
            deltax = planets[i][0][0] - otherPlanets[j][0][0] #calculates diff in x and y co-ords between planets
            deltay = planets[i][0][1] - otherPlanets[j][0][1]
            displacement = (deltax**2 + deltay**2)**0.5
            if displacement<1:
                print("crashy crash crash")
            mass1 = otherPlanets[j][2]
            mass2 = planets[i][2]
            force = (g*mass1*mass2)/(displacement**2)
            xForce = (deltax/displacement) *  force
            yForce = (deltay/displacement) *  force
            totalForcex += xForce
            totalForcey += yForce
        accelerationx = -totalForcex/(planets[i][2])
        accelerationy = -totalForcey/(planets[i][2])
        
        deltaVelx = (accelerationx * deltaT)
        deltaVely = (accelerationy * deltaT)
        
        planets[i][1][0]+= deltaVelx #updates planets velocities
        planets[i][1][1]+= deltaVely
        
        planets[i][0][0] += (planets[i][1][0] * deltaT) # updates planets co-ords by adding the vel*time period
        planets[i][0][1] += (planets[i][1][1] * deltaT)
        
        
        pygame.draw.circle(win,(colours[i]),(planets[i][0][0],planets[i][0][1]),2)
    pygame.display.update()
        



