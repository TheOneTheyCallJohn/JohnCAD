import os
import math

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





while (isopen==1):

    if (mode=="stockselect"):
        print("Select Stock:");
        print("'S' SheetMetal Comming Soon");
        print("'B' Flat Bar Stock");
        print("'R' RoundStock");
        print("'W' Weld Comming Soon");
        print("'P' Percision Select Currently 1/", percision, "mm")
        command = input();
        
        if (command == "S" or command == "s"):
            stock="SheetMetal";
            mode="Sdetails";
        if (command == "B" or command == "b"):
            stock="Barstock";
            mode="Bdetails";
        if (command == "R" or command == "r"):
            stock="Roundstock";
            mode="Rdetails";
        if (command=="C"):
            stock="Cast";
            mode="Cdetails";
        if (command == "P" or command == "p"):
            print("Enter Percision in 1/x mm, should probably be 1 for now")
            percision = int(input())




    if (mode=="Sdetails"):
        while (selection==0):
            print("Enter Thickness (Z):");
            command = input();
            command = float(command);
            if (command > 0):
                data[0] = command;
                selection=1;
        while (selection==1):
            print("Enter Dimensions Width (X):");
            command = input();
            command = float(command);
            if (command > 0):
                data[1] = command;
                selection=2;
        while (selection==2):
            print("Enter Dimensions Length (Y):");
            command = input();
            command = float(command);
            if (command > 0):
                data[2] = command;
                mode = "SheetOperations";
                selection=0;
        print("Thickness, Width, Height")
        print(data[0],'mm',data[1],'mm',data[2],'mm');

#Ok, this is to assist the Z value to ensure there are enough blank spaces.
        x=data[1];
        if (data[2] > data[1]):
            x = data[2];
        command = input("Press Enter To Generate");
        spacesize=int((data[0]*percision)*(data[1]*percision)*(data[2]*percision) + (data[1]*percision)*(data[2]*percision)*(x*percision))
#Generation code, just makes everything material withen the XYZ, also creates open space above it.
        for i in range(0, spacesize):
            if (i < int(data[0]*percision)*(data[1]*percision)*(data[2]*percision)):
                space[i]=u"\u25A0";
            if (i >= int(data[0]*percision)*(data[1]*percision)*(data[2]*percision)):
                space[i]=u"\u25A1";
        print(len(space));
        print((data[0]*percision)*(data[1]*percision)*(data[2]*percision));


    #RoundStockGeneration
    if (mode== "Rdetails"):
        while (selection==0):
            print("Enter Stock Diameter")
            command = input();
            command = int(command)
            if (isinstance(command, int) and command > 0):
                command = float(command);
                data[0] = command;
                boundaryX=command*percision;
                boundaryY=command*percision;
                selection=1;
        while (selection==1):
            print("Enter Stock Length")
            command = input();
            command = int(command)
            if (isinstance(command, int) and command > 0):
                command = float(command);
                data[1] = command;
                boundaryZ = command*percision;
                mode = "StockOperations";
                selection=0;
        print("Diameter, Length");
        print(data[0], 'mm' ,data[1], 'mm');
        command = input("Press Enter To Generate");
        


        #Round Generation
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
                        if math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) <= (data[0]*percision)/2:
                            space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A0";
                            data[2]=data[2]+1
                        #elif math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) > (data[0]*percision)/2 and math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) < (data[0]*percision)/2+1:
                            #space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A2";
                            
                        elif math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) > (data[0]*percision)/2:
                            space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
                            
    #Barstock deatils   
    if (mode=="Bdetails"):
        while (selection==0):
            print("Enter Stock Width X")
            command = input();
            command = float(command);
            data[0] = 1
            if (command > 0):
                data[0] = command;
                boundaryX=command*percision;
                selection=1;
        while (selection==1):
            print("Enter Stock Height Y")
            command = input();
            command = float(command);
            data[1] = 1;
            if (command > 0):
                data[1] = command;
                boundaryY = command*percision;
                mode = "StockOperations";
                selection=2;
        while (selection==2):
            print("Enter Stock Length Z")
            command = input();
            command = float(command);
            data[1] = 1;
            if (command > 0):
                data[2] = command;
                boundaryZ = command*percision;
                mode = "StockOperations";
                selection=0;
        for k in range (-1, 0):
            for j in range (0, int(boundaryY)):
                for i in range (0, int(boundaryX)):
                    space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=u"\u25A1";
        for k in range (int(boundaryZ), int(boundaryZ)+2):
            for j in range (0, int(boundaryY)):
                for i in range (0, int(boundaryX)):
                    space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=u"\u25A1";
        for k in range (0, int(boundaryZ)*percision):
            for j in range (0, int(boundaryY)*percision):
                for i in range (0, int(boundaryX)*percision):
                    space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=u"\u25A0";
        print("Thickness, Width, Height")
        print(data[0],'mm',data[1],'mm',data[2],'mm');

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

            #Detect Openspaces around (Rework generation and delete this part)
#            for k in range(0, int(boundaryZ)*percision):
#                for j in range(0, int(boundaryY)*percision):
#                    for i in range(0, int(boundaryX)*percision):
#                        openl[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
#                        openr[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
#                        openb[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
#                        opent[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
#                        opena[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
#                        openf[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;

                            
#                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0"):
#                            if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+(i-1)]) == u"\u25A1" or i == 0:
#                                openl[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                            if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+(i+1)]) == u"\u25A1" or i == boundaryX-1:
#                                openr[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                                
#                            if (space[k*(boundaryY*boundaryX)+(j-1)*(boundaryX)+i]) == u"\u25A1" or j == 0:
#                                openb[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                            if (space[k*(boundaryY*boundaryX)+(j+1)*(boundaryX)+i]) == u"\u25A1" or j == boundaryY-1:
#                                opent[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                                
#                            if (space[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i]) == u"\u25A1" or k == 0:
#                                openf[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                            if (space[(k+1)*(boundaryY*boundaryX)+j*(boundaryX)+i]) == u"\u25A1" or k == boundaryZ-1:
#                                opena[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;




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
                        if top[int(k*(boundaryX*percision))+i] != u"\u25A0" and space[int(k*(boundaryX*boundaryY*percision)+j*(boundaryX*percision))+i] == u"\u25A1":
                            top[int(k*(boundaryX*percision))+i] = u"\u25A1"
            #Draw Top
            print("Top")
            for i in range(0, int(boundaryZ)*percision):
                for j in range(0, int(boundaryX)*percision):
                    print(top[int(i*(boundaryY*percision))+j], "" ,end = "")
                print("")

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


                            
            #Draw Front and Right


            print("Front", "                   ", "Right")
            for i in range(0, int(boundaryY)*percision):
                for j in range(0, int(boundaryX)*percision):
                    print(front[int(i*(boundaryX*percision))+j], "" ,end = "")
                print(" ",end = "")
                for k in range(0, int(boundaryZ)*percision):
                    print(right[int(k*(boundaryY*percision))+i], "" ,end = "")
                print("")

            
#            print("Front")
#            for i in range(0, int(boundaryY)*percision):
#                for j in range(0, int(boundaryX)*percision):
#                    print(front[int(i*(boundaryX*percision))+j], "" ,end = "")
#                print("")




            #Draw Right
#            print("Right")
#            for i in range(0, int(boundaryX)*percision):
#                for j in range(0, int(boundaryZ)*percision):
#                    print(right[int(j*(boundaryY*percision))+i], "" ,end = "")
#                print("")
                            

                        
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
            exportname = input('Enter File Name')
            exportname = exportname + ".stl"
            export = open(exportname, 'w');
            export.write(header + '\n');
            #Identify which blocks are adjacent to open space (Delete soon)
            #for k in range (0, int(boundaryZ)):
            #    for j in range (0,int(boundaryY)):
            #        for i in range (0, int(boundaryX)):
            #            stlprep[k*(boundaryY*boundaryX)+j*(boundaryX)+i] = space[k*(boundaryY*boundaryX)+j*(boundaryX)+i];
            #            openl[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
            #            openr[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
            #            opena[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
            #            openf[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
            #            openb[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
            #            opent[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
            #            opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=0;
                        
                        
            #for k in range (0, int(boundaryZ)):
            #    for j in range (0,int(boundaryY)):
            #        for i in range (0, int(boundaryX)):
            #            stlprep[k*(boundaryY*boundaryX)+j*(boundaryX)+i] = space[k*(boundaryY*boundaryX)+j*(boundaryX)+i];
            #            if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0"):

#                            if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+(i-1)]) == u"\u25A1":
#                                openl[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                                opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]+1
#                            if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+(i+1)]) == u"\u25A1":
#                                openr[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                                opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]+1
#                            if (space[k*(boundaryY*boundaryX)+(j-1)*(boundaryX)+i]) == u"\u25A1":
#                                opena[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                                opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]+1
#                            if (space[k*(boundaryY*boundaryX)+(j+1)*(boundaryX)+i]) == u"\u25A1":
#                                openf[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                                opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]+1
#                            if (space[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i]) == u"\u25A1":
#                                openb[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                                opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]+1
#                            if (space[(k+1)*(boundaryY*boundaryX)+j*(boundaryX)+i]) == u"\u25A1":
#                                opent[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=1;
#                                opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=opens[k*(boundaryY*boundaryX)+j*(boundaryX)+i]+1

            #Compress STLS and hopefuflly make it run faster
            #Bottom Compression
            for k in range (0, int(boundaryZ)):
                for j in range (0,int(boundaryY)):
                    compressor[0] = -1
                    compressor[1] = -1
                    compressor[2] = -1
                    compressor[3] = -1
                    for i in range (0, int(boundaryX)):
                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0" and space[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i] != u"\u25A0" and compressor[0] == -1):
                            compressor[0]=i
                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0" and (space[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] == u"\u25A0" or space[(k)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] != u"\u25A0" or i==boundaryX-1) and compressor[0] != -1 and compressor[1] == -1):
                            compressor[1]=i+1
                        if compressor[0] != -1 and compressor[1] != -1:
                            #Triangle RealAft1
                            theVs[0]=compressor[0]/percision
                            theVs[1]=j/percision+1/percision
                            theVs[2]=k/percision

                            theVs[3]=compressor[1]/percision
                            theVs[4]=j/percision
                            theVs[5]=k/percision

                            theVs[6]=compressor[0]/percision
                            theVs[7]=j/percision
                            theVs[8]=k/percision
                            #Triangle RealAft2
                            theVs[9]=compressor[1]/percision
                            theVs[10]=j/percision
                            theVs[11]=k/percision

                            theVs[12]=compressor[0]/percision
                            theVs[13]=j/percision+1/percision
                            theVs[14]=k/percision
    
                            theVs[15]=compressor[1]/percision
                            theVs[16]=j/percision+1/percision
                            theVs[17]=k/percision
                            
                            points()

                            compressor[0]=-1
                            compressor[1]=-1

                        #Front
                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0" and space[(k+1)*(boundaryY*boundaryX)+j*(boundaryX)+i] != u"\u25A0" and compressor[2] == -1):
                            compressor[2]=i
                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0" and (space[(k+1)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] == u"\u25A0" or space[(k)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] != u"\u25A0" or i==boundaryX-1) and compressor[2] != -1 and compressor[3] == -1):
                            compressor[3]=i+1
                        if compressor[2] != -1 and compressor[3] != -1:
                            #Triangle RealFront1
                            theVs[0]=compressor[2]/percision
                            theVs[1]=j/percision+1/percision
                            theVs[2]=k/percision+1/percision

                            theVs[3]=compressor[2]/percision
                            theVs[4]=j/percision
                            theVs[5]=k/percision+1/percision
                            
                            theVs[6]=compressor[3]/percision
                            theVs[7]=j/percision
                            theVs[8]=k/percision+1/percision
                            
                            #Triangle RealFront2
                            theVs[9]=compressor[2]/percision
                            theVs[10]=j/percision+1/percision
                            theVs[11]=k/percision+1/percision
                            
                            theVs[12]=compressor[3]/percision
                            theVs[13]=j/percision
                            theVs[14]=k/percision+1/percision

                            theVs[15]=compressor[3]/percision
                            theVs[16]=j/percision+1/percision
                            theVs[17]=k/percision+1/percision
                            
                            points()
                                
                            compressor[2]=-1
                            compressor[3]=-1


#Going to have two more of these loops for the time being, for left right, and top down
            for j in range (0,int(boundaryY)):
                for k in range (0, int(boundaryZ)):
                    compressor[0] = -1
                    compressor[1] = -1
                    compressor[2] = -1
                    for i in range (0, int(boundaryX)):
                        #Bottom
                        if (space[k*(boundaryZ*boundaryX)+j*(boundaryZ)+i] == u"\u25A0" and space[(k)*(boundaryZ*boundaryX)+(j-1)*(boundaryZ)+i] == u"\u25A1" and +(space[(k)*(boundaryY*boundaryX)+j*(boundaryX)+i-1] == u"\u25A1" or i == 0)):
                            compressor[0]=k
                            compressor[1]=i
                        if (space[k*(boundaryZ*boundaryX)+j*(boundaryZ)+i] == u"\u25A0" and space[(k)*(boundaryZ*boundaryX)+(j-1)*(boundaryZ)+(i)] != u"\u25A0" and space[(k)*(boundaryY*boundaryX)+j*(boundaryX)+(i+1)] == u"\u25A1" and (space[(k)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] == u"\u25A1" or i == boundaryX-1)):
                            compressor[2]=i+1
                        if compressor[0] != -1 and compressor[1] != -1 and compressor[2]!= -1:
                            #print('test')
                                #Triangle Bottom1
                            theVs[0]=i/percision+1/percision
                            theVs[1]=j/percision+1/percision
                            theVs[2]=compressor[0]/percision

                            theVs[3]=i/percision
                            theVs[4]=j/percision+1/percision
                            theVs[5]=k/percision+1/percision

                            theVs[6]=i/percision+1/percision
                            theVs[7]=j/percision+1/percision
                            theVs[8]=k/percision+1/percision
                                #Triangle Bottom2
                            theVs[9]=i/percision
                            theVs[10]=j/percision+1/percision
                            theVs[11]=compressor[0]/percision

                            theVs[12]=i/percision
                            theVs[13]=j/percision+1/percision
                            theVs[14]=k/percision+1/percision

                            theVs[15]=i/percision+1/percision
                            theVs[16]=j/percision+1/percision
                            theVs[17]=k/percision

                            #points()




                            compressor[0]=-1
                            compressor[1]=-1
                            compressor[2]=-1


                        
                                                
            for k in range (0, int(boundaryZ)):
                for j in range (0,int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0"):
                            
                            if (space[(k)*(boundaryY*boundaryX)+(j)*(boundaryX)+i-1] == u"\u25A1" or i == 0):
                                #Triangle L1
                                theVs[0]=i/percision
                                theVs[1]=j/percision
                                theVs[2]=k/percision+1/percision

                                theVs[3]=i/percision
                                theVs[4]=j/percision+1/percision
                                theVs[5]=k/percision+1/percision

                                theVs[6]=i/percision
                                theVs[7]=j/percision
                                theVs[8]=k/percision
                                #Triangle L2
                                theVs[9]=i/percision
                                theVs[10]=j/percision
                                theVs[11]=k/percision

                                theVs[12]=i/percision
                                theVs[13]=j/percision+1/percision
                                theVs[14]=k/percision+1/percision

                                theVs[15]=i/percision
                                theVs[16]=j/percision+1/percision
                                theVs[17]=k/percision

                                points()
    
                            if (space[(k)*(boundaryY*boundaryX)+(j)*(boundaryX)+i+1] == u"\u25A1"  or i == boundaryX-1):
                                #Triangle R1
                                theVs[0]=i/percision+1/percision
                                theVs[1]=j/percision
                                theVs[2]=k/percision

                                theVs[3]=i/percision+1/percision
                                theVs[4]=j/percision+1/percision
                                theVs[5]=k/percision+1/percision

                                theVs[6]=i/percision+1/percision
                                theVs[7]=j/percision
                                theVs[8]=k/percision+1/percision
                                #Triangle R2
                                theVs[9]=i/percision+1/percision
                                theVs[10]=j/percision+1/percision
                                theVs[11]=k/percision

                                theVs[12]=i/percision+1/percision
                                theVs[13]=j/percision+1/percision
                                theVs[14]=k/percision+1/percision

                                theVs[15]=i/percision+1/percision
                                theVs[16]=j/percision
                                theVs[17]=k/percision

                                points()
                                
                            if (space[(k)*(boundaryY*boundaryX)+(j-1)*(boundaryX)+i] == u"\u25A1"  or j == 0):
                                #Triangle Top1
                                theVs[0]=i/percision+1/percision
                                theVs[1]=j/percision
                                theVs[2]=k/percision+1/percision

                                theVs[3]=i/percision
                                theVs[4]=j/percision
                                theVs[5]=k/percision+1/percision

                                theVs[6]=i/percision+1/percision
                                theVs[7]=j/percision
                                theVs[8]=k/percision
                                #Triangle Top2
                                theVs[9]=i/percision+1/percision
                                theVs[10]=j/percision
                                theVs[11]=k/percision

                                theVs[12]=i/percision
                                theVs[13]=j/percision
                                theVs[14]=k/percision+1/percision

                                theVs[15]=i/percision
                                theVs[16]=j/percision
                                theVs[17]=k/percision

                                points()

                            if (space[(k)*(boundaryY*boundaryX)+(j+1)*(boundaryX)+i] == u"\u25A1"  or j == boundaryY-1):
                                #Triangle Bottom1
                                theVs[0]=i/percision+1/percision
                                theVs[1]=j/percision+1/percision
                                theVs[2]=k/percision

                                theVs[3]=i/percision
                                theVs[4]=j/percision+1/percision
                                theVs[5]=k/percision+1/percision

                                theVs[6]=i/percision+1/percision
                                theVs[7]=j/percision+1/percision
                                theVs[8]=k/percision+1/percision
                                #Triangle Bottom2
                                theVs[9]=i/percision
                                theVs[10]=j/percision+1/percision
                                theVs[11]=k/percision

                                theVs[12]=i/percision
                                theVs[13]=j/percision+1/percision
                                theVs[14]=k/percision+1/percision

                                theVs[15]=i/percision+1/percision
                                theVs[16]=j/percision+1/percision
                                theVs[17]=k/percision

                                points()


                            
            export.write(footer + '\n');
            export.close();

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
            mode = "DrillToolOperations"

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
                angle=(k%operation[3])/operation[3]*360
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

    #Hand tools                    
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
