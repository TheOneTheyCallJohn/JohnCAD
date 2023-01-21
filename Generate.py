import tkinter as tk


def generate(data,x,y,z,stock,percision,space):
    genWindow = tk.Tk()
    labelx=tk.Label(genWindow, text="Width X")
    labely=tk.Label(genWindow, text="Length Y")
    labelz=tk.Label(genWindow, text="Height Z")
    entryx=tk.Entry(genWindow, textvariable = x)
    entryy=tk.Entry(genWindow, textvariable = y)
    entryz=tk.Entry(genWindow, textvariable = z)

    labeld=tk.Label(genWindow, text="Diameter X Y")
    entryd=tk.Entry(genWindow, textvariable = y)

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
        clear()
        labeld.grid(row=5, column=0)
        labelz.grid(row=6, column=0)
        labelb.grid(row=7, column=0)
        entryd.grid(row=5, column=1)
        entryz.grid(row=6, column=1)

    def p1():
        global percision
        percision = 1
    def p2():
        global percision
        percision = 10
    def p3():
        global percision
        percision = 100
    def size():
        data[0]=x
        data[1]=y
        data[2]=z
    def gen():
        genWindow.destroy()





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

    tk.Button(genWindow, text="Generate!", command = gen).grid(row=8, column=0)
    genWindow.mainloop()


    if (stock=="SheetMetal"):
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
        mode="SheetOperations"

    #RoundStockGeneration
    if (stock== "RoundStock"):
        print("Diameter, Length");
        print(data[0], 'mm' ,data[1], 'mm');
        command = input("Press Enter To Generate");
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
                        elif math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) > (data[0]*percision)/2 and math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) < (data[0]*percision)/2+.8:
                            space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A2";
                            
                        elif math.sqrt((i+.5-((boundaryX)/2))**2+(j+.5-((boundaryY)/2))**2) > (data[0]*percision)/2+.8:
                            space[(k)*(boundaryX*boundaryY)+(j)*(boundaryY)+i]=u"\u25A1";
            mode="StockOperations"   
    #Barstock deatils   
    if (stock=="BarStock"):
        mode = "StockOperations"
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
        mode="StockOperations"
