# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:14:58 2018
@author: Tej K

"""
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:13:31 2018
@author: Tej K

"""
"""
Discription: To approximate the curability of the tumour 
Inputs:Age and Size of thr tumour 
Output:Curability status

"""

#Libraries
from numpy import *
import numpy as np
from matplotlib.pyplot import * 
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox

#Creating a window
root = Tk()

#The data of age and tumor size
x=np.array([40,32,10,35,28,50,19,11,50,25,17,66,22,9,33,10,15,7,19,42,22,45,77,63,56,76,33,49,79,100,55,77,42,80,45,28,92,55,17,35,12,13,15,21,31,35,46,76,87,90,57,64,86,77,3,2])
y=np.array([5.6,5.2,2.8,2.25,3.4,1.5,4.35,2.6,4.4,6,1.1,4,3.4,5,2.8,2,4.9,3.3,6,1.1,6,1.1,4.4,3.3,6.9,1,2,3,4,5,6,1.2,3.4,5.6,2,6.3,4.4,0.3,3.4,1.1,4.4,5.6,1.1,6.4,6.7,1.4,3.5,5,2,1.9,0.2,5.1,7,5.3,0.1,0.0])

#Obatin the fit line required for regression for degree 1
p1=polyfit(x,y,1)
m,c=p1
print(m)
print(c)

#Naming the graph and axes
plt.title('GRAPH')
plt.xlabel('AGE')
plt.ylabel('TUMOUR SIZE')


#Window attributes
root.title("TUMOUR HEALTH")
root.geometry("600x500")

#Background image
image = PhotoImage(file = "ima1.png")
image=image.subsample(1,1)
labeli=Label(image=image)
labeli.image=image
labeli.place(x=0,y=0,relwidth=1.0,relheight=1.0,anchor=NW)

#root.configure(background='#000080')

#Title
label1=Label(root,text="CURABILITY PREDICTOR",font="Corbel 30 bold",bg="#DF0040",fg="black")
            
#Fields             
label2=Label(root,text="NAME",font="Times 20 bold",bg="#DF0040",fg="black")
label3=Label(root,text="AGE (in years)",font="Times 20 bold",bg="#DF0040",fg="black")
label4=Label(root,text="SIZE (in cm)",font="Times 20 bold",bg="#DF0040",fg="black")

#Entries
entry1=Entry(root,bd =5)
entry2=Entry(root,bd =5)
entry3=Entry(root,bd =5)

#Arrangement of fields
label1.grid(row=0,column=1,columnspan=3,sticky=NSEW)
label2.grid(row=3,column=2,columnspan=2,sticky=W)
entry1.grid(row=3,column=3,sticky=E)
label3.grid(row=5,column=2,columnspan=2,sticky=W)
entry2.grid(row=5,column=3,sticky=E)
label4.grid(row=7,column=2,columnspan=2,sticky=W)
entry3.grid(row=7,column=3,sticky=E)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(5, weight=0)
root.grid_rowconfigure(7, weight=0)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

#Takes the iput and processes
def getData():
    try:
        global m,c,x,y,p1,fit,xx,yy
        r=entry2.get()
        name = (entry1.get())
        xx = float((entry2.get()))
        yy = float((entry3.get()))
    
        print(xx)
        print(yy)
        plot(x,y,'o')
        plt.axis([0,60,0,7])
        fit=m*xx+c
        print(fit)
        plot(x,polyval(p1,x),'r--')
        plot([xx],[yy],'o')
        print(x)
        print(y)
    except:
        tkinter.messagebox.showerror("DATA","Please enter valid data")    
        
#confirmation of entered data        
def confirm():
    if(len(entry1.get())==0 or len(entry2.get())==0 or len(entry3.get())==0):
        tkinter.messagebox.showinfo('info','Enter valid data')
    else:
        ans=tkinter.messagebox.askquestion('CONFIRMATION','do you want to confitm submission?')
        if ans=="yes":
            getData()

#checks for curability        
def cure():
    global yy,fit
    if(fit>yy):
        tkinter.messagebox.showinfo("cure", 'Curable')
    else:
        tkinter.messagebox.showinfo("cure", 'Non Curable')
        
#The quit function         
def quii():
     ans=tkinter.messagebox.askquestion('CONFIRMATION','do you want to quit?')
     if ans=="yes":
         root.destroy()

#Buttons 
submit = Button(root, text ="Submit", command = getData,bg="#FF5733",fg="black")
submit.grid(row=13,column=2,sticky=W) 
submit.config(width=10, height=2)

cure = Button(root, text ="Cureable?", command = cure,bg="#FF5733",fg="black")
cure.grid(row=13,column=3,sticky=E)
cure.config(width=10, height=2) 

qui= Button(root,text="Quit",command=quii,bg="#FF5733",fg="black")
qui.grid(row=15,column=1,columnspan=3)
qui.config(width=10, height=2) 

root.grid_rowconfigure(13, weight=0)
root.grid_rowconfigure(15, weight=0)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()