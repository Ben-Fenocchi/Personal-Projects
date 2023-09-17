import math
import random
import matplotlib.pyplot as plt
import time

#energy = 0
energyIntoGas = 0
energyFromGas = 0
deltaPressure = 0
gasConstant = 8.3145
totalVolume = (float(input("please enter piston and cylinder head volume combined in cm^3")))/1000000
volumeCylinderHead = (float(input("please enter cylinder head volume in cm^3")))/1000000
volume = totalVolume
atmosphericPressure = 100000.0
temperature = 293.0
deltaTemperature = 0
pressure = atmosphericPressure
deltaVolume = -0.00000001
volumes = []
pressures = []
temperatures = []
volumes.append(volume)
pressures.append(pressure)
temperatures.append(temperature)

molesGas = (atmosphericPressure*totalVolume)/(gasConstant*temperature)
molesOxygen = 0.21*molesGas
molesOctane = molesOxygen/12.5
energyCombustionOctane = 5074100*molesOctane

def calculateDeltaPressure(pressure,volume,deltaVolume,temperature):
    deltaTemperature = ((-0.4*pressure*deltaVolume)/(gasConstant*molesGas))
    deltaPressure = (((molesGas*gasConstant*deltaTemperature)/(volume))+((-molesGas*gasConstant*temperature*deltaVolume)/(volume**2)))
    return(deltaPressure,deltaTemperature)


def integrate(file,deltaVolume):
    energy = 0
    f = open(file,"r")
    for line in f:
        content = line.split(",")
        if content[0] == "V/cm^3":
            pass
        else:
            pressure = float(content[2])
            energy += abs(pressure*deltaVolume)
    return(energy)

        
########plotting and recording compression data###########
for i in range(int((totalVolume-volumeCylinderHead)//(deltaVolume*-1))):
    deltaPressure , deltaTemperature = calculateDeltaPressure(pressure,volume,deltaVolume,temperature)
    pressure += deltaPressure
    temperature += deltaTemperature
    volume += deltaVolume
    volumes.append((volume)*1000000)
    pressures.append(pressure)
    temperatures.append(temperature)

f = open("compressionData.txt","w+")
f.write("V/cm^3,T/K,P/Pa")
f.write("\n")
for i in range(len(volumes)):
    f.write(str(round(volumes[i])))
    f.write(",")
    f.write(str(round(temperatures[i])))
    f.write(",")
    f.write(str(round(pressures[i])))
    f.write(",")
    f.write("\n")
f.close()

energyIntoGas = integrate("compressionData.txt",deltaVolume)



#####plotting the point from the combustion##########

#in theory below is correct, but produces weird graph of 50 percent efficiency, but this is for no friction, complete combustion, constant heat capacity, instantaneous explosion ect so isnt accurate

deltaTemperatureCombustion = (energyCombustionOctane)/(molesGas*2.5*gasConstant)
deltaPressureCombustion = (((molesGas*gasConstant)/volume)*deltaTemperatureCombustion)
temperature += deltaTemperatureCombustion
pressure += deltaPressureCombustion
pressures.append(pressure)
volumes.append(volume*1000000)
temperatures.append(temperature)
'''
deltaTemperatureCombustion = 2000
deltaPressureCombustion = (((molesGas*gasConstant)/volume)*deltaTemperatureCombustion)
pressure +=deltaPressureCombustion
temperature += deltaTemperatureCombustion
pressures.append(pressure)
volumes.append(volume*1000000)
temperatures.append(temperature)
'''
#####plotting adn recording the exhaust data
deltaVolume = deltaVolume*-1
for i in range(int((totalVolume-volumeCylinderHead)//(deltaVolume))):
    deltaPressure , deltaTemperature = calculateDeltaPressure(pressure,volume,deltaVolume,temperature)
    pressure += deltaPressure
    temperature += deltaTemperature
    volume += deltaVolume
    volumes.append((volume)*1000000)
    pressures.append(pressure)
    temperatures.append(temperature)
f = open("exhaustData.txt","w+")
f.write("V/cm^3,T/K,P/Pa")
f.write("\n")
x = (len(volumes)//2)
for i in range(x):
    f.write(str(round(volumes[x+i])))
    f.write(",")
    f.write(str(round(temperatures[x+i])))
    f.write(",")
    f.write(str(round(pressures[x+i])))
    f.write(",")
    f.write("\n")
f.close()

energyFromGas = integrate("exhaustData.txt",deltaVolume)

print("Energy supplied to piston:",(energyFromGas-energyIntoGas))
print("Efficiency:",((energyFromGas-energyIntoGas)*100/energyCombustionOctane),"%")

plt.plot(volumes,pressures,"+")
plt.xlabel("volume in cm^3")
plt.ylabel("pressure in MPa")
#plt.fill(x,y)
plt.show()

