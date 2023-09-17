#scale slightly broken


import time
import math
import random
import matplotlib.pyplot as plt
import pygame
pygame.font.init()


win = pygame.display.set_mode((900,900))
pygame.display.set_caption("pendulum phase space, y-axis omega, x-axis theta")


vectorLengths = []
xAxis = ["-8","-6","-4","-2","0","2","4","6","8"]
yAxis = ["6","4","2","0","-2,","-4","6"]

xAxisValues = []
yAxisValues = []
#xAxisValues = [-8,-7.5,-7,-6.5,-6,-5.5,-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8]
#yAxisValues = [-6,-5.5,-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]
for i in range(49):
    yAxisValues.append(-6+0.25*i)
for i in range(65):
    xAxisValues.append(-8+0.25*i)
print(xAxisValues)
print(yAxisValues)

font1 = "freesansbold.ttf"
deltaT = 0.01
mass = 1.0
length = 1.0
dragCoefficient = 0.3
dragConstant = 1

def draw_text(font,text,text_colour,size,xcor,ycor):
    
    fonts = pygame.font.Font(font,size)
    text_surface = fonts.render(text,True,text_colour)
    text_rect = text_surface.get_rect()
    text_rect.center = (xcor,ycor)
    win.blit(text_surface,text_rect)


def drawVector(omega,theta,i,j):
    x = math.sin(theta)
    omegadot = -((9.81/length)*(x)) - ((dragConstant/mass)*omega)
    rise = omegadot*deltaT
    run = omega*deltaT
    vectorLength = (rise**2 + run**2)**0.5
    rise = rise*(6/vectorLength)  # scales the vector
    run = run*(25/vectorLength)
    xCord = i*18 -125 - run/2
    yCord = j*(900/65)+(900/8)- run/2
    if vectorLength>0.1:
        colour = (255,0,0)
    elif vectorLength>0.05:
        colour = (255,153,0)
    else:
        colour = (255,255,0)
    pygame.draw.line(win,colour,(xCord,yCord),((xCord + run),(yCord + rise)),2)
    pygame.draw.circle(win,colour,((xCord + run),(yCord + rise)),2)
    vectorLengths.append(vectorLength)


pygame.draw.line(win,(255,255,255),(450,0),(450,900),2)
pygame.draw.line(win,(255,255,255),(0,450),(900,450),2)
draw_text(font1,"X: Angle to vertical/ radians",(255,255,255),15,130,430)
draw_text(font1,"Y: Omega/radians per second",(255,255,255),15,580,20)
'''
for i in range(9):
    if i == 4:
        pass
    else:
        draw_text(font1,(xAxis[i]),(255,255,255),15,(i*100 +50),475)
for i in range(7):
    if i == 3:
        pass
    else:draw_text(font1,(yAxis[i]),(255,255,255),15,475,(i*(900/7)+(900/14)))
'''

value = 0

for i in range(len(xAxisValues)):
    if i == ((len(xAxisValues)-1)/2):
        pass
    else:
        for j in range(len(yAxisValues)):
            if j ==(len(yAxisValues)-1)/2:
                if xAxisValues[i] % 1 == 0:
                    
                    draw_text(font1,str(xAxisValues[i]),(255,255,255),15,((900/17)*value),470)
                    value+=1
            else:

                drawVector((yAxisValues[j]),(xAxisValues[i]),i,j)


pygame.display.update()




