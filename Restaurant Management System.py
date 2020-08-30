from tkinter import*
import random
import time
import datetime
from tkinter import messagebox

root = Tk()
root.geometry("1400x1400+0+0")
root.title("Restaurant Management System")
root.configure(background='black')

heading=Frame(root, width=1350, height=100,relief="raise",bd=14)
heading.pack(side=TOP)
heading = Label(heading,font=( 'aria' ,62, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=14)
heading.grid(row=0,column=0)
#-----------------------------------------------FRAME-------------------------------------------------------------------------

bottomframe=Frame(root, width=1350, height=100,bd=14,relief="raise",bg="black")
bottomframe.pack(side=BOTTOM)

frame1=Frame(bottomframe, width=300, height=550, bd=14,relief="raise",bg="light yellow")
frame1.pack(side=LEFT)

frame2=Frame(bottomframe, width=300, height=550, bd=14,relief="raise",bg="light yellow")
frame2.pack(side=LEFT)

frame3=Frame(bottomframe, width=300, height=550, bd=14,relief="raise",bg="light yellow")
frame3.pack(side=LEFT)

frame4=Frame(bottomframe, width=400, height=550, bd=14,relief="raise",bg="light yellow")
frame4.pack(side=RIGHT)

#--------------------------------------------------------------------------
def qExit():
    qExit=messagebox.askyesno("Quit System","Do you want to exit?")
    if (qExit > 0):
        root.destroy()
        return
btnExit=Button(frame3,padx=25,pady=15,bd=10,fg="black",font=('arial',10,'bold'),text="Exit",command=qExit).place(x=1,y=250)
#-----------------------------------------------------------------------
#--------------------------------------------RESET FUNCTION---------------------------------------------------------------------------------
def qReset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostOfBeverages.set("")
    CostOfFoods.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    E_Burger.set("0")
    E_Pizza.set("0")
    E_Sandwich.set("0")
    E_Salad.set("0")

    E_Coffee.set("0")
    E_Tea.set("0")
    E_Mojita.set("0")
    E_Shake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
       

    txtBurger.configure(state="disabled")
    txtPizza.configure(state="disabled")
    txtSandwich.configure(state="disabled")
    txtSalad.configure(state="disabled")

    txtCoffee.configure(state="disabled")
    txtTea.configure(state="disabled")
    txtMojita.configure(state="disabled")
    txtShake.configure(state="disabled")


btnReset=Button(frame3,padx=15,pady=15,bd=10,fg="black",font=('arial',10,'bold'),text="Reset",command=qReset).place(x=150,y=350)

def chkButton():
    if(var1.get() ==1):
        txtBurger.configure(state="normal")
    elif(var1.get()==0):
        txtBurger.configure(state="disabled")
        E_Burger.set("0")
        
    if(var2.get() ==1):
        txtPizza.configure(state="normal")
    elif(var2.get()==0):
        txtPizza.configure(state="disabled")
        E_Pizza.set("0")

    if(var3.get() ==1):
        txtSandwich.configure(state="normal")
    elif(var3.get()==0):
        txtSandwich.configure(state="disabled")
        E_Sandwich.set("0")

    if(var4.get() ==1):
        txtSalad.configure(state="normal")
    elif(var4.get()==0):
        txtSalad.configure(state="disabled")
        E_Salad.set("0")

    if(var5.get() ==1):
        txtCoffee.configure(state="normal")
    elif(var5.get()==0):
        txtCoffee.configure(state="disabled")
        E_Coffee.set("0")

    if(var6.get() ==1):
        txtTea.configure(state="normal")
    elif(var6.get()==0):
        txtTea.configure(state="disabled")
        E_Tea.set("0")

    if(var7.get() ==1):
        txtMojita.configure(state="normal")
    elif(var7.get()==0):
        txtMojita.configure(state="disabled")
        E_Mojita.set("0")

    if(var8.get() ==1):
        txtShake.configure(state="normal")
    elif(var8.get()==0):
        txtShake.configure(state="disabled")
        E_Shake.set("0")


#-----------------------------------------------------------------------
def CostOfItem():
    Item1= float(E_Burger.get())
    Item2= float(E_Pizza.get())
    Item3= float(E_Sandwich.get())
    Item4= float(E_Salad.get())
    
    Item5= float(E_Coffee.get())
    Item6= float(E_Tea.get())
    Item7= float(E_Mojita.get())
    Item8= float(E_Shake.get())

    PriceOfBeverages=(Item1 * 10)+ (Item2 * 20)+ (Item3 * 30)+ (Item4 * 15)
    PriceOfFoods=(Item5 * 15)+ (Item6 * 20)+ (Item7 * 25)+ (Item8 * 40)

    BeveragesPrice=""+ str('%.2f'%(PriceOfBeverages))
    FoodsPrice=""+ str('%.2f'%(PriceOfFoods))

    CostOfBeverages.set(BeveragesPrice)
    CostOfFoods.set(FoodsPrice)

    SC = "" + str ('%.2f'%(1.59))
    ServiceCharge.set(SC)

    subTotal1 = "" + str('%2f'%(PriceOfBeverages + PriceOfFoods +1.59))
    SubTotal.set(subTotal1)

    Tax=  "" + str('%2f'%((PriceOfBeverages + PriceOfFoods +1.59)*0.15))
    PaidTax.set(Tax)

    TT= ((PriceOfBeverages + PriceOfFoods +1.59)*0.15)

    TC= "" + str('%2f'%(PriceOfBeverages + PriceOfFoods +1.59+ TT))
    TotalCost.set(TC)



btnTotal=Button(frame3,padx=15,pady=15,bd=10,fg="black",font=('arial',10,'bold'),text="Total",command=CostOfItem).place(x=150,y=250)
#----------------------------------------------------------------------------------------------------------------------------------------
def receipt():
    
    
    txtReceipt.delete("1.0",END)
    x=random.randint(100898,6812789)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)

    txtReceipt.insert(END, 'Burger \t\t\t' + str(E_Burger.get()) + "\n")
    txtReceipt.insert(END, 'Pizza \t\t\t' + str(E_Pizza.get()) + "\n")
    txtReceipt.insert(END, 'Sandwich \t\t\t' + str(E_Sandwich.get()) + "\n")
    txtReceipt.insert(END, 'Salad \t\t\t' + str(E_Salad.get()) + "\n")

    txtReceipt.insert(END, 'Coffee \t\t\t' + str(E_Coffee.get()) + "\n")
    txtReceipt.insert(END, 'Tea \t\t\t' + str(E_Tea.get()) + "\n")
    txtReceipt.insert(END, 'Mojita \t\t\t' + str(E_Mojita.get()) + "\n")
    txtReceipt.insert(END, 'Shake \t\t\t' + str(E_Shake.get()) + "\n")

    txtReceipt.insert(END, 'CostOfFoods \t\t\t' + str(CostOfFoods.get()) + "\n")
    txtReceipt.insert(END, 'CostOfBeverages \t\t\t' + str(CostOfBeverages.get()) + "\n")
    txtReceipt.insert(END, 'PaidTax \t\t\t' + str(PaidTax.get()) + "\n")
    txtReceipt.insert(END, 'ServiceCharge \t\t\t' + str(ServiceCharge.get()) + "\n")
    txtReceipt.insert(END, 'TotalCost \t\t\t' + str(TotalCost.get()) + "\n")

   
var1 =  IntVar()
var2 =  IntVar()
var3 =  IntVar()
var4 =  IntVar()

var5 =  IntVar()
var6 =  IntVar()
var7 =  IntVar()
var8 =  IntVar()
    
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))
Receipt = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostOfBeverages = StringVar()
CostOfFoods = StringVar()
ServiceCharge = StringVar()
Receipt_Ref = StringVar()



btnReceipt =Button(frame3,padx=15,pady=15,bd=10,fg="black",font=('arial',10,'bold'),text="Receipt",command=receipt).place(x=1,y=350)

#-------------------------------------------------------------------------------------------------------------------------------


#-----------FOOD INPUT------------------------------------------------
E_Burger = IntVar()
E_Pizza = IntVar()
E_Sandwich = IntVar()
E_Salad = IntVar()

E_Burger.set("0")
E_Pizza.set("0")
E_Sandwich.set("0")
E_Salad.set("0")


#------------------------------------BEVERAGES INPUT-----------------------------------------------------------------------------------
E_Coffee = StringVar()
E_Tea = StringVar()
E_Mojita = StringVar()
E_Shake = StringVar()

E_Coffee.set("0")
E_Tea.set("0")
E_Mojita.set("0")
E_Shake.set("0")

#----------------------------------------LEFT FOODS SIDE-------------------------------------------------------------------------

Burger = Checkbutton(frame1,text="Burger: 10 \t",variable=var1,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=chkButton).place(x=1,y=10)
Pizza = Checkbutton(frame1,text="Pizza: 20 \t",variable=var2,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=chkButton).place(x=1,y=35)
Sandwich = Checkbutton(frame1,text="Sandwich: 30 \t",variable=var3,onvalue=1,offvalue=0,font=('arial',9,'bold'),command=chkButton).place(x=1,y=60)
Salad = Checkbutton(frame1,text="Salad: 15 \t",variable=var4,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=chkButton).place(x=1,y=85)

txtBurger = Entry(frame1, font=('arial',10,'bold'),bd=8,width=22,textvariable=E_Burger,justify='left',state='disabled')
txtBurger.place(x=100,y=10)
txtPizza = Entry(frame1, font=('arial',10,'bold'),bd=8,width=22,textvariable=E_Pizza,justify='left',state='disabled')
txtPizza.place(x=100,y=35)
txtSandwich = Entry(frame1, font=('arial',9,'bold'),bd=8,width=22,textvariable=E_Sandwich,justify='left',state='disabled')
txtSandwich.place(x=100,y=60)
txtSalad = Entry(frame1, font=('arial',10,'bold'),bd=8,width=22,textvariable=E_Salad,justify='left',state='disabled')
txtSalad.place(x=100,y=85)

Coffee = Checkbutton(frame2,text="Coffee: 15 \t",variable=var5,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=chkButton).place(x=1,y=10)
Tea = Checkbutton(frame2,text="Tea: 20 \t",variable=var6,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=chkButton).place(x=1,y=35)
Mojita = Checkbutton(frame2,text="Mojita: 25 \t",variable=var7,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=chkButton).place(x=1,y=60)
Shake = Checkbutton(frame2,text="Shake: 40  \t",variable=var8,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=chkButton).place(x=1,y=85)

txtCoffee = Entry(frame2, font=('arial',10,'bold'),bd=8,width=22,textvariable=E_Coffee,justify='left',state='disabled')
txtCoffee.place(x=100,y=10)
txtTea = Entry(frame2, font=('arial',10,'bold'),bd=8,width=22,textvariable=E_Tea,justify='left',state='disabled')
txtTea.place(x=100,y=35)
txtMojita = Entry(frame2, font=('arial',10,'bold'),bd=8,width=22,textvariable=E_Mojita,justify='left',state='disabled')
txtMojita.place(x=100,y=60)
txtShake = Entry(frame2, font=('arial',10,'bold'),bd=8,width=22,textvariable=E_Shake,justify='left',state='disabled')
txtShake.place(x=100,y=85)

#----------------------FOR RECEIPT FRAME----------------------------------------------------
lblReceipt = Label(frame4,font=('arial',12,'bold'),text="Restaurant Receipt", bd=2)
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt =Text(frame4,font=('arial',11,'bold'),bd=8,width=40)
txtReceipt.grid(row=1,column=0)
#--------------------------------Cost of Item information------------------------------------
lblCostOfFoods = Label(frame3,font=('arial',10,'bold'),text="CostOfFoods:", bd=8)
lblCostOfFoods.place(x=1,y=10)

txtCostOfFoods = Entry(frame3,font=('arial',10,'bold'), bd=6,justify='left',textvariable=CostOfFoods)
txtCostOfFoods.place(x=120,y=10)

lblCostOfBeverages = Label(frame3,font=('arial',10,'bold'),text="CostOfBeverages:", bd=8)
lblCostOfBeverages.place(x=1,y=40)

lblCostOfBeverages = Entry(frame3,font=('arial',10,'bold'),bd=7,justify='left',textvariable=CostOfBeverages)
lblCostOfBeverages.place(x=120,y=40)

lblCostofserviceCharge = Label(frame3,font=('arial',10,'bold'),text="ServiceCharge:", bd=8)
lblCostofserviceCharge.place(x=1,y=70)

lblCostofserviceCharge = Entry(frame3,font=('arial',10,'bold'), bd=6,justify='left',textvariable=ServiceCharge )
lblCostofserviceCharge.place(x=120,y=70)

#--------------------------------payment Information---------------------------------------------
lblCostOfTax = Label(frame3,font=('arial',10,'bold'),text="tex percentage:", bd=8)
lblCostOfTax.place(x=1,y=100)

txtCostOfTax = Entry(frame3,font=('arial',10,'bold'), bd=6,justify='left',textvariable=PaidTax)
txtCostOfTax.place(x=120,y=100)

lblCostOfSubTotal = Label(frame3,font=('arial',10,'bold'),text="SubTotal:", bd=8)
lblCostOfSubTotal.place(x=1,y=130)

lblCostOfSubTotal = Entry(frame3,font=('arial',10,'bold'),bd=6,justify='left',textvariable=SubTotal)
lblCostOfSubTotal.place(x=120,y=130)


lblCostofTotal = Label(frame3,font=('arial',10,'bold'),text="Total:", bd=8)
lblCostofTotal.place(x=1,y=160)

lblCostofTotal = Entry(frame3,font=('arial',10,'bold'), bd=6,justify='left',textvariable=TotalCost )
lblCostofTotal.place(x=120,y=160)
   
root.mainloop()

