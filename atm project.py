from tkinter import*
import time

win=Tk()
win.geometry("900x850")
win.title("ATM MACHINE")
win .config(bg="black")

Tops=Frame(win,bg="WHITE",width=80,height=50,padx="40",pady="40",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(win,bg="black",width=300,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(win,bg="black",width=400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

Lblinfo=Label(Tops,font=('aria',20,'bold'),text="ATM MACHINE:",fg="red",bg="black",bd=10,anchor='w')
Lblinfo.grid(row=0,column=0)

Lblinfo=Label(Tops,font=('aria',20,'bold'),text=localtime,fg="blue",bg="black",bd=10,anchor='w')
Lblinfo.grid(row=1,column=0)

number= StringVar()
amount= StringVar()
withdraw= StringVar()
acca= " "

def bank():
    global acca
    accno =["0001","0002","0003","0004"]
    account=number.get()
    if account in accno:
        label1.config(text="REGISTERED USER")
        bank={"0001":1000,"0002":1500,"0003":2000,"0004":2500}
        balance=bank[account]
        acca=balance
    else:
        label1.config(text="NON REGISTERED USER")
        
def deposit():
    global acca
    amo=float(amount.get())
    bal=acca+amo
    label3.config(text=("NET BALANCE:",str(bal)))


def withdraw():
    global acca
    wd=float(withdraw.get(0))
    if acca>=wd:
        acce=acca-wd
        label4.config(text=("NET BALANCE:",str(acce)))
    else:
        label4.config(text="insufficient balance")
        
def bal():
    global acca
    label5.config(text=("net balance",str(acca)))
    
def reset():
    number.set("")
    amount.set("")
    withdraw.set("")
    label1.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")
                          
Lbl=Label(f1,font=('aria',20,'bold'),text="ENTER THE ACCOUNT NUMBER:   ",fg="white",bg="black",bd=10,anchor='w')
Lbl.grid(row=0,column=3)
text=Entry(f1,font=('ariel',20,'bold'),textvariable=number,bd=6,insertwidth=4,bg="blue")  
text.grid(row=0,column=4)
label1=Label(f1,font=('white',20,'bold'),fg="blue",bg="black",bd=10)
label1.grid(row=1,column=4)
btnsubmit=Button(f2,padx=16,pady=4,bd=10,fg="black",font=('aria',20,'bold'),width=7,text="SUMMIT",bg="blue",command=bank)
btnsubmit.grid(row=0,column=4)  


lbltotal=Label(f1,text="               ",fg="white",bg="black")
lbltotal.grid(row=3,columnspan=10)

Lbl=Label(f1,font=('aria',20,'bold'),text="ENTER THE AMOUNT TO BE DEPOSITED:   ",fg="white",bg="black",bd=10,anchor='w')
Lbl.grid(row=4,column=3)
text=Entry(f1,font=('ariel',20,'bold'),textvariable=amount,bd=6,insertwidth=4,bg="blue")  
text.grid(row=4,column=4)
label3=Label(f1,font=('white',20,'bold'),fg="blue",bg="black",bd=10)
label3.grid(row=5,column=4)
btnsubmit=Button(f2,padx=16,pady=4,bd=10,fg="black",font=('aria',20,'bold'),width=7,text="DEPOSIT",bg="blue",command=deposit)
btnsubmit.grid(row=4,column=4)

lbltotal=Label(f1,text="        ",fg="white",bg="black") 
lbltotal.grid(row=7,columnspan=10)

Lbl=Label(f1,font=('aria',20,'bold'),text="ENTER THE AMOUNT TO BE WITHDRAW:   ",fg="white",bg="black",bd=10,anchor='w')
Lbl.grid(row=8,column=3)
text=Entry(f1,font=('ariel',20,'bold'),textvariable=withdraw,bd=6,insertwidth=4,bg="blue")  
text.grid(row=8,column=4)
label4=Label(f1,font=('white',20,'bold'),fg="blue",bg="black",bd=10)
label4.grid(row=9,column=4)
label5=Label(f1,fg="white",bg="black",font=('aria',16,'bold'))
label5.grid(row=10,column=4)

btnwithdraw=Button(f2,padx=16,pady=4,bd=10,fg="black",font=('aria',20,'bold'),width=7,text="WITHDRAW",bg="blue",command=withdraw)
btnwithdraw.grid(row=8,column=4)
btnbal=Button(f2,padx=16,pady=4,bd=10,fg="black",font=('aria',20,'bold'),width=7,text="BALANCE",bg="blue",command=bal)
btnbal.grid(row=10,column=4)
btnreset=Button(f2,padx=16,pady=4,bd=10,fg="black",font=('aria',20,'bold'),width=7,text="RESET",bg="blue",command=reset)
btnreset.grid(row=11,column=4)
btnexit=Button(f2,padx=16,pady=4,bd=10,fg="black",font=('aria',20,'bold'),width=7,text="EXIT",bg="blue",command=win.destroy)
btnexit.grid(row=12,column=4)

mainloop()






