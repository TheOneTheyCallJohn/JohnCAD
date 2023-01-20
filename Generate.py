import tkinter as tk
def generate():
    def sm():
        global stock
        stock= "SheetMetal"
    def bs():
        global stock
        stock= "BarStock"
    def rs():
        global stock
        stock= "RoundStock"
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



    genWindow = tk.Tk()


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
            
    tk.Label(genWindow, text="Dimensions:").grid(row=4, column=0)
    tk.Label(genWindow, text="Width X").grid(row=5, column=0)
    tk.Label(genWindow, text="Length Y").grid(row=6, column=0)
    tk.Label(genWindow, text="Height Z").grid(row=7, column=0)

    tk.Entry(genWindow, textvariable = x).grid(row=5,column=1)
    tk.Entry(genWindow, textvariable = y).grid(row=6,column=1)
    tk.Entry(genWindow, textvariable = z).grid(row=7,column=1)

    tk.Button(genWindow, text="Generate!", command = gen).grid(row=8, column=0)
    genWindow.mainloop()