import os
import math
import pygame
import tkinter as tk

#Other Files/Functions
import Generate
import Export
import Simple #Simple often repeated functions

isopen = True

#Pygame window
pygame.init()
wireframedisplayX=1500
wireframedisplayY=750
#Drawing
Edge = (255,255,255)
Corner = (255,0,0)
Background = (0,0,255)

#These variables are in two different, files, they are temp/default
stock = "SheetMetal"

data = {}
data[2]=5
data[1]=10
data[0]=10
precision = 1
material = {}
material[0]="Aluminum"
material[1]=2700


space = {}
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
opens = {}
processplanner = {}
operationnum = 0


compressor = {}






#Finally going to define some functions
def generate():

    global boundaryX
    global boundaryY
    global boundaryZ
    boundaryX=data[0]
    boundaryY=data[1]
    boundaryZ=data[2]
    
    genWindow = tk.Tk()
    labelx=tk.Label(genWindow, text="Width X")
    labely=tk.Label(genWindow, text="Length Y")
    labelz=tk.Label(genWindow, text="Height Z")
    entryx=tk.Entry(genWindow, textvariable = data[0])
    entryy=tk.Entry(genWindow, textvariable = data[1])
    entryz=tk.Entry(genWindow, textvariable = data[2])

    labeld=tk.Label(genWindow, text="Diameter X Y")
    entryd=tk.Entry(genWindow, textvariable = data[1])

    labelb=tk.Label(genWindow, text="")
    

    def clear():
        labelx.grid_forget()
        labely.grid_forget()
        labelz.grid_forget()
        labeld.grid_forget()
        labelb.grid_forget()
        entryx.grid_forget()
        entryy.grid_forget()
        entryz.grid_forget()
        entryd.grid_forget()
    def sm():
        global stock
        stock= "SheetMetal"
        clear()
        labelx.grid(row=5, column=0)
        labely.grid(row=6, column=0)
        labelz.grid(row=7, column=0)
        entryx.grid(row=5, column=1)
        entryy.grid(row=6, column=1)
        entryz.grid(row=7, column=1)
    def bs():
        global stock
        stock= "BarStock"
        clear()
        labelx.grid(row=5, column=0)
        labely.grid(row=6, column=0)
        labelz.grid(row=7, column=0)
        entryx.grid(row=5, column=1)
        entryy.grid(row=6, column=1)
        entryz.grid(row=7, column=1)
    def rs():
        global stock
        stock= "RoundStock"
        print(stock)
        clear()
        labeld.grid(row=5, column=0)
        labelz.grid(row=6, column=0)
        labelb.grid(row=7, column=0)
        entryd.grid(row=5, column=1)
        entryz.grid(row=6, column=1)
    def p1():
        global precision
        precision = 1
    def p2():
        global precision
        precision = 10
    def p3():
        global precision
        precision = 100
    def size():
        data[0]=x
        data[1]=y
        data[2]=z
    def gen():
        global mode
        
        

        genWindow.destroy()
        if (stock=="SheetMetal"):
            boundaryX=data[0]
            boundaryY=data[1]
            boundaryZ=data[2]
            print("Thickness, Width, Height")
            print(data[0],'mm',data[1],'mm',data[2],'mm');

    #Ok, this is to assist the Z value to ensure there are enough blank spaces.
            x=data[1];
            if (data[2] > data[1]):
                x = data[2];
            spacesize=int((data[0]*precision)*(data[1]*precision)*(data[2]*precision) + (data[1]*precision)*(data[2]*precision)*(x*precision))
    #Generation code, just makes everything material withen the XYZ, also creates open space above it.
            for i in range(0, spacesize):
                if (i < int(data[0]*precision)*(data[1]*precision)*(data[2]*precision)):
                    space[i]=u"\u25A0";
                if (i >= int(data[0]*precision)*(data[1]*precision)*(data[2]*precision)):
                    space[i]=u"\u25A1";
            print(len(space));
            print((data[0]*precision)*(data[1]*precision)*(data[2]*precision));
            mode="SheetOperations"

        #RoundStockGeneration
        if (stock== "RoundStock"):
            print('test')
            boundaryX=data[0]
            boundaryY=data[1]
            boundaryZ=data[2]
            print("Diameter, Length");
            print(data[0], 'mm' ,data[1], 'mm');
            for k in range (-1, 0):
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=u"\u25A1";
            for k in range (int(boundaryZ), int(boundaryZ)+2):
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=u"\u25A1";
            data[2]=0


            if data[0]%2==1 or 1 == 1:
                for k in range (0, int(boundaryZ)):
                    for j in range (0, int(boundaryY)):
                        for i in range (0, int(boundaryX)):
                            if math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) <= (data[0]*precision)/2:
                                space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A0";
                                data[2]=data[2]+1
                            #elif math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) > (data[0]*precision)/2 and math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) < (data[0]*precision)/2+.8:
                                #space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A2";
                                
                            if math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) > (data[0]*precision)/2:
                                space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
            
            mode="StockOperations"
        #Barstock deatils   
        if (stock=="BarStock"):
            boundaryX=data[0]
            boundaryY=data[1]
            boundaryZ=data[2]
            mode = "StockOperations"
            for k in range (-1, 0):
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=u"\u25A1";
            for k in range (int(boundaryZ), int(boundaryZ)+2):
                for j in range (0, int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=u"\u25A1";
            for k in range (0, int(boundaryZ)*precision):
                for j in range (0, int(boundaryY)*precision):
                    for i in range (0, int(boundaryX)*precision):
                        space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=u"\u25A0";
            print("Thickness, Width, Height")
            print(data[0],'mm',data[1],'mm',data[2],'mm');
            mode="StockOperations"


    genWindow.title("JohnCAD Stock Generation")
    genWindow.geometry("350x250")
            
    tk.Label(genWindow, text="Stock Type:").grid(row=0, column=0)
    tk.Radiobutton(genWindow, text="Sheet Metal ", command = sm, variable = 0, value = 0).grid(row=1, column=0)
    tk.Radiobutton(genWindow, text="Bar Stock", command = bs, variable = 0, value = 1).grid(row=2, column=0)
    tk.Radiobutton(genWindow, text="Round Stock     ", command = rs, variable = 0, value = 2).grid(row=3, column=0)

    tk.Label(genWindow, text="Precision:").grid(row=0, column=1)
    tk.Radiobutton(genWindow, text="1/1 mm", command = p1, variable = 1, value = 0).grid(row=1, column=1)
    tk.Radiobutton(genWindow, text="1/10 mm", command = p2, variable = 1, value = 1).grid(row=2, column=1)
    tk.Radiobutton(genWindow, text="1/100 mm     ", command = p3, variable = 1, value = 2).grid(row=3, column=1)

    tk.Label(genWindow, text="Data Storage (Coming soon):").grid(row=0, column=2)
    tk.Radiobutton(genWindow, text="RAM (Faster)", command = p1, variable = 2, value = 0).grid(row=1, column=2)
    tk.Radiobutton(genWindow, text="Disk (For larger files)", command = p2, variable = 2, value = 1).grid(row=2, column=2)

    tk.Button(genWindow, text="Generate!", command = gen).grid(row=8, column=0)
    genWindow.mainloop()
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




generate()


print(precision)
print(stock)
print(mode)

#reminder to move this back down to thermal
restingtemp=0
for k in range (-1, int(boundaryZ+1)):
    for j in range (0, int(boundaryY)):
        for i in range (0, int(boundaryX)):
            spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=restingtemp
            spacetemp[0]=100




while (isopen==1):


    if (mode=="StockOperations"):
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

            for k in range(0, int(boundaryZ)*precision):
                for j in range(0, int(boundaryY)*precision):
                    for i in range(0, int(boundaryX)*precision):
                        front[int(i*(boundaryX*precision))+j]=u"\u25A1"
                        top[int(k*(boundaryX*precision))+i] = u"\u25A1"
                        right[int(k*(boundaryX*precision))+j] = u"\u25A1"

            #Generate Top
            for k in range(0, int(boundaryZ)*precision):
                for j in range(0, int(boundaryY)*precision):
                    for i in range(0, int(boundaryX)*precision):
                        if space[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == u"\u25A0":
                            top[int(k*(boundaryX*precision))+i] = u"\u25A0"
                            pygame.draw.rect(wireframedisplay,Edge,(i*displayscale,j*displayscale,1*displayscale,1*displayscale))
                        if top[int(k*(boundaryX*precision))+i] != u"\u25A0" and space[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == u"\u25A1":
                            top[int(k*(boundaryX*precision))+i] = u"\u25A1"
                            
            #Generate Front
            for k in range(0, int(boundaryZ)*precision):
                for j in range(0, int(boundaryY)*precision):
                    for i in range(0, int(boundaryX)*precision):
                        if space[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == u"\u25A0":
                            front[int(j*(boundaryX*precision))+i] = u"\u25A0"
                        if space[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == u"\u25A1":
                            front[int(j*(boundaryX*precision))+i] = u"\u25A1"
                            
                        #Draw hatch if on the outside
            #for k in range(0, int(boundaryZ)*precision):
                #for j in range(0, int(boundaryY)*precision):
                    #for i in range(0, int(boundaryX)*precision):
                        #if openl[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == 1 or openr[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == 1 or opent[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == 1 or openb[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == 1:
                            #front[int(j*(boundaryX*precision))+k] = u"\u25A4"



            #Generate Right
            for k in range(0, int(boundaryZ)*precision):
                for j in range(0, int(boundaryY)*precision):
                    for i in range(0, int(boundaryX)*precision):
                        if space[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == u"\u25A0":
                            right[int(k*(boundaryX*precision))+j] = u"\u25A0"
                        if right[int(k*(boundaryX*precision))+j] != u"\u25A0" and space[int(k*(boundaryX*boundaryY*precision)+j*(boundaryX*precision))+i] == u"\u25A1":
                            right[int(k*(boundaryX*precision))+j] = u"\u25A1"

                            
            pygame.display.update()
                        
        #Full Layered Display
        if (command == "H" or command == "h"):
            for k in range(0, int(boundaryZ)):
                print("");
                print("Layer ", k+1);
                for j in range(0, int(boundaryY)):
                    for i in range(0, int(boundaryX)):

                        print(space[   int(k*(boundaryX*boundaryY)+(boundaryY-1-j)*(boundaryX))+i     ], "" ,end = ""); #insert boundaryY-1- before j to swap y axis
                    print("");
                
                    
        #Export
        if (command == "E" or command == "e"):
            Export.export(boundaryX,boundaryY,boundaryZ)
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

        #temp defaults
        alphasymbolthing = .0000177
        thermalstep = .01
        dxyz=.001/precision
        



        
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

        if (command == "S" or command == "s"):

            for t in range (0, int(5)):
                for k in range (0, int(boundaryZ)):
                    for j in range (0,int(boundaryY)):
                        for i in range (0, int(boundaryX)):
                            ot=spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]
                            lt=spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i-1]
                            rt=spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i+1]
                            dt=spacetemp[k*(boundaryY*boundaryX)+(j-1)*(boundaryX)+i]
                            tt=spacetemp[k*(boundaryY*boundaryX)+(j+1)*(boundaryX)+i]
                            #This part was not my work
                            spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i] = ot + alphasymbolthing*thermalstep*(      (((lt-ot)/(dxyz)-(rt-ot)/(dxyz))/dxyz)+(((dt-ot)/(dxyz)-(tt-ot)/(dxyz))/dxyz)              )
            
        if (command == "H" or command == "h"):
            wireframedisplay=pygame.display.set_mode((wireframedisplayX,wireframedisplayY))
            pygame.display.set_caption("Face Wireframes")
            wireframedisplay.fill(Background)
            for k in range(0, int(boundaryZ)):
                print("");
                print("Layer ", k+1);
                for j in range(0, int(boundaryY)):
                    for i in range(0, int(boundaryX)):
                        color = ( abs(int(spacetemp[   int(0*(boundaryX*boundaryY)+j*(boundaryX))+i     ])/100*255),0,0)
                        
                        pygame.draw.rect(wireframedisplay,color,(i*10,j*10,1*10,1*10))
                        pygame.display.update()
                        print(spacetemp[   int(k*(boundaryX*boundaryY)+(boundaryY-1-j)*(boundaryX))+i     ], "" ,end = ""); #boundaryY-1- before j to swap y axis
                    print("");
            
                    
