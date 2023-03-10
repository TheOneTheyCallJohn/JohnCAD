import os
import math
import pygame
import tkinter as tk

#Other Files/Functions, Export not required as of now
import Generate
import Export
import Simple #Simple often repeated functions
#Pygame window
pygame.init()
wireframedisplayX=1500
wireframedisplayY=750
#Drawing
Edge = (255,255,255)
Corner = (255,0,0)
Background = (0,0,255)


mode="stockselect";
selection = 0;
isopen = 1;
data = {};
space = {};

#Space for temperature data
spacetemp = {};
spacek = {};
#Thermal Analysis
thermalsetup = {};
thermalsetup[0]=0;

#Highest and lowest points operated on to make exporting faster
highlow = {}

stlprep = {}
adjacents={}

operation = {}
lathe = {}
mill = {}
drill = {}

top = {}
front = {}
right = {}

theVs = {}
openl = {}
openr = {}
opena = {}
openf = {}
openb = {}
opent = {}
opens = {}
processplanner = {}
operationnum = 0
material = {}
material[0]="Aluminum"
material[1]=2700

compressor = {}

header = "solid MadeWithJohnCAD"
facetn = "facet normal 0 0 0"
oloop = 'outer loop'
eloop ='endloop'
endfacet = "endfacet"
footer = "endsolid MadeWithJohncad";
percision = 1;





#Finally going to define some functions
def points():
    point0= "vertex " + str(theVs[0]) + " " + str(theVs[1])+ " " + str(theVs[2])
    point1= "vertex " + str(theVs[3])+ " " + str(theVs[4])+ " " + str(theVs[5])
    point2= "vertex " + str(theVs[6])+ " " + str(theVs[7])+ " " + str(theVs[8])
    point3= "vertex " + str(theVs[9])+ " " + str(theVs[10])+ " " + str(theVs[11])
    point4= "vertex " + str(theVs[12])+ " " + str(theVs[13])+ " " + str(theVs[14])
    point5= "vertex " + str(theVs[15])+ " " + str(theVs[16])+ " " + str(theVs[17])

    export.write(facetn + '\n');
    export.write(oloop + '\n');                            
    export.write(str(point0) + '\n');
    export.write(str(point1) + '\n');
    export.write(str(point2) + '\n');
    export.write(eloop + '\n');
    export.write(endfacet + '\n');
    export.write(facetn + '\n');
    export.write(oloop + '\n');                            
    export.write(str(point3) + '\n');
    export.write(str(point4) + '\n');
    export.write(str(point5) + '\n');
    export.write(eloop + '\n');
    export.write(endfacet + '\n');
    export.write('\n');


def displaysetup():
    wireframedisplay=pygame.display.set_mode((wireframedisplayX,wireframedisplayY))
    pygame.display.set_caption("JohnCAD")
    wireframedisplay.fill(Background)
    displayscale=(750/boundaryY)/2

#These variables are in two different, files, they are temp/default
global x
global y
global z
stock="SheetMetal"
x=15
y=10
z=5


data[2]=5
data[1]=10
data[0]=15

#TIL "percision" is not spelled like that

Generate.generate(data,x,y,z,stock,percision,space)


while (isopen==1):
    #Sheetmetal operations
    if (mode=="SheetOperations"):
        print("Operations Menu:");
        print("Press S to Sheer");
        print("Press B to Bend");
        print("Press C to Cut");
        print("Press E to Export");
        print("Press D to Display");
        print("Press H to Full Display");
        
        command = input();
        
        if (command == "D" or command == "d"):



            
            #Starting with generating the Front :)
            for i in range (0, int(data[0]*percision)):
                for j in range (0, int(data[1]*percision*data[2]*percision)):
                    if space[int(data[0]*i+j)]==u"\u25A0":
                        top[j]=u"\u25A0";
                    if space[int(data[0]*i+j)]==u"\u25A1":
                        top[j]=u"\u25A1";
            #Generating the FRONT
            for i in range (0, int(data[2]*percision)):
                for j in range (0, int(data[0]*percision*data[1]*percision)):
                    if space[int(data[2]*i+j)]==u"\u25A0":
                        front[j]=u"\u25A0";
                    if space[int(data[2]*i+j)]==u"\u25A1":
                        front[j]=u"\u25A1";
            #Generating the RIGHT
            for i in range (0, int(data[1]*percision)):
                for j in range (0, int(data[2]*percision*data[0]*percision)):
                    if space[int(data[1]*i+j)]==u"\u25A0":
                        front[j]=u"\u25A0";
                    if space[int(data[1]*i+j)]==u"\u25A1":
                        front[j]=u"\u25A1";
            #Drawing the TOP
            print("Top");
            for i in range(0, int(data[2]*percision)):
                for j in range(0, int(data[1]*percision)):
                    print(top[int(i*data[1]*100+j)], "" ,end = "");
                print("");
            #Drawing the FRONT
            print("Front");
            for i in range(0, int(data[0]*percision)):
                for j in range(0, int(data[1]*percision)):
                    print(top[int(i*data[1]*100+j)], "" ,end = "");
                print("");
            #Drawing the RIGHT
            print("Right");
            for i in range(0, int(data[0]*percision)):
                for j in range(0, int(data[2]*percision)):
                    print(top[int(i*data[2]*100+j)], "" ,end = "");
                print("");

            print("");
            


            
        if (command == "E" or command == "e"):
            export = open('export.txt', 'w');
            export.write(header + '\n');
            for i in range (0, data[2]*10):
                    for j in range (0,data[1]*10):
                        
                        export.write(facetn + '\n');
                        export.write(oloop + '\n');
                        for k in range (0,3):
                            export.write("vector: v1x v1y v1z" + '\n');
                        export.write(eloop + '\n');
                        export.write(endfacet + '\n');
            export.close();
        

    if (mode == "StockOperations"):
        print("Operations");
        print("Press M for Mill operations")
        print("Press L for Lathe operations")
        print("Enter E for Export STL");
        print("Enter P for Export Process Plan");
        print("Enter D for Display");
        print("Enter H for Layered Display");
        print("Enter A for Analysis");

        command=input();



        #Display
        if (command == "D" or command == "d"):


            #Window Output
            wireframedisplay=pygame.display.set_mode((wireframedisplayX,wireframedisplayY))
            pygame.display.set_caption("Face Wireframes")
            wireframedisplay.fill(Background)
            displayscale=(750/boundaryY)/2

            for k in range(0, int(boundaryZ)*percision):
                for j in range(0, int(boundaryY)*percision):
                    for i in range(0, int(boundaryX)*percision):
                        front[int(i*(boundaryX*percision))+j]=u"\u25A1"
                        top[int(k*(boundaryX*percision))+i] = u"\u25A1"
                        right[int(k*(boundaryX*percision))+j] = u"\u25A1"

            #Generate Top
            for k in range(0, int(boundaryZ)*percision):
                for j in range(0, int(boundaryY)*percision):
                    for i in range(0, int(boundaryX)*percision):
                        if space[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == u"\u25A0":
                            top[int(k*(boundaryX*percision))+i] = u"\u25A0"
                            pygame.draw.rect(wireframedisplay,Edge,(i*displayscale,j*displayscale,1*displayscale,1*displayscale))
                        if top[int(k*(boundaryX*percision))+i] != u"\u25A0" and space[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == u"\u25A1":
                            top[int(k*(boundaryX*percision))+i] = u"\u25A1"
                            
            #Generate Front
            for k in range(0, int(boundaryZ)*percision):
                for j in range(0, int(boundaryY)*percision):
                    for i in range(0, int(boundaryX)*percision):
                        if space[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == u"\u25A0":
                            front[int(j*(boundaryX*percision))+i] = u"\u25A0"
                        if space[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == u"\u25A1":
                            front[int(j*(boundaryX*percision))+i] = u"\u25A1"
                            
                        #Draw hatch if on the outside
            #for k in range(0, int(boundaryZ)*percision):
                #for j in range(0, int(boundaryY)*percision):
                    #for i in range(0, int(boundaryX)*percision):
                        #if openl[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == 1 or openr[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == 1 or opent[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == 1 or openb[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == 1:
                            #front[int(j*(boundaryX*percision))+k] = u"\u25A4"



            #Generate Right
            for k in range(0, int(boundaryZ)*percision):
                for j in range(0, int(boundaryY)*percision):
                    for i in range(0, int(boundaryX)*percision):
                        if space[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == u"\u25A0":
                            right[int(k*(boundaryX*percision))+j] = u"\u25A0"
                        if right[int(k*(boundaryX*percision))+j] != u"\u25A0" and space[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == u"\u25A1":
                            right[int(k*(boundaryX*percision))+j] = u"\u25A1"

                            
            pygame.display.update()
                        
        #Full Layered Display
        if (command == "H" or command == "h"):
            for k in range(0, int(boundaryZ)):
                print("");
                print("Layer ", k+1);
                for j in range(0, int(boundaryY)):
                    for i in range(0, int(boundaryX)):
                        #space[   int(k*(boundaryX*boundaryY)+j*(boundaryX))+i] = int(k*(boundaryX*boundaryY)+j*(boundaryX)+i)
                        #space[   int(i*(boundaryX*boundaryY)+j*(boundaryX))+k] =int(math.sqrt((k-((data[0]+2)/2-.5))**2+(j-((data[0]+2)/2-.5))**2))
                        print(space[   int(k*(boundaryX*boundaryY)+(boundaryY-1-j)*(boundaryX))+i     ], "" ,end = ""); #insert boundaryY-1- before j to swap y axis
                    print("");
                
                    
        #Export
        if (command == "E" or command == "e"):
            Export.export
        if (command == "P" or command == "p"):
            exportpname = input('Enter File Name')
            exportpname = exportpname + ".txt"
            exportp = open(exportpname, 'w');
            exportp.write("Process Plan" + '\n');
            processplanner[0]=0
            processplanner[1]=2
            processplanner[2]=3
            for i in range (0, 1):
                if int(processplanner[i]) == 0:
                    exportp.write("Lathe Bore " + '\n');
                    exportp.write("Diameter " + str(processplanner[i+1]) + '\n');
                    exportp.write("Depth " + str(processplanner[i+2]) + '\n');
                    i=i+2
                if processplanner[i]==1:
                    exportp.write("Mill" + '\n');        
            exportp.close();

        if (command == "A" or command == "a"):
            mode = "Analysis"

                    
        if (command == "L" or command == "l"):
            mode = "LatheOperations"
            lathe[0]=0;
            lathe[1]=0;

        if (command == "M" or command == "m"):
            mode = "MillOperations"

        if (command == "T" or command =="t"):
            mode = "DrillOperations"

    if (mode == "LatheOperations"):
        print("Operations >>> Lathe Operations")
        print("Enter O for Offset Currently:");
        print("Enter D for Direction");
        print("Enter B to Front/Back Bore");
        print("Enter F to Face");
        print("Enter T to Turn");
        print("Enter E to Thread")
        print("Enter Z to return");
        
        command=input();

        print(len(space))

        if (command == "O" or command == "o"):
            print("Enter Offset X")
            lathe[0]=0;
            lathe[0]=input();
            lathe[0]=int(lathe[0])
            print("Enter Offset Y")
            lathe[1]=0;
            lathe[1]=input();
            lathe[1]=int(lathe[1])

        if (command == "z"):
            mode = "StockOperations"
        #Boreing, formerly drilling
        if (command == "B" or command == "b"):
            print("Enter Bit Diameter");
            operation[0]=input();
            operation[0]=int(operation[0]);
            print("Enter Depth Or T for Thru");
            operation[1]=input();
            if ( operation[1] == "T" or operation[1] == "t" or int(operation[1]) > int(boundaryZ)):
                operation[1] = boundaryZ;

            for k in range (0, int(operation[1])):
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        if math.sqrt((i+.5-((boundaryX+lathe[0])/2))**2+(j+.5-((boundaryY+lathe[1])/2))**2) <= (operation[0]-1)/2:
                            space[k*(boundaryX*boundaryY)+j*(boundaryX)+i]=u"\u25A1";
        #TURNING 
        if (command == "T" or command == "t"):
            print("Enter Bit Diameter");
            operation[0]=input();
            operation[0]=int(operation[0]);
            print("Enter Start Depth");
            operation[2]=input();
            print("Enter Depth Or T for Thru");
            operation[1]=input();
            if ( operation[1] == "T" or operation[1] == "t" or int(operation[1]) > int(data[1])):
                operation[1] = boundaryZ;
            
            for k in range (int(operation[2]), int(operation[1])):
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        if (int(math.sqrt(         (i-(boundaryX+lathe[0])/2+.5)**2         +(j-(boundaryY+lathe[1])/2+.5)**2          )   ) >= operation[0]/2):
                            space[k*(boundaryX*boundaryY)+j*(boundaryX)+i]=u"\u25A1";
        #Threading
        if (command == "E" or command == "e"):
            print("Enter Inner Diameter")
            operation[0]=input()
            operation[0]=int(operation[0])
            print("Enter Outer Diameter")
            operation[4]=input()
            operation[4]=int(operation[4])
            print("Enter mm between threads")
            operation[3]=input()
            operation[3]=int(operation[3])
            print("Enter Start Depth")
            operation[2]=input()
            operation[2]=int(operation[2])
            print("Enter Final Depth")
            operation[1]=input()
            operation[1]=int(operation[1])
            for k in range (int(operation[2]), int(operation[1])):
                angle=-(k%operation[3])/operation[3]*360
                t1=(operation[4]-operation[0])*math.sin(angle*math.pi/180)
                t2=(operation[4]-operation[0])*math.cos(angle*math.pi/180)
                
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        if (int(math.sqrt(         (i-(boundaryX+lathe[0]+t1)/2+.5)**2         +(j-(boundaryY+lathe[1]+t2)/2+.5)**2          )   ) >= operation[0]/2):
                            space[k*(boundaryX*boundaryY)+j*(boundaryX)+i]=u"\u25A1";

                            
    #Milling
    if (mode == "MillOperations"):
        print("Operations >>> Mill Operations")
        print("Enter P for Pocketing:");
        print("Enter D for Direction");
        print("Enter D for Facing");
        print("Enter S for Slotting");
        print("Enter Z to return");
        command=input();

        if (command == "Z" or command == "z"):
            mode = "StockOperations";
        if (command == "P" or command == "p"):
            print("Enter Bit Diameter")
            operation[0]=int(input());
            print("Enter Depth")
            operation[1]=int(input());
            print("Enter Start X")
            operation[2]=int(input());
            print("Enter Start Y")
            operation[3]=int(input());
            print("Enter End X")
            operation[4]=int(input());
            if operation[4] < operation[2]+operation[0]+1:
                operation[4] = operation[2]+operation[0]+1
            print("Enter End Y")
            operation[5]=int(input());
            if operation[5] < operation[3]+operation[0]+1:
                operation[5] = operation[3]+operation[0]+1

                
            
            for i in range (0, int(operation[1])):
                for j in range (0, int(boundaryY)):
                    for k in range (0, int(boundaryZ)):
                        for l in range(int(operation[3])+int(operation[0]/2), int(operation[5])-int(operation[0]/2)):
                            for m in range(int(operation[2]+operation[0]/2),int(operation[4]-operation[0]/2)):
                                if (int(math.sqrt((k-m)**2+(j-l)**2) <= int(operation[0])/2)):
                                    space[i*(data[0])**2+j*(data[0])+k]=u"\u25A1";


        if (command == "S" or command == "s"):
            print("Enter Bit Diameter")
            operation[0]=int(input());
            print("Enter Bit Depth")
            operation[1]=int(input());
            print("Enter Direction H or V")
            operation[2]="h"
            if (operation[2] == "H" or operation[2] == "h"):  
                print("Enter Y")
                operation[3]=int(input());
                #print("Enter Start X")
                #operation[4]=int(input());        
                #print("Enter End X")
                #operation[5]=int(input());
            if (operation[2] == "V" or operation[2] == "v"):  
                print("Enter X")
                operation[3]=int(input());
                print("Enter Start Y")
                operation[4]=int(input());        
                print("Enter End Y")
                operation[5]=int(input());
    
            for k in range (0, int(operation[1])):
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        if (abs(j-operation[3]) < operation[0]/2):
                            space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] = u"\u25A1"

    #Drill                    
    if (mode == "DrillOperations"):
        drill[0]=0
        drill[1]=0
        print("Operations >>> DrillTool Operations")
        print("Enter T for Taper:");
        print("Enter Z to return");
        command=input();
        if (command == "Z" or command == "z"):
            mode = "StockOperations";
        if (command == "T" or command == "t"):
            print("Enter Inner Diameter")
            operation[0]=input()
            operation[0]=int(operation[0])
            print("Enter Outer Diameter")
            operation[4]=input()
            operation[4]=int(operation[4])
            print("Enter mm between threads")
            operation[3]=input()
            operation[3]=int(operation[3])
            print("Enter Start Depth")
            operation[2]=input()
            operation[2]=int(operation[2])
            print("Enter Final Depth")
            operation[1]=input()
            operation[1]=int(operation[1])
            for k in range (int(operation[2]), int(operation[1])):
                angle=(k%operation[3])/operation[3]*360
                t1=(operation[0]-operation[4])*math.sin(angle*math.pi/180)
                t2=(operation[0]-operation[4])*math.cos(angle*math.pi/180)
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        if (int(math.sqrt(         (i-(boundaryX+drill[0]+t1)/2+.5)**2         +(j-(boundaryY+drill[1]+t2)/2+.5)**2          )   ) <= operation[4]/2):
                            space[k*(boundaryX*boundaryY)+j*(boundaryX)+i]=u"\u25A1";
        
    if (mode == "Analysis"):

        if (command == "Z" or command == "z"):
            mode = "StockOperations";
        
        material[2]=0
        for k in range (0, int(boundaryZ)):
            for j in range (0,int(boundaryY)):
                for i in range (0, int(boundaryX)):
                    if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0"):
                        material[2]=material[2]+1;
        print("Operations >>> Analysis")
        print("Enter M to select Material");
        print("Density", material[1], "kg/m3")
        print("Initial Volume", data[2]/1000, "m3")
        print("Volume", material[2]/1000, "m3");
        print("Mass", material[1]*(material[2]/1000), "Kg");
        print("Enter T for Thermal Analysis");
        print("Enter Z to return");
        
        command=input();
        if (command == "Z" or command == "z"):
            mode = "StockOperations";




            #From https://www.theworldmaterial.com/density-of-metals/
        if (command == "M" or command == "m"):
            print("a: Steel, Density 7,850 kg/m3")
            print("b: Iron, Density 7,870 kg/m3")
            print("c: Stainless Steel, Density 7,850 kg/m3")
            print("d: Aluminum, Density 2,700 kg/m3")
            print("e: Carbon, Density 7,250 kg/m3")
            command=input();
            if (command == "A" or command == "a"):
                material[0]="Steel"
                material[1]=7850
            if (command == "B" or command == "b"):
                material[0]="Iron"
                material[1]=7870
            if (command == "C" or command == "c"):
                material[0]="Stainless Steel"
                material[1]=7850
            if (command == "D" or command == "d"):
                material[0]="Aluminum"
                material[1]=2700
            if (command == "E" or command == "e"):
                material[0]="Carbon"
                material[1]=7250
                
        if (command == "T" or command == "t"):
            mode = "ThermalAnalysis"


    if (mode == "ThermalAnalysis"):
        print("Operations >>> Analysis >>> Thermal");
        print("Enter H to View");
        print("Enter T to set Time", thermalsetup[0]);
        print("Enter I to set Initial Conditions");
        print("Enter S to Solve");
        print("Enter Z to return");
        command=input();


        
        if (command == "Z" or command == "z"):
            mode == "Analysis"

            
        if (command == "T" or command == "t"):
            print("Enter time after initial conditions")
            thermalsetup[0] = input();

        if (command == "I" or command == "i"):
            print("Enter X Coordinate")
            thermalsetup[1] = input();
            print("Enter Y Coordinate")
            thermalsetup[2] = input();
            print("Enter Z Coordinate")
            thermalsetup[3] = input();
            print("Enter Initial Temp");
            thermalsetup[4] = input();
            spacetemp[int(thermalsetup[3])*(boundaryY*boundaryX)+int(thermalsetup[2])*(boundaryX)+ int(thermalsetup[1])]=int(thermalsetup[4]);
#heat transfer rate Q = (t1-t2)/R
#R = L/KA  L thickness? k conducivity, A area
            
            
        if (command == "H" or command == "h"):
            for k in range (0, int(boundaryZ)):
                for j in range (0,int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A1"):
                            spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]="X";
                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0"):
                            spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
            for k in range(0, int(boundaryZ)*percision):
                print("");
                print("Layer ", i+1);
                for j in range(0, int(boundaryY)*percision):
                    for i in range(0, int(boundaryX)*percision):
                        print(spacetemp[   int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i     ], u"\u00B0" ,end = "");
                    print("");
