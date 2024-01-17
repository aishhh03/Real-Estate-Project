from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Owner:
     def  __init__(self,root):
         self.root=root
         self.root.title("Real Estate")
         self.root.geometry("1137x480+225+214")
         
 #*******************************title*******************************
         lbl_title=Label(self.root,text="Pimpri-Chinchwad, Home Housing Society, Pune",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_title.place(x=0,y=0,width=1137,height=50)
         
         # ****************************logo***********************
         img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\logo.png")
         img2=img2.resize((100,40),Image.LANCZOS)
         self.photoimg2=ImageTk.PhotoImage(img2)
         
         lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
         lblimg.place(x=5,y=2,width=100,height=40)
         
#****************************lbl frame************************
         labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Owner Details",font=("times new roman",12,"bold"),padx=2)
         labelframeleft.place(x=5,y=50,width=540,height=350)
         
         lbl_cust_contact=Label(labelframeleft,text="Owner Name: ABc",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_cust_contact.grid(row=0,column=0,sticky=W)   

         lbl_cust_contact=Label(labelframeleft,text="Owner Home Address: sant tukaram nagar , Pimpri Chinchwad ",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=1,column=0,sticky=W)   

         lbl_cust_contact=Label(labelframeleft,text="City                                            State",font=("arial",12,"bold"),padx=2,pady=2)
         lbl_cust_contact.grid(row=2,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Pimpri-Chinchwad,Pune      Mahrashtra",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=3,column=0,sticky=W)   
 

         lbl_cust_contact=Label(labelframeleft,text="E-mail                           Contact",font=("arial",13,"bold"),padx=2,pady=2)
         lbl_cust_contact.grid(row=4,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="aishwarya@gmail.com                        8669513068",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=6,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Property Information",font=("arial",13,"bold"),padx=2,pady=2)
         lbl_cust_contact.grid(row=7,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Rental Property Address: Pimpri-Chinchwad Home ousing Society,Pune",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=8,column=0,sticky=W)  

#*******************************Rightside img****************************************
         img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\111.jpg")
         img3=img3.resize((500,330),Image.LANCZOS)
         self.photoimg3=ImageTk.PhotoImage(img3)
         lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
         lblimg.place(x=600,y=55,width=500,height=330)
         
           



if __name__ == "__main__":
    root=Tk()
    obj=Owner(root)
    root.mainloop()