import time
import math
import random
import matplotlib.pyplot as plt

'''
print("Please Enter")
omega = float(input("Angular velocity(rad/s) :"))
theta = math.pi/2
deltaT = float(input("Time period"))
mass = float(input("Mass :"))
length = float(input("Length :"))
dragCoefficient = float(input("Drag Coefficient of fluid :"))
dragConstant = float(6*math.pi*dragCoefficient)
'''
omegas = []
thetas = []

omega = -6
theta = 3
deltaT = 0.01
mass = 1.0
length = 1.0
dragCoefficient = 0.3
dragConstant = 1



def calculateNextOmega(omega,theta):
    x = math.sin(theta)
    omegadot = -((9.81/length)*(x)) - ((dragConstant/mass)*omega)
    omega += omegadot*deltaT
    return(omega)


for i in range(5000):
    i+=1
    omega = calculateNextOmega(omega,theta)
    theta += omega*deltaT

    omegas.append(omega)
    thetas.append(theta)

print(omegas)
print(thetas)

plt.plot(thetas,omegas)
plt.xlabel("Theta(rad)")
plt.ylabel("Omega(rad/s)")
plt.show()

