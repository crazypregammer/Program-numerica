# Program-numerica
Bisection method fortran python
from tkinter import  ttk
from  tkinter import *



def Biseccion():
    ventana2 = Toplevel(ventana, bg="green")
    ventana2.title("Biseccion")
    ventana2.geometry('400x300')
    Label(ventana2, text='X1:',font=("Agency FB",14),bg="green").place(x=10,y=20)
    entradaX1=StringVar()
    txtX1= Entry(ventana2,textvariable=entradaX1).place(x=80,y=20)
    Label(ventana2, text='X2:',font=("Agency FB",14),bg="green").place(x=10,y=65)
    entradaX2 = StringVar()
    txtX2= Entry(ventana2, textvariable=entradaX2).place(x=80,y=70)

    resultado=StringVar()
    Label(ventana2, text='RESULTADO:', font=("Agency FB", 14), bg="green").place(x=0, y=115)
    txtR= Entry(ventana2, textvariable=resultado,state="readonly",width=50).place(x=80, y=120)
    buton=Button(ventana2,text="CALCULAR",font=("Agency FB", 14)).place(x=80, y=170)


def Secante():
    ventana=Tk()

def Newton():
    ventana = Tk()

def Grafica():
    ventana = Tk()

def ReglaFalsa():
    ventana=Tk()





ventana=Tk()
ventana.geometry('400x300+1900+100')
ventana.configure(background='dark turquoise')
ventana.title("Calculo de ceros de funciones")
titulo=Label(ventana,text='Algoritmos',font=("Agency FB",30),bg='dark turquoise')
titulo.pack()
entry=Entry(ventana)
entry.pack(fill=X,padx=5,pady=5,ipadx=5,ipady=5)




botonB=Button(ventana,text="Biseccion",command=Biseccion)
botonS=Button(ventana,text="Secante",command=Secante)
botonN=Button(ventana,text="Newton-Rampson",command=Newton)
botonG=Button(ventana,text="Grafica",command=Grafica)
botonR=Button(ventana,text="Regla falsa",command=ReglaFalsa)

botonB.pack(side=LEFT,padx=5,pady=5,ipadx=2,ipady=5)
botonS.pack(side=LEFT,padx=5,pady=5,ipadx=2,ipady=5)
botonN.pack(side=LEFT,padx=5,pady=5,ipadx=2,ipady=5)
botonR.pack(side=LEFT,padx=5,pady=5,ipadx=2,ipady=5)
botonG.pack(side=LEFT,padx=5,pady=5,ipadx=2,ipady=5)
ventana.mainloop()
