import math
import matplotlib.pyplot as plt
import random
import pygame

#g = 6.67*(10**(-11))
g = 1

planets = []
otherPlanets = []


finished = False

'''
deltaT = float(input("enter deltaT"))
print("Enter co-ords for new Planet in form xco-ord,yco-ord, for a 100 X 100 grid")
print("please enter starting velocity of planet in form yvel,xvel,   1 is one co-ord on grid")
print("please enter relative masses of planets, around 5 is avg mass")

while not finished:
    
    xCoord = float(input("Enter x co-ord :"))
    yCoord = float(input("Enter y xo-ord :"))
    coords = [xCoord,yCoord]

    xVel = float(input("Enter x Vel :"))
    yVel = float(input("Enter y Vel :"))
    velocities = [xVel,yVel]
    
    relativeMass = float(input("Mass:"))
    planets.append((coords,velocities,relativeMass))
    newPlanet = int(input("Press 1 to add new planet,0 to stop"))

    if newPlanet !=1:
        finished = True
'''
deltaT = 0.1

planets.append([[50,0],[0,1],(1),"planet1"])
planets.append([[-100,0],[0,-1],(1),"planet2"])
planets.append([[0,0],[0,0],(50),"planet3"])

'''
positions = [([[],[]],)*(len(planets))]
'''
positions = [
[[],[]],
[[],[]],
[[],[]],

    ]
print(positions)

#layout of the positions array
'''
positions = [
[(xcoords),(ycoords)],           #for planet 1
[(xcoords),(ycoords)],            #for planet 2
[(xcoords),(ycoords)],            #for planet 3

ect....

[

'''

for x in range(5000000):
    
    for i in range(len(planets)):
        
        totalForcex = 0
        totalForcey = 0
        otherPlanets = planets.copy()
        otherPlanets.remove(planets[i])#creates a list of all other planets so you can add up forces
        for j in range(len(otherPlanets)):
            deltax = planets[i][0][0] - otherPlanets[j][0][0] #calculates diff in x and y co-ords between planets
            deltay = planets[i][0][1] - otherPlanets[j][0][1]
            displacement = (deltax**2 + deltay**2)**0.5
            mass1 = otherPlanets[j][2]
            mass2 = planets[i][2]
            force = (g*mass1*mass2)/(displacement**2)
            xForce = (deltax/displacement) *  force
            yForce = (deltay/displacement) *  force
            totalForcex += xForce
            totalForcey += yForce
        accelerationx = -totalForcex/(planets[i][2])
        accelerationy = -totalForcey/(planets[i][2])
        
        deltaVelx = accelerationx * deltaT
        deltaVely = accelerationy * deltaT
        
        planets[i][1][0]+= deltaVelx #updates planets velocities
        planets[i][1][1]+= deltaVely
        
        planets[i][0][0] += planets[i][1][0] * deltaT # updates planets co-ords by adding the vel*time period
        planets[i][0][1] += planets[i][1][1] * deltaT
        
        (positions[i][0]).append(planets[i][0][0]) # adds new x and y locations to the position array holding all x and y co-ords for each planet
        (positions[i][1]).append(planets[i][0][1])


print(planets)
print(positions)
for i in range(len(planets)):
    plt.plot(positions[i][0],positions[i][1])

plt.show()






        
        
