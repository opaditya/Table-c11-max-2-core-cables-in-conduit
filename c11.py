from tkinter import *

conduitType = ["Heavy duty rigid UPVC conduit", "Corflo conduit", 
"Medium duty corrugated", "Medium duty rigid UPVC conduit"]
CableType = ["-", "1.5", "2.5", "4" , "6" ,"10" ,'16', '25']
PVC_FLAT = ["-", '1', "1.5", "2.5", "4" , "6" ,"10" ,"16"]

class Application(Frame):

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.UserIn = IntVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self): 

        self.conduitLbl = Label (self, text = "Type of Conduit", height=2, width=20)#Label
        self.conduitLbl.grid(row=0, column = 0)

        self.conduit = StringVar(master) ### OPTION MENU FOR CONIOT TYPE
        self.conduit.set("Heavy duty rigid UPVC conduit") # default value
        self.conduitOptions = OptionMenu(master, self.conduit, *conduitType)
        self.conduitOptions.config(width=28)
        self.conduitOptions.grid(row=0, column=1)
        
        self.PVCLabel = Label (master, text = "PVC V90 & V75", height=2, width=20)#Label
        self.PVCLabel.grid(row=1, column = 0)
        
        self.PVC_flat = Label (master, text = "PVC V90 FLAT", height=2, width=20)#Label
        self.PVC_flat.grid(row=2, column = 0)

        self.cable = StringVar(master)
        self.cable.set("-") # default value
        self.PVCom = OptionMenu(master, self.cable, *CableType, )
        self.PVCom.config(width=15)
        self.PVCom.grid(row=1, column=1)

        self.cablePVC = StringVar(master)
        self.cablePVC.set("-") # default value
        self.PVCom = OptionMenu(master, self.cablePVC, *PVC_FLAT, )
        self.PVCom.config(width=15)
        self.PVCom.grid(row=2, column=1)

        self.circuitLbl = Label (master, text = "Number of Circuits:", height=1, width=20) #Label
        self.circuitLbl.grid(row=3, column = 0)

        self.getCircuit = IntVar()  
        self.getCircuit = Entry (master) ######## ENTRY BOX

        self.getCircuit.grid(row=3, column=1)        
            
        self.btn = Button(master, text="Calculate", bg="light grey", command=self.onButtonClick)
        self.btn.grid(row = 4,column=1)           

        self.conduitTypeResult = Label (master, text = "Conduit Type-> ", height=1, width=40) #Label
        self.conduitTypeResult.grid(row=0, column =2) 

        self.PVCResult = Label (master, text = "Cable Type-> ", height=2, width=25) #Label
        self.PVCResult.grid(row=1, column =2)    

        self.XLPE = Label (master, text = "", height=2, width=25) #Label
        self.XLPE.grid(row=2, column =2)  

        self.circuitNo = Label (master, text = "Number of Circuits-> ", height=2, width=25) #Label
        self.circuitNo.grid(row=3, column =2)   

        self.conduitResult = Label (master, text = "-", height=2, width=40, font='Helvetica 9 bold') #Label
        self.conduitResult.grid(row=4, column =2)    

        self.close = Button(master, text="Close", bg="light grey", command=master.destroy)
        self.close.grid(row = 5,column=0) 

        def openImage():
            control = Toplevel()
            canvas = Canvas(control, width=1101, height=595)
            canvas.pack(expand = YES, fill = BOTH)
            png1 = PhotoImage(file='C:\\Users\\Aditya.Verma\\Documents\\GitHub\\Table-c11-max-2-core-cables-in-conduit\\Capture.PNG')
            canvas.create_image(0, 0, image = png1, anchor = NW)
            canvas.png1 = png1

        self.canvas = Canvas(master, width=99, height=30)
        self.canvas.grid(row=5, column=2)
        self.logo = PhotoImage(file='C:\\Users\\Aditya.Verma\\Documents\\GitHub\\Table-c10---max-single-core-sheathed-cables\\Lucid Logo.PNG')
        self.canvas.create_image(0, 0, image = self.logo, anchor = NW)
        self.canvas.logo = self.logo   

        self.openImage = Button(master, text="Open Table", bg="light grey", command=openImage) #image open button
        self.openImage.grid(row=5, column = 1)

        self.disclaimerText = Label (master, text = """DISCLAIMER\n Please refer to the Table (can be accessed by clicking Open Table button)
         to confirm the results before practically applying the Number Of Conduits. Each output has not been tested thus 
         caution should be taken when using this program.\n
         REFERENCE: AS/NZ 3000:2018 Electrical Installations (known as the Australian/New Zeealand Wiring Rules"""
        ,font='Helvetica 9 bold') #Label
        self.disclaimerText.grid(row=6, rowspan=2, column=0, columnspan=3, sticky=W)    
        
        def reset():
             self.PVCResult.configure(text="" )
             self.conduitTypeResult.configure(text="-" )
             self.PVCResult.configure(text="-" )
             self.conduit.set("Heavy duty rigid UPVC conduit")
             self.cable.set("-")

        self.tableview = Button(master, text="Reset", bg="light grey", command=reset)
        self.tableview.grid(row = 4,column=0) 

        def toogle_state(*_):
            if self.getCircuit.get():
                btn['state']='normal'    
            else:
                btn['state']='disabled'
    def onButtonClick(self):
        
        #get values
        def getConduitType(self):
            self.x = self.conduit.get()
            return self.x
        def getCable(self):
            self.x = self.cable.get()
            return self.x   
        def getPVC_FLAT(self):
            self.x = self.cablePVC.get()
            return self.x          
        def getCircuitState(self):
            self.x = self.getCircuit.get()          
            return int(self.x) 

        if not self.getCircuit.get() or self.cable.get():
            self.conduitResult.configure(text="No. of Circuits has not been selected ", bg='orange' )      
        self.conduitTypeResult.configure(text="Conduit Type:  " + self.conduit.get(), font='Helvetica 9 bold')      
        
        if (getCable(self)=="-"):
            self.PVCResult.configure(text="" + self.cable.get(),font='Helvetica 9 bold' )
        else:
            self.PVCResult.configure(text="Cable Type:  " + self.cable.get(),font='Helvetica 9 bold' )

        if (getPVC_FLAT(self)=="-"):
            self.XLPE.configure(text="" + self.cablePVC.get(),font='Helvetica 9 bold' )
        else:
            self.XLPE.configure(text="Cable Type:  " + self.cablePVC.get(),font='Helvetica 9 bold' ) 
        
        self.circuitNo.configure(text="Number of Circuits:  "+ self.getCircuit.get(), font='Helvetica 9 bold')

        # file = open("Data.txt","a+")
        # file.write(str(getCable(self)))
        # file.write("test")
        # file.write(str(getPVC_FLAT(self)))
        # file.write(str(getCircuitState(self)))
        # # file.write(str(circuitNo(self)))
        # file.close()
        def circuitNo(self):

            if (getConduitType(self)=="Heavy duty rigid UPVC conduit"):

                if(getCable(self)=="1.5" and getCircuitState(self)<= int("1")):
                    return "20 or 25"
                
                if((getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self) <= int("1")):
                    return "25 or 32"
                
                if((getCable(self)=="2.5" or getCable(self)=="4" or getCable(self)=="6")  and getCircuitState(self) <= int("0")):
                    return "20"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("2")):
                    return "32"
                
                if((getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self) <= int("2")):
                    return "40"
                
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("3")):
                    return "40"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("4")):
                    return "40"
                
                if((getCable(self)=="4" or getCable(self)=="6") and getCircuitState(self) <= int("4")):
                    return "50"
                
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("5")):
                    return "50"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("7")):
                    return "50"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("11")):
                    return "63"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("9")):
                    return "63"
                if(getCable(self)=="4" and getCircuitState(self) <= int("7")):
                    return "63"
                if(getCable(self)=="6" and getCircuitState(self) <= int("6")):
                    return "63"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("21")):
                    return "80 (NZ)"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("9")):
                    return "80 (NZ)"
                if(getCable(self)=="4" and getCircuitState(self) <= int("7")):
                    return "80 (NZ)"
                if(getCable(self)=="6" and getCircuitState(self) <= int("6")):
                    return "80 (NZ)"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("24")):
                    return "80 (AUS)"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("16")):
                    return "80 (AUS)"
                if(getCable(self)=="4" and getCircuitState(self) <= int("13")):
                    return "80 (AUS)"
                if(getCable(self)=="6" and getCircuitState(self) <= int("12")):
                    return "80 (AUS)"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("38")):
                    return "100 (NZ)"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("30")):
                    return "100 (NZ)"
                if(getCable(self)=="4" and getCircuitState(self) <= int("23")):
                    return "100 (NZ)"
                if(getCable(self)=="6" and getCircuitState(self) <= int("21")):
                    return "100 (NZ)"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("41")):
                    return "100 (AUS)"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("32")):
                    return "100 (AUS)"
                if(getCable(self)=="4" and getCircuitState(self) <= int("25")):
                    return "100 (AUS)"
                if(getCable(self)=="6" and getCircuitState(self) <= int("21")):
                    return "100 (AUS)"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("62")):
                    return "125"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("48")):
                    return "125"
                if(getCable(self)=="4" and getCircuitState(self) <= int("38")):
                    return "125"
                if(getCable(self)=="6" and getCircuitState(self) <= int("34")):
                    return "125"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("81")):
                    return "150"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("63")):
                    return "150"
                if(getCable(self)=="4" and getCircuitState(self) <= int("50")):
                    return "150"
                if(getCable(self)=="6" and getCircuitState(self) <= int("45")):
                    return "150"

                if((getCable(self)=="10" or getCable(self)=="16" or getCable(self)=="25") and getCircuitState(self) == int("0")):
                    return "20 or 25"
                
                if((getCable(self)=="10" or getCable(self)=="16") and getCircuitState(self) <= int("1")):
                    return "32 or 40"
                
                if(getCable(self)=='25' and getCircuitState(self) <= int("0")):
                    return "32"
                
                if(getCable(self)=='50' and getCircuitState(self) <= int("1")):
                    return "50"
                
                if(getCable(self)=="25"  and getCircuitState(self) <= int("1")):
                    return "40 pr 50"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("2")):
                    return "50"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("4")):
                    return "63"
                if(getCable(self)=='16' and getCircuitState(self) <= int("3")):
                    return "63"
                if(getCable(self)=='25' and getCircuitState(self) <= int("2")):
                    return "63"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("7")):
                    return "80 (NZ)"
                if(getCable(self)=='16' and getCircuitState(self) <= int("6")):
                    return "80 (NZ)"
                if(getCable(self)=='25' and getCircuitState(self) <= int("4")):
                    return "80 (NZ)"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("9")):
                    return "80 (AUS)"
                if(getCable(self)=='16' and getCircuitState(self) <= int("7")):
                    return "80 (AUS)"
                if(getCable(self)=='25' and getCircuitState(self) <= int("5")):
                    return "80 (AUS)"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("13")):
                    return "100 (NZ)"
                if(getCable(self)=='16' and getCircuitState(self) <= int("11")):
                    return "100 (NZ)"
                if(getCable(self)=='25' and getCircuitState(self) <= int("7")):
                    return "100 (NZ)"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("15")):
                    return "100 (AUS)"
                if(getCable(self)=='16' and getCircuitState(self) <= int("11")):
                    return "100 (AUS)"
                if(getCable(self)=='25' and getCircuitState(self) <= int("8")):
                    return "100 (AUS)"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("22")):
                    return "125"
                if(getCable(self)=='16' and getCircuitState(self) <= int("18")):
                    return "125"
                if(getCable(self)=='25' and getCircuitState(self) <= int("12")):
                    return "125"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("29")):
                    return "150"
                if(getCable(self)=='16' and getCircuitState(self) <= int("23")):
                    return "150"
                if(getCable(self)=='25' and getCircuitState(self) <= int("16")):
                    return "150"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("1")):
                    return "20"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("1")):
                    return "20"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("1")):
                    return "20"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("1")):
                    return "20"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("0")):
                    return "20"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("0")):
                    return "20"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("0")):
                    return "20"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("2")):
                    return "25"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("2")):
                    return "25"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("1")):
                    return "25"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("1")):
                    return "25"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("1")):
                    return "25"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("1")):
                    return "25"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("0")):
                    return "25"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("5")):
                    return "32"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("5")):
                    return "32"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("3")):
                    return "32"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("2")):
                    return "32"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("1")):
                    return "32"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("1")):
                    return "32"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("1")):
                    return "32"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("8")):
                    return "40"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("8")):
                    return "40"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("5")):
                    return "40"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("4")):
                    return "40"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("3")):
                    return "40"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("2")):
                    return "40"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("1")):
                    return "40"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("14")):
                    return "50"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("13")):
                    return "50"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("9")):
                    return "50"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("6")):
                    return "50"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("5")):
                    return "50"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("4")):
                    return "50"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("2")):
                    return "50"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("23")):
                    return "63"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("22")):
                    return "63"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("15")):
                    return "63"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("11")):
                    return "63"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("9")):
                    return "63"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("7")):
                    return "63"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("4")):
                    return "63"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("42")):
                    return "80 (NZ)"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("40")):
                    return "80 (NZ)"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("28")):
                    return "80 (NZ)"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("20")):
                    return "80 (NZ)"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("17")):
                    return "80 (NZ)"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("12")):
                    return "80 (NZ)"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("8")):
                    return "80 (NZ)"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("48")):
                    return "80 (AUS)"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("46")):
                    return "80 (AUS)"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("32")):
                    return "80 (AUS)"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("23")):
                    return "80 (AUS)"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("19")):
                    return "80 (AUS)"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("14")):
                    return "80 (AUS)"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("9")):
                    return "80 (AUS)"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("75")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("71")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("52")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("36")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("30")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("22")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("14")):
                    return "100 (NZ)"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("81")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("77")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("54")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("38")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("32")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("24")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("15")):
                    return "100 (AUS)"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) >= int("100")):
                    return "125"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) >= int("100")):
                    return "125"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("81")):
                    return "125"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("58")):
                    return "125"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("49")):
                    return "125"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("36")):
                    return "125"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("23")):
                    return "125"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) >= int("100")):
                    return "150"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) >= int("100")):
                    return "150"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) >= int("100")):
                    return "150"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("76")):
                    return "150"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("64")):
                    return "150"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("47")):
                    return "150"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("31")):
                    return "150"

        
            if (getConduitType(self)=="Corflo conduit"):

                if(getCable(self)=="1.5" and getCircuitState(self) <= int("38")):
                    return "100 (NZ)"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("30")):
                    return "100 (NZ)"
                if(getCable(self)=="4" and getCircuitState(self) <= int("23")):
                    return "100 (NZ)"
                if(getCable(self)=="6" and getCircuitState(self) <= int("21")):
                    return "100 (NZ)"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("40")):
                    return "100 (AUS)"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("31")):
                    return "100 (AUS)"
                if(getCable(self)=="4" and getCircuitState(self) <= int("24")):
                    return "100 (AUS)"
                if(getCable(self)=="6" and getCircuitState(self) <= int("22")):
                    return "100 (AUS)"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("59")):
                    return "125"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("46")):
                    return "125"
                if(getCable(self)=="4" and getCircuitState(self) <= int("36")):
                    return "125"
                if(getCable(self)=="6" and getCircuitState(self) <= int("33")):
                    return "125"
                
                if(getCable(self)=="1.5" and getCircuitState(self) <= int("78")):
                    return "150"
                if(getCable(self)=="2.5" and getCircuitState(self) <= int("61")):
                    return "150"
                if(getCable(self)=="4" and getCircuitState(self) <= int("48")):
                    return "150"
                if(getCable(self)=="6" and getCircuitState(self) <= int("43")):
                    return "150"

                if(getCable(self)=='10' and getCircuitState(self) <= int("13")):
                    return "100 (NZ)"
                if(getCable(self)=='16' and getCircuitState(self) <= int("11")):
                    return "100 (NZ)"
                if(getCable(self)=='25' and getCircuitState(self) <= int("7")):
                    return "100 (NZ)"

                if(getCable(self)=='10' and getCircuitState(self) <= int("14")):
                    return "100 (AUS)"
                if(getCable(self)=='16' and getCircuitState(self) <= int("11")):
                    return "100 (AUS)"
                if(getCable(self)=='25' and getCircuitState(self) <= int("8")):
                    return "100 (AUS)"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("21")):
                    return "125"
                if(getCable(self)=='16' and getCircuitState(self) <= int("17")):
                    return "125"
                if(getCable(self)=='25' and getCircuitState(self) <= int("12")):
                    return "125"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("28")):
                    return "150"
                if(getCable(self)=='16' and getCircuitState(self) <= int("22")):
                    return "150"
                if(getCable(self)=='25' and getCircuitState(self) <= int("16")):
                    return "150"
                ##################################################### BREAK POINT
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("75")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("71")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("50")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("36")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("30")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("22")):
                    return "100 (NZ)"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("17")):
                    return "100 (NZ)"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("78")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("74")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("52")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("37")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("31")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("23")):
                    return "100 (AUS)"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("15")):
                    return "100 (AUS)"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) >= int("100")):
                    return "125"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) >= int("100")):
                    return "125"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("77")):
                    return "125"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("55")):
                    return "125"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("47")):
                    return "125"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("34")):
                    return "125"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("22")):
                    return "125"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) >= int("100")):
                    return "150"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) >= int("100")):
                    return "150"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) >= int("100")):
                    return "150"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("73")):
                    return "150"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("62")):
                    return "150"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("45")):
                    return "150"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("30")):
                    return "150"

            if (getConduitType(self)=="Medium duty corrugated"):
        
                if(getCable(self)=='10' and getCircuitState(self) <= int("7")):
                    return "80 (NZ)"
                if(getCable(self)=='16' and getCircuitState(self) <= int("6")):
                    return "80 (NZ)"
                if(getCable(self)=='25' and getCircuitState(self) <= int("4")):
                    return "80 (NZ)"

                if(getCable(self)=='10' and getCircuitState(self) <= int("7")):
                    return "80 (NZ)"
                if(getCable(self)=='16' and getCircuitState(self) <= int("6")):
                    return "80 (NZ)"
                if(getCable(self)=='25' and getCircuitState(self) <= int("4")):
                    return "80 (NZ)"

                if((getCable(self)=='2.5' or getCable(self)=='4' or getCable(self)=='6') and getCircuitState(self) <= int("0")):
                    return "20"
                if(getCable(self)=='1.5' and getCircuitState(self) <= int("1")):
                    return "20"
                if((getCable(self)=='1.5' or getCable(self)=='2.5' or getCable(self)=='4') and getCircuitState(self) <= int("1")):
                    return "20 or 32"
                if(getCable(self)=='6' and getCircuitState(self) <= int("1")):
                    return "32 or 40"
                if(getCable(self)=='6' and getCircuitState(self) <= int("0")):
                    return "25"
                if((getCable(self)=='1.5' or getCable(self)=='2.5')and getCircuitState(self) <= int("3")):
                    return "40"
                if(getCable(self)=='4' and getCircuitState(self) <= int("2")):
                    return "40"

                if((getCable(self)=='10' or getCable(self)=='16' or getCable(self)=='25') and getCircuitState(self) <= int("0")):
                    return "20 or 25"
                if((getCable(self)=='16' or getCable(self)=='25') and getCircuitState(self) <= int("0")):
                    return "32"
                if(getCable(self)=='25' and getCircuitState(self) <= int("4")):
                    return "80 (NZ)"
                if(getCable(self)=='20' and getCircuitState(self) <= int("1")):
                    return "32"
                if((getCable(self)=='10' or getCable(self)=='16' or getCable(self)=='25') and getCircuitState(self) <= int("1")):
                    return "32"
        
                if((getPVC_FLAT(self)=='1' or getPVC_FLAT(self)=='2.5' or getPVC_FLAT(self)=='1.5') and getCircuitState(self) >= int("1")):
                    return "20"
                if((getPVC_FLAT(self)=='4' or getPVC_FLAT(self)=='6' or getPVC_FLAT(self)=='10' or getPVC_FLAT(self)=='16')
                 and getCircuitState(self) <= int("0")):
                    return "20"
                if((getPVC_FLAT(self)=='2.5' or getPVC_FLAT(self)=='4' or getPVC_FLAT(self)=='6' or getPVC_FLAT(self)=='10') and getCircuitState(self) <= int("1")):
                    return "25"
                if((getPVC_FLAT(self)=='1' or getPVC_FLAT(self)=='1.5') and getCircuitState(self) <= int("2")):
                    return "25"
                if(getPVC_FLAT(self)=='16'and getCircuitState(self) <= int("0")):
                    return "25"
                
                if((getPVC_FLAT(self)=='1' or getPVC_FLAT(self)=='1.5') and getCircuitState(self) <= int("4")):
                    return "32"
                if(getPVC_FLAT(self)=='2.5'and getCircuitState(self) <= int("3")):
                    return "32"
                if((getPVC_FLAT(self)=='4' or getPVC_FLAT(self)=='6' or getPVC_FLAT(self)=='10' or getPVC_FLAT(self)=='16') and getCircuitState(self) <= int("1")):
                    return "32"
                
                if((getPVC_FLAT(self)=='1' or getPVC_FLAT(self)=='1.5') and getCircuitState(self) <= int("7")):
                    return "40"
                if(getPVC_FLAT(self)=='2.5'and getCircuitState(self) <= int("5")):
                    return "40"
                if(getPVC_FLAT(self)=='4' or getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("3")):
                    return "40"
                if((getPVC_FLAT(self)=='10' or getPVC_FLAT(self)=='16') and getCircuitState(self) <= int("1")):
                    return "40"    
            if (getConduitType(self)=="Medium duty rigid UPVC conduit"):
                if((getCable(self)=='1.5' or getCable(self)=='2.5' or getCable(self)=='4' or getCable(self)=='4') and getCircuitState(self) <= int("0")):
                    return "20"

                if((getCable(self)=='1.5' or getCable(self)=='2.5') and getCircuitState(self) <= int("1")):
                    return "20 or 25"
                
                if((getCable(self)=='4' or getCable(self)=='6') and getCircuitState(self) <= int("1")):
                    return "25 or 32"
                
                if((getCable(self)=='4' or getCable(self)=='6') and getCircuitState(self) <= int("0")):
                    return "20"
                
                if(getCable(self)=='2.5' and getCircuitState(self) <= int("1")):
                    return "32"
                
                if(getCable(self)=='1.5' and getCircuitState(self) <= int("2")):
                    return "32"
                
                if(getCable(self)=='2.5' and getCircuitState(self) <= int("3")):
                    return "40"
                
                if(getCable(self)=='1.5' and getCircuitState(self) <= int("4")):
                    return "40"
                
                if(getCable(self)=='1.5' and getCircuitState(self) <= int("7")):
                    return "50"

                if(getCable(self)=='2.5' and getCircuitState(self) <= int("6")):
                    return "50"

                if((getCable(self)=='4' or getCable(self)=='6') and getCircuitState(self) <= int("2")):
                    return "40"
                if((getCable(self)=='4' or getCable(self)=='6') and getCircuitState(self) <= int("4")):
                    return "50"
                
                if((getCable(self)=='10' or getCable(self)=='16' or getCable(self)=='25') and getCircuitState(self) <= int("0")):
                    return "16, 20 or 25"
                if(getCable(self)=='25' and getCircuitState(self) <= int("0")):
                    return "32"
                
                if((getCable(self)=='10' or getCable(self)=='16') and getCircuitState(self) <= int("1")):
                    return "32 or 40"
                
                if(getCable(self)=='25' and getCircuitState(self) <= int("1")):
                    return "40 or 50"
                
                if(getCable(self)=='16' and getCircuitState(self) <= int("1")):
                    return "50"
                
                if(getCable(self)=='10' and getCircuitState(self) <= int("2")):
                    return "50"
                
                if((getPVC_FLAT(self)=='1' or getPVC_FLAT(self)=='1.5' or getPVC_FLAT(self)=='2.5') and getCircuitState(self) <= int("1")):
                    return "16 or 20"
                
                if((getPVC_FLAT(self)=='2.5' or getPVC_FLAT(self)=='4' or getPVC_FLAT(self)=='6') and getCircuitState(self) <= int("1")):
                    return "20 or 25"
                
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("0")):
                    return "16"
                
                if((getPVC_FLAT(self)=='10' or getPVC_FLAT(self)=='16') and getCircuitState(self) <= int("0")):
                    return "20"
                
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("0")):
                    return "25"
                
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("1")):
                    return "25 or 32"
                
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("1")):
                    return "32 or 40"
                
                if((getPVC_FLAT(self)=='1' or getPVC_FLAT(self)=='1.5') and getCircuitState(self) <= int("3")):
                    return "25"
                
                if((getPVC_FLAT(self)=='1' or getPVC_FLAT(self)=='1.5') and getCircuitState(self) <= int("5")):
                    return "32"
                
                if((getPVC_FLAT(self)=='1' or getPVC_FLAT(self)=='1.5') and getCircuitState(self) <= int("9")):
                    return "40"
                
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("3")):
                    return "32"
                
                if((getPVC_FLAT(self)=='4' or getPVC_FLAT(self)=='6') and getCircuitState(self) <= int("1")):
                    return "32"
                
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("6")):
                    return "40"
                
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("4")):
                    return "40"
                
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("3")):
                    return "40"
                
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("2")):
                    return "40"
                
                if(getPVC_FLAT(self)=='1' and getCircuitState(self) <= int("15")):
                    return "50"
                if(getPVC_FLAT(self)=='1.5' and getCircuitState(self) <= int("14")):
                    return "50"
                if(getPVC_FLAT(self)=='2.5' and getCircuitState(self) <= int("10")):
                    return "50"
                if(getPVC_FLAT(self)=='4' and getCircuitState(self) <= int("7")):
                    return "50"
                if(getPVC_FLAT(self)=='6' and getCircuitState(self) <= int("6")):
                    return "50"
                if(getPVC_FLAT(self)=='10' and getCircuitState(self) <= int("4")):
                    return "50"
                if(getPVC_FLAT(self)=='16' and getCircuitState(self) <= int("3")):
                    return "50"
            
            else:
                return "Invalid input, please check again"

        

        self.conduitResult.configure(text="Number of Conduits: \n" + circuitNo(self), bg='green2')
        if (circuitNo(self)=="Invalid input, please check again"):
            self.conduitResult.configure(bg='red')
         
master = Tk()
master.title("Number of Conduits. Table C11")
master.geometry("700x325")
app = Application(master)

master.mainloop()
