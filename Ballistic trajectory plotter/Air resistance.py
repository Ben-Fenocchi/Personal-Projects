import math
import random
import matplotlib.pyplot as plt
import time


def draw_graph(graphs_drawn,file,colours):

    def pick_shape():
        choice = int(input("Press: \n 1 for aerofoil \n 2 for car \n 3 for ball \n 4 for flat surface"))
        shapes = ["aerofoil","car","ball","flat surface"]
        for i in range(4):
            
            if i+1 == choice:
                shape = shapes[i]
        return shape
    def calculate_crosssection(shape):
        if shape == "areofoil":
            crosssection = float(input("Enter the cross-section in m^2"))
        if shape == "car":
            crosssection = float(input("Enter the cross-section in m^2"))
        if shape == "flat surface":
            width = float(input("enter the width"))
            height = float(input("Enter the height"))
            crosssection = width * height
        if shape == "ball":
            radius = float(input("enter radius"))
            crosssection = math.pi*radius**2
        return crosssection     
    def calculate_delta_vy(drag_coefficient,air_density,crosssection,time_interval,mass,vy,vx):
        beta = 0.5*drag_coefficient*air_density*crosssection
        deltavy = (-9.81-((beta/mass)*(vy*(math.sqrt(vx**2+vy**2)))))*time_interval
        return deltavy
    def calculate_delta_vx(drag_coefficient,air_density,crosssection,time_interval,mass,vy,vx):
        beta = 0.5*drag_coefficient*air_density*crosssection
        deltavx = (-((beta/mass)*(vx*(math.sqrt(vx**2+vy**2)))))*time_interval
        return deltavx
    def select_colours(colours):
        for i in range(len(colours)):
            print(colours[i])
        colour = input("please type the colour you wish this line to be")
        colour = colour.lower()
        colour = colour.strip()
        if colour =="blue":
            colour = "b"
        if colour =="green":
            colour = "g"
        if colour =="red":
            colour = "r"
        if colour =="cyan":
            colour = "c"
        if colour =="magenta":
            colour = "m"
        if colour =="yellow":
            colour = "y"
        if colour =="black":
            colour = "k"
        if colour =="white":
            colour = "w"    
        return(colour)

    if graphs_drawn>=1:
        choice = int(input(("Do you want to keep settings from graph",graphs_drawn,"?,1 for yes 2 for no\n there will be a chance to change values even if you keep the last settings")))
    if graphs_drawn>=1 and choice == 1:
        file.close()
        file = open("last_graph_details.txt","r")
        
        if choice ==1:
            settings = ["starting_height","angle","vely","velx","mass","drag_coefficient","cross_section","air_density","time_interval","total_time"]
            for line in file:
                details= line.split(",")
                for i in range(len(settings)):
                    if details[0]==settings[i]:
                        settings[i] = details[1]

        file.close()
        file = open("last_graph_details.txt","r")
        starting_height = float(settings[0])
        angle = float(settings[1])
        vely = float(settings[2])
        velx = float(settings[3])
        mass = float(settings[4])
        drag_coefficient = float(settings[5])
        cross_section = float(settings[6])
        air_density = float(settings[7])
        time_interval = float(settings[8])
        total_time = float(settings[9])
        print("Current values: \n Starting Height",starting_height,"\n angle",angle,"\n vely",vely,"\n velx",velx,"\n mass",mass,"\n Drag co-efficient",drag_coefficient,"\n Cross-section",cross_section,"\n Air density",air_density,"\n Time interval",time_interval,"\n Total time",total_time)
        time.sleep(3)
        choices =["Do you want to change either: ","\n 1-Starting Height","\n 2-angle ","\n 3-Y-velocity ","\n 4-X velocity ","\n 5-mass"," \n 6-co-efficient of drag"," \n 7-cross-section ","\n 8-density of air ","\n 9-Time interval","\n 10-Total time"]
        for i in range(len(choices)):
            print(choices[i])
            time.sleep(0.5)
        satisfied = False    
        while satisfied == False:
            choice = int(input("press 1 - 10 for your corresponding variable or zero for none"))
            if choice ==1:
                starting_height = float(input("Starting Height"))
                print("Your Starting Height is",starting_height)
            if choice ==2:
                angle = float(input("Enter new angle"))
                print("Your new angle is",angle)
            if choice ==3:
                vely = float(input("Enter new Y-velocity"))
                print("Your new Y-velocity",vely)
            if choice ==4:
                velx = float(input("Enter new X velocity"))
                print("Your new X velocity is",velx)
            if choice ==5:
                mass = float(input("Enter new mass"))
                print("Your new mass is",mass)            
            if choice == 6:
                drag_coefficient==float(input("Enter new drag co-efficient"))
                print("Your new Drag co-efficient is",drag_coefficient)
            if choice == 7:
                cross_section = float(input("Enter new cross section in meters squared"))
                print("Your new Cross section is",cross_section)
            if choice == 8:
                air_density = float(input("Enter new air density in kg/m^3"))
                print("Your new Air density is",air_density)
            if choice ==9:
                time_interval = float(input("Enter new time interval"))
                print("Your new Time interval is",time_interval)
            if choice ==10:
                total_time = float(input("Enter new Total time"))
                print("Your new Total time is",total_time)
            another = int(input("Please press 1 to alter another value, 2 if you are satisfied"))
            if another == 2:
                satisfied = True

            colour = select_colours(colours)
            




            
   
    if graphs_drawn == 0 or choice ==2:
        starting_height = float(input("What is the starting hieght of the projectile above ground"))
        angle = ((int(input("Enter angle:")))/360)*(2*math.pi)
        vel = int(input("enter vel:"))
        vely = vel* math.sin(angle)
        velx = vel* math.cos(angle)
        print("X velocity is",velx)
        print("Y velocity is",vely)
        mass = float(input("Enter mass in KG:"))
        shape = pick_shape()
        print(shape,"Has been selected")
        drag_coefficient = 0.45
        cross_section = calculate_crosssection(shape)
        air_density = 1.21
        time_interval = 0.1
        total_time=10
        print("Current values: \n Drag co-efficient",drag_coefficient,"\n Cross-section",cross_section,"\n Air density",air_density,"\n Time interval",time_interval,"\n Total time",total_time)
        time.sleep(2)
        choice =int(input("Do you want to change either \n 1-co-efficient of drag \n 2-cross-section \n 3-density of air \n 4-Time interval\n 5-Total time\n press 1 2 3 4 or 5 or zero for none"))
        if choice == 1:
            drag_coefficient==float(input("Enter new drag co-efficient"))
            print("Your new Drag co-efficient is",drag_coefficient)

        if choice == 2:
            cross_section = float(input("Enter new cross section in meters squared"))
            print("Your new Cross section is",cross_section)
        if choice == 3:
            air_density = float(input("Enter new air density in kg/m^3"))
            print("Your new Air density is",air_density)
        if choice ==4:
            time_interval = float(input("Enter new time interval"))
            print("Your new Time interval is",time_interval)
        if choice ==5:
            total_time = float(input("Enter new Total time"))
            print("Your new Total time is",total_time)



        file.write("starting_height,"+(repr(starting_height))+",\n")
        file.write("angle,"+repr(angle)+",\n")
        file.write("vely,"+repr(vely)+",\n")
        file.write("velx,"+repr(velx)+",\n")
        file.write("mass,"+repr(mass)+",\n")        
        file.write("drag_coefficient,"+repr(drag_coefficient)+",\n")
        file.write("cross_section,"+repr(cross_section)+",\n")
        file.write("air_density,"+repr(air_density)+",\n")
        file.write("time_interval,"+repr(time_interval)+",\n")
        file.write("total_time,"+repr(total_time)+",\n")
        colour = select_colours(colours)

    
    vx =[]
    vy =[]
    sx =[]
    sy =[]
    Time =[]
    vx.append(velx)
    vy.append(vely)#adds the first velocity and e#
    sx.append(0)
    sy.append(starting_height)

    for i in range(round(total_time/time_interval)):
        new_vx = vx[i]+ calculate_delta_vx(drag_coefficient,air_density,cross_section,time_interval,mass,vy[i],vx[i])
        new_vy = vy[i]+ calculate_delta_vy(drag_coefficient,air_density,cross_section,time_interval,mass,vy[i],vx[i])
        vx.append(new_vx)
        vy.append(new_vy)
    i=0
    while i< (round(total_time/time_interval)):
        x = sx[i]+(vx[i]*time_interval)
        sx.append(x)
        y = sy[i]+(vy[i]*time_interval)
        sy.append(y)
        i+=1
        if y<=0:
            break

    


    plt.plot(sx,sy,(str(colour)+"+"))
    '''
    plt.xlabel("Horizontal displacement")
    plt.ylabel("Vertical displacement")
    '''
 

###########################################################################################################################

previous_details_array = []
file = open("last_graph_details.txt","w")

why_the_hell = True
while why_the_hell == True:
    graphs_drawn = 0
    colours= ["Blue","Green","Red","Cyan","Magenta","Yellow","Black","White"]
    graphs = int(input("How many graphs to plot?"))
    for i in range(graphs):
        draw_graph(graphs_drawn,file,colours)
        graphs_drawn +=1

    plt.show()
    plt.close()

    file.close()
    file = open("last_graph_details.txt","r")
    print(file.read())
    choice = int(input("Would You like to run the program again?\n 1 for yes, 2 for no"))
    if choice == 2:
        why_the_hell = False
        

