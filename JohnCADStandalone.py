#until fuctions return, I have created a showcase heatsink, maybe dont take the results to heart yet.
import os
import math
import pygame
import tkinter as tk

isopen = True



#These variables are in two different, files, they are temp/default
stock = "SheetMetal"

data = {}
data[0]=55#60
data[1]=55#60
data[2]=40 #40
precision = 1
material = {}
material[0]="Aluminum"
material[1]=2700


space = {}
#Space for temperature data
spacetemp = {};
ospacetemp = {};
#Thermal Analysis
thermalsetup = {};
thermalsetup[0]=0;

#Highest and lowest points operated on to make exporting faster
highlow = {}

stlprep = {}
adjacents={}

operation = {}
operation[0]=0
lathe = {}
mill = {}
drill = {}

header = "solid MadeWithJohnCAD"
facetn = "facet normal 0 0 0"
oloop = 'outer loop'
eloop ='endloop'
endfacet = "endfacet"
footer = "endsolid MadeWithJohncad";
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
            boundaryX=data[0]*precision
            boundaryY=data[1]*precision
            boundaryZ=data[2]*precision
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
            boundaryX=data[0]*precision
            boundaryY=data[1]*precision
            boundaryZ=data[2]*precision
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
    genWindow.geometry("550x250")
            
    tk.Label(genWindow, text="Stock Type:").grid(row=0, column=0)
    tk.Radiobutton(genWindow, text="Sheet Metal ", command = sm, variable = 0, value = 0).grid(row=1, column=0)
    tk.Radiobutton(genWindow, text="Bar Stock", command = bs, variable = 0, value = 1).grid(row=2, column=0)
    tk.Radiobutton(genWindow, text="Round Stock     ", command = rs, variable = 0, value = 2).grid(row=3, column=0)

    tk.Label(genWindow, text="Precision:").grid(row=0, column=1)
    tk.Radiobutton(genWindow, text="1/1 mm", command = p1, variable = 1, value = 0).grid(row=1, column=1)
    tk.Radiobutton(genWindow, text="1/10 mm", command = p2, variable = 1, value = 1).grid(row=2, column=1)
    tk.Radiobutton(genWindow, text="1/100 mm     ", command = p3, variable = 1, value = 2).grid(row=3, column=1)

    tk.Label(genWindow, text="Material:").grid(row=0, column=2)
    tk.Radiobutton(genWindow, text="Steel", command = p1, variable = 2, value = 0).grid(row=1, column=2)
    tk.Radiobutton(genWindow, text="Aluminum", command = p2, variable = 2, value = 1).grid(row=2, column=2)
    tk.Radiobutton(genWindow, text="Copper", command = p2, variable = 2, value = 2).grid(row=3, column=2)
    tk.Radiobutton(genWindow, text="Custom", command = p2, variable = 2, value = 3).grid(row=4, column=2)
    tk.Radiobutton(genWindow, text="None/Other", command = p2, variable = 2, value = 4).grid(row=5, column=2)

    tk.Label(genWindow, text="Data Storage (Coming soon):").grid(row=0, column=3)
    tk.Radiobutton(genWindow, text="RAM (Faster)", command = p1, variable = 3, value = 0).grid(row=1, column=3)
    tk.Radiobutton(genWindow, text="Disk (For larger files)", command = p2, variable = 3, value = 1).grid(row=2, column=3)

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








generate()
regenerate = True

print(precision)
print(stock)
print(mode)

#reminder to move this back down to thermal
roomtemp=20
for k in range (-1, int(boundaryZ+1)):
    for j in range (0, int(boundaryY)):
        for i in range (0, int(boundaryX)):
            spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=roomtemp



#move this to top when done with ui
#Pygame window
pygame.init()

#Drawing
Edge = (255,255,255)
Corner = (255,0,0)
Background = (64,244,208)
MenuRGB = (229,228,228)
width=1500
height=750
scale = 10
mdisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption("I humbly present JohnCAD")
mdisplay.fill(Background)

opfont= pygame.font.SysFont("candara",20)
menu1 = opfont.render("Mill Operations", 1, (0,0,0))
menu2 = opfont.render("Lathe Operations", 1, (0,0,0))
menu3 = opfont.render("Drill Operations", 1, (0,0,0))
menu4 = opfont.render("Exporting", 1, (0,0,0))
menu5 = opfont.render("Analysis", 1, (0,0,0))
#make menu an array for org





orgin=[width/2,height-height/2]





#Hard code mill and heat demo
for k in range (10, int(boundaryZ)):
    for j in range (0,int(boundaryY)):
        for i in range (0, int(boundaryX)):
            if j >= 0 and j <= 5:
                space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
            if j >= 10 and j <= 15:
                space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
            if j >= 20 and j <= 25:
                space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
            if j >= 30 and j <= 35:
                space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
            if j >= 40 and j <= 45:
                space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
            if j >= 50 and j <= 55:
                space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
alphasymbolthing = .0000177
thermalstep = .01
thermaltime = 100/ thermalstep
dxyz=.001/precision
maxtemp = 400
for t in range (0, int(50)):
    for k in range (-1, int(boundaryZ)+1):
        for j in range (0,int(boundaryY)):
            for i in range (0, int(boundaryX)):
                ospacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]            
    for k in range (0, int(boundaryZ)):
        for j in range (0,int(boundaryY)):
            for i in range (0, int(boundaryX)):
                #Temperture of own space, and surrounding spaces
                ot=spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]
                xn=ospacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i-1]
                xp=ospacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i+1]
                yn=ospacetemp[k*(boundaryY*boundaryX)+(j-1)*(boundaryX)+i]
                yp=ospacetemp[k*(boundaryY*boundaryX)+(j+1)*(boundaryX)+i]
                zn=ospacetemp[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i]
                zp=ospacetemp[(k+1)*(boundaryY*boundaryX)+j*(boundaryX)+i]

                if i==0:
                    xn=roomtemp
                if i==boundaryX:
                    xp=roomtemp
                if j==0:
                    yn=roomtemp
                if j==boundaryY:
                    yp=roomtemp
                if k==0:
                    bt=400
                if k==boundaryZ:
                    ft=roomtemp
                if zp > zn:
                    inter = zp
                    zp = zn
                    zn = inter
                            #This part was not my work
                if space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]==u"\u25A0":
                    spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i] = ot + alphasymbolthing*thermalstep*(      (((zp-ot)/(dxyz)-(zn-ot)/(dxyz))/dxyz)          )
                    if spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i] >= maxtemp:
                        maxtemp = spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]
                    if spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i] < 0:
                        spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i] = 0
                    #if spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i] > 400:
                    #    spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i] = 400
print()                    
                   
#print(pygame.font.get_fonts())
while (isopen==True):
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isopen = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                operation[0] = "Mill"
                print(operation[0])
            if event.key == pygame.K_l:
                operation[0] = "Lathe"
            if event.key == pygame.K_d:
                operation[0] = "Drill"
            if event.key == pygame.K_e:
                operation[0] = "Export"
            if event.key == pygame.K_z:
                operation[0] = 0
            if event.key == pygame.K_RIGHT:
                orgin[0]=orgin[0]+50
                regenerate = True
            if event.key == pygame.K_LEFT:
                orgin[0]=orgin[0]-50
                regenerate = True
            if event.key == pygame.K_UP:
                orgin[1]=orgin[1]-50
                regenerate = True
            if event.key == pygame.K_DOWN:
                orgin[1]=orgin[1]+50
                regenerate = True
            if event.key == pygame.K_p:
                scale = scale +1
                regenerate = True
            if event.key == pygame.K_o and scale > 0:
                scale = scale -1
                regenerate = True


#Color settings
    displaymode = 1
    spacetemp[int(39*(boundaryX*boundaryY)+(30)*(boundaryX))+30]=375
    spacetemp[int(39*(boundaryX*boundaryY)+(30)*(boundaryX))+31]=290
    if displaymode == 0:
        shading=[55,55,55]
        xshading=(shading[0]+10,shading[1],shading[2])
        yshading=(shading[0],shading[1]+10,shading[2])
        zshading=(shading[0],shading[1],shading[2]+10)

    while regenerate == True:
        mdisplay.fill(Background)            
        pygame.draw.rect(mdisplay, MenuRGB,((0,0), (width,100)))
        mdisplay.blit(menu1,(10,10))
        mdisplay.blit(menu2,(200,10))
        mdisplay.blit(menu3,(400,10))
        mdisplay.blit(menu4,(600,10))
        mdisplay.blit(menu5,(800,10))
        #Backgrounds to text and sidebar
        if operation[0] == 0:
            pygame.draw.rect(mdisplay, (0,0,0),((30,30), (30,30)))
            pygame.draw.rect(mdisplay, (0,0,0),((230,30), (30,30)))
            pygame.draw.rect(mdisplay, (0,0,0),((430,30), (30,30)))
            pygame.draw.rect(mdisplay, (0,0,0),((630,30), (30,30)))
            pygame.draw.rect(mdisplay, (0,0,0),((830,30), (30,30)))
            
        if operation[0] != 0:
            pygame.draw.rect(mdisplay, MenuRGB,((0,100), (200,height-100)))
            pygame.draw.rect(mdisplay,(0,0,0),((30,550), (30,30)))
        if operation[0] == "Mill":
            pygame.draw.rect(mdisplay, (255,255,255),(0,0), width=10,height=10)
        #if operation[0] == "Export":

        
        for k in range(0, int(boundaryZ)):
            for j in range(0, int(boundaryY)):
                for i in range(0, int(boundaryX)):
                    if space[int(k*(boundaryX*boundaryY)+j*(boundaryX))+i] == u"\u25A0":
                        if displaymode == 1:
                            if spacetemp[int(k*(boundaryX*boundaryY)+(j)*(boundaryX))+i] <= maxtemp/2:
                                xshading=(0+spacetemp[int(k*(boundaryX*boundaryY)+(j)*(boundaryX))+i]/(maxtemp/2)*255,255,0)
                                #print(0+spacetemp[int(k*(boundaryX*boundaryY)+(j)*(boundaryX))+i]/200*255)
                                yshading=xshading
                                zshading=yshading
                            if spacetemp[int(k*(boundaryX*boundaryY)+(j)*(boundaryX))+i] >= maxtemp/2:
                                xshading=(255,255-spacetemp[int(k*(boundaryX*boundaryY)+(j)*(boundaryX))+i]/(maxtemp/2)*255+255,0)
                                #print(255-spacetemp[int(k*(boundaryX*boundaryY)+(j)*(boundaryX))+i]/200*255+255)
                                yshading=xshading
                                zshading=yshading

                            
                        dx=(j-i)*scale+orgin[0]
                        dy=((i+j)/2-k)*scale+orgin[1]
                        hy=math.sqrt(scale**2+scale**2)
                        if i == boundaryX-1 or space[int(k*(boundaryX*boundaryY)+j*(boundaryX))+i+1 == u"\u25A0"]:
                            pygame.draw.polygon(mdisplay, xshading, ((dx,dy+hy),(dx,dy),(dx+math.cos(math.degrees(30))*hy,dy+math.sin(math.degrees(30))*hy),(dx+math.cos(math.degrees(30))*hy,dy+math.sin(math.degrees(30))*hy+hy))) #X+
                        if j == boundaryY-1 or space[int(k*(boundaryX*boundaryY)+(j+1)*(boundaryX))+i == u"\u25A0"]:
                            pygame.draw.polygon(mdisplay, yshading, ((dx,dy),(dx,dy+hy),(dx-math.cos(math.degrees(30))*hy,dy+math.sin(math.degrees(30))*hy+hy),(dx-math.cos(math.degrees(30))*hy,dy+math.sin(math.degrees(30))*hy))) #Y+
                        #pygame.draw.polygon(display, zshading, ((dx,dy),(dx-math.cos(math.degrees(30))*hy,dy+math.sin(math.degrees(30))*hy),(dx,dy-hy),(dx+math.cos(math.degrees(30))*hy,dy+math.sin(math.degrees(30))*hy))) #Z-
                        if k == boundaryZ-1 or space[int((k+1)*(boundaryX*boundaryY)+j*(boundaryX))+i == u"\u25A0"]:
                            pygame.draw.polygon(mdisplay, zshading, ((dx,dy),(dx-math.cos(math.degrees(30))*hy,dy+math.sin(math.degrees(30))*hy),(dx,dy-math.cos(math.degrees(60))*scale*2),(dx+math.cos(math.degrees(30))*hy,dy+math.sin(math.degrees(30))*hy))) #Z+
        regenerate = False
                        
    #for k in range(0, int(boundaryZ)*precision):
        #for j in range(0, int(boundaryY)*precision):
            #for i in range(0, int(boundaryX)*precision):
                #dx=(j-i)*scale+orgin[0]
                #dy=((i+j)/2-k)*scale+orgin[1]
                #hy=math.sqrt(scale**2+scale**2)
                #pygame.draw.circle(mdisplay, (255,0,0), (dx,dy), 2)
    pygame.draw.circle(mdisplay, (255,0,0), (orgin), 2)
    pygame.draw.line(mdisplay, (255,0,0), (orgin), (orgin[0]+math.cos(math.degrees(30))*(boundaryX*scale),orgin[1]-math.sin(math.degrees(30))*(boundaryX*scale))  )
    pygame.draw.line(mdisplay, (0,255,0), (orgin), (orgin[0]-math.cos(math.degrees(30))*(boundaryX*scale),orgin[1]-math.sin(math.degrees(30))*(boundaryX*scale))  )
    pygame.draw.line(mdisplay, (0,0,100), (orgin), (orgin[0],orgin[1]-boundaryZ*scale))
    pygame.display.update()







    if (mode=="StockOperations"):

        #command=input();
        command=1



                
                    
        #Export
        if (command == "E" or command == "e"):

            exportname = input('Enter File Name')
            exportname = exportname + ".stl"
            export = open(exportname, 'w');
            export.write(header + '\n');



            #Rounded Edges
            for k in range (0, int(boundaryZ)):
                for j in range (0,int(boundaryY)):
                    for i in range (0, int(boundaryX)):            
                         if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A2"):
                             h=1


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
                            theVs[0]=compressor[0]/precision
                            theVs[1]=j/precision+1/precision
                            theVs[2]=k/precision

                            theVs[3]=compressor[1]/precision
                            theVs[4]=j/precision
                            theVs[5]=k/precision

                            theVs[6]=compressor[0]/precision
                            theVs[7]=j/precision
                            theVs[8]=k/precision
                            #Triangle RealAft2
                            theVs[9]=compressor[1]/precision
                            theVs[10]=j/precision
                            theVs[11]=k/precision

                            theVs[12]=compressor[0]/precision
                            theVs[13]=j/precision+1/precision
                            theVs[14]=k/precision

                            theVs[15]=compressor[1]/precision
                            theVs[16]=j/precision+1/precision
                            theVs[17]=k/precision
                            
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
                            theVs[0]=compressor[2]/precision
                            theVs[1]=j/precision+1/precision
                            theVs[2]=k/precision+1/precision

                            theVs[3]=compressor[2]/precision
                            theVs[4]=j/precision
                            theVs[5]=k/precision+1/precision
                            
                            theVs[6]=compressor[3]/precision
                            theVs[7]=j/precision
                            theVs[8]=k/precision+1/precision
                            
                            #Triangle RealFront2
                            theVs[9]=compressor[2]/precision
                            theVs[10]=j/precision+1/precision
                            theVs[11]=k/precision+1/precision
                            
                            theVs[12]=compressor[3]/precision
                            theVs[13]=j/precision
                            theVs[14]=k/precision+1/precision

                            theVs[15]=compressor[3]/precision
                            theVs[16]=j/precision+1/precision
                            theVs[17]=k/precision+1/precision
                            
                            points()
                                
                            compressor[2]=-1
                            compressor[3]=-1


        #Going to have two more of these loops for the time being, for left right, and top down
            for k in range (0, int(boundaryY)):
                for j in range (0,int(boundaryX)):
                    compressor[0] = -1
                    compressor[1] = -1
                    compressor[2] = -1
                    compressor[3] = -1
                    for i in range (0, int(boundaryZ)):
                        #if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0" and space[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i] != u"\u25A0" and compressor[0] == -1):
                            #compressor[0]=i
                        #if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0" and (space[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] == u"\u25A0" or space[(k)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] != u"\u25A0" or i==boundaryX-1) and compressor[0] != -1 and compressor[1] == -1):
                            #compressor[1]=i+1
                        if compressor[0] != -1 and compressor[1] != -1:
                            #Triangle RealBottom1
                            theVs[0]=compressor[0]/precision
                            theVs[1]=j/precision+1/precision
                            theVs[2]=k/precision

                            theVs[3]=compressor[1]/precision
                            theVs[4]=j/precision
                            theVs[5]=k/precision

                            theVs[6]=compressor[0]/precision
                            theVs[7]=j/precision
                            theVs[8]=k/precision
                            #Triangle RealBottom2
                            theVs[9]=compressor[1]/precision
                            theVs[10]=j/precision
                            theVs[11]=k/precision

                            theVs[12]=compressor[0]/precision
                            theVs[13]=j/precision+1/precision
                            theVs[14]=k/precision

                            theVs[15]=compressor[1]/precision
                            theVs[16]=j/precision+1/precision
                            theVs[17]=k/precision
                            
                            #points()

                            compressor[0]=-1
                            compressor[1]=-1

                        #Front
                        #if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0" and space[(k+1)*(boundaryY*boundaryX)+j*(boundaryX)+i] != u"\u25A0" and compressor[2] == -1):
                            #compressor[2]=i
                        #if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0" and (space[(k+1)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] == u"\u25A0" or space[(k)*(boundaryY*boundaryX)+j*(boundaryX)+i+1] != u"\u25A0" or i==boundaryX-1) and compressor[2] != -1 and compressor[3] == -1):
                            #compressor[3]=i+1
                        if compressor[2] != -1 and compressor[3] != -1:
                            #Triangle RealTop1
                            theVs[0]=compressor[2]/precision
                            theVs[1]=j/precision+1/precision
                            theVs[2]=k/precision+1/precision

                            theVs[3]=compressor[2]/precision
                            theVs[4]=j/precision
                            theVs[5]=k/precision+1/precision
                            
                            theVs[6]=compressor[3]/precision
                            theVs[7]=j/precision
                            theVs[8]=k/precision+1/precision
                            
                            #Triangle Top2
                            theVs[9]=compressor[2]/precision
                            theVs[10]=j/precision+1/precision
                            theVs[11]=k/precision+1/precision
                            
                            theVs[12]=compressor[3]/precision
                            theVs[13]=j/precision
                            theVs[14]=k/precision+1/precision

                            theVs[15]=compressor[3]/precision
                            theVs[16]=j/precision+1/precision
                            theVs[17]=k/precision+1/precision
                            
                            #points()
                                
                            compressor[2]=-1
                            compressor[3]=-1


                        
                                                
            for k in range (0, int(boundaryZ)):
                for j in range (0,int(boundaryY)):
                    for i in range (0, int(boundaryX)):
                        if (space[k*(boundaryY*boundaryX)+j*(boundaryX)+i] == u"\u25A0"):
                            
                            if (space[(k)*(boundaryY*boundaryX)+(j)*(boundaryX)+i-1] == u"\u25A1" or i == 0):
                                #Triangle L1
                                theVs[0]=i/precision
                                theVs[1]=j/precision
                                theVs[2]=k/precision+1/precision

                                theVs[3]=i/precision
                                theVs[4]=j/precision+1/precision
                                theVs[5]=k/precision+1/precision

                                theVs[6]=i/precision
                                theVs[7]=j/precision
                                theVs[8]=k/precision
                                #Triangle L2
                                theVs[9]=i/precision
                                theVs[10]=j/precision
                                theVs[11]=k/precision

                                theVs[12]=i/precision
                                theVs[13]=j/precision+1/precision
                                theVs[14]=k/precision+1/precision

                                theVs[15]=i/precision
                                theVs[16]=j/precision+1/precision
                                theVs[17]=k/precision

                                points()

                            if (space[(k)*(boundaryY*boundaryX)+(j)*(boundaryX)+i+1] == u"\u25A1"  or i == boundaryX-1):
                                #Triangle R1
                                theVs[0]=i/precision+1/precision
                                theVs[1]=j/precision
                                theVs[2]=k/precision

                                theVs[3]=i/precision+1/precision
                                theVs[4]=j/precision+1/precision
                                theVs[5]=k/precision+1/precision

                                theVs[6]=i/precision+1/precision
                                theVs[7]=j/precision
                                theVs[8]=k/precision+1/precision
                                #Triangle R2
                                theVs[9]=i/precision+1/precision
                                theVs[10]=j/precision+1/precision
                                theVs[11]=k/precision

                                theVs[12]=i/precision+1/precision
                                theVs[13]=j/precision+1/precision
                                theVs[14]=k/precision+1/precision

                                theVs[15]=i/precision+1/precision
                                theVs[16]=j/precision
                                theVs[17]=k/precision

                                points()
                                
                            if (space[(k)*(boundaryY*boundaryX)+(j-1)*(boundaryX)+i] == u"\u25A1"  or j == 0):
                                #Triangle Top1
                                theVs[0]=i/precision+1/precision
                                theVs[1]=j/precision
                                theVs[2]=k/precision+1/precision

                                theVs[3]=i/precision
                                theVs[4]=j/precision
                                theVs[5]=k/precision+1/precision

                                theVs[6]=i/precision+1/precision
                                theVs[7]=j/precision
                                theVs[8]=k/precision
                                #Triangle Top2
                                theVs[9]=i/precision+1/precision
                                theVs[10]=j/precision
                                theVs[11]=k/precision

                                theVs[12]=i/precision
                                theVs[13]=j/precision
                                theVs[14]=k/precision+1/precision

                                theVs[15]=i/precision
                                theVs[16]=j/precision
                                theVs[17]=k/precision

                                points()

                            if (space[(k)*(boundaryY*boundaryX)+(j+1)*(boundaryX)+i] == u"\u25A1"  or j == boundaryY-1):
                                #Triangle Bottom1
                                theVs[0]=i/precision+1/precision
                                theVs[1]=j/precision+1/precision
                                theVs[2]=k/precision

                                theVs[3]=i/precision
                                theVs[4]=j/precision+1/precision
                                theVs[5]=k/precision+1/precision

                                theVs[6]=i/precision+1/precision
                                theVs[7]=j/precision+1/precision
                                theVs[8]=k/precision+1/precision
                                #Triangle Bottom2
                                theVs[9]=i/precision
                                theVs[10]=j/precision+1/precision
                                theVs[11]=k/precision

                                theVs[12]=i/precision
                                theVs[13]=j/precision+1/precision
                                theVs[14]=k/precision+1/precision

                                theVs[15]=i/precision+1/precision
                                theVs[16]=j/precision+1/precision
                                theVs[17]=k/precision

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
        thermaltime = 100/ thermalstep
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

            for t in range (0, int(20)):
                for k in range (-1, int(boundaryZ)+1):
                    for j in range (0,int(boundaryY)):
                        for i in range (0, int(boundaryX)):
                            ospacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]=spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]

                            
                for k in range (0, int(boundaryZ)):
                    for j in range (0,int(boundaryY)):
                        for i in range (0, int(boundaryX)):
                            #Temperture of own space, and surrounding spaces
                            ot=spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i]
                            lt=ospacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i-1]
                            rt=ospacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i+1]
                            dt=ospacetemp[k*(boundaryY*boundaryX)+(j-1)*(boundaryX)+i]
                            tt=ospacetemp[k*(boundaryY*boundaryX)+(j+1)*(boundaryX)+i]
                            bt=ospacetemp[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i]
                            ft=ospacetemp[(k-1)*(boundaryY*boundaryX)+j*(boundaryX)+i]

                            if spacetemp[i==0]:
                                lt=roomtemp
                            if spacetemp[i==boundaryX]:
                                rt=roomtemp
                            if spacetemp[j==0]:
                                dt=roomtemp
                            if spacetemp[j==boundaryY]:
                                tt=400
                            if spacetemp[k==0]:
                                bt=roomtemp
                            if spacetemp[k==boundaryZ]:
                                ft=roomtemp
                            #This part was not my work
                            if k*(boundaryY*boundaryX)+j*(boundaryX)+i == 0:
                                print(ot)
                                print(alphasymbolthing)
                                print(thermalstep)
                                print(rt)
                                print(tt)
                            if space[k*(boundaryY*boundaryX)+j*(boundaryX)+i]==u"\u25A0":
                                spacetemp[k*(boundaryY*boundaryX)+j*(boundaryX)+i] = ot + alphasymbolthing*thermalstep*(      (((rt-ot)/(dxyz)-(lt-ot)/(dxyz))/dxyz)+(((dt-ot)/(dxyz)-(tt-ot)/(dxyz))/dxyz) +(((bt-ot)/(dxyz)-(ft-ot)/(dxyz))/dxyz)              )
            
        if (command == "H" or command == "h"):
            for k in range(0, int(boundaryZ)):
                print("");
                print("Layer ", k+1);
                for j in range(0, int(boundaryY)):
                    for i in range(0, int(boundaryX)):
                        print(spacetemp[   int(k*(boundaryX*boundaryY)+(j)*(boundaryX))+i     ], "" ,end = ""); #boundaryY-1- before j to swap y axis

                        
                    print("")
