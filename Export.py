def export():
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
                    theVs[0]=compressor[0]/percision
                    theVs[1]=j/percision+1/percision
                    theVs[2]=k/percision

                    theVs[3]=compressor[1]/percision
                    theVs[4]=j/percision
                    theVs[5]=k/percision

                    theVs[6]=compressor[0]/percision
                    theVs[7]=j/percision
                    theVs[8]=k/percision
                    #Triangle RealBottom2
                    theVs[9]=compressor[1]/percision
                    theVs[10]=j/percision
                    theVs[11]=k/percision

                    theVs[12]=compressor[0]/percision
                    theVs[13]=j/percision+1/percision
                    theVs[14]=k/percision

                    theVs[15]=compressor[1]/percision
                    theVs[16]=j/percision+1/percision
                    theVs[17]=k/percision
                    
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
                    theVs[0]=compressor[2]/percision
                    theVs[1]=j/percision+1/percision
                    theVs[2]=k/percision+1/percision

                    theVs[3]=compressor[2]/percision
                    theVs[4]=j/percision
                    theVs[5]=k/percision+1/percision
                    
                    theVs[6]=compressor[3]/percision
                    theVs[7]=j/percision
                    theVs[8]=k/percision+1/percision
                    
                    #Triangle Top2
                    theVs[9]=compressor[2]/percision
                    theVs[10]=j/percision+1/percision
                    theVs[11]=k/percision+1/percision
                    
                    theVs[12]=compressor[3]/percision
                    theVs[13]=j/percision
                    theVs[14]=k/percision+1/percision

                    theVs[15]=compressor[3]/percision
                    theVs[16]=j/percision+1/percision
                    theVs[17]=k/percision+1/percision
                    
                    #points()
                        
                    compressor[2]=-1
                    compressor[3]=-1


                
                                        
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
