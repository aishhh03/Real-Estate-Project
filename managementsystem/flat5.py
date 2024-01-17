from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import tkinter as tk

class Flat5:
     def  __init__(self,root):
         self.root=root
         self.root.title("Real Estate3")
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
         labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Flat",font=("times new roman",12,"bold"),padx=2)
         labelframeleft.place(x=5,y=50,width=540,height=420)
         
#************************lbls and entries************************
            
         
         lbl_cust_contact=Label(labelframeleft,text="2 BHK Flat for Rent",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_cust_contact.grid(row=0,column=0,sticky=W)   

         lbl_cust_contact=Label(labelframeleft,text="Pimpri-Chinchwad,Home Housing Society, Pune ",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=1,column=0,sticky=W)   

         lbl_cust_contact=Label(labelframeleft,text="Overview",font=("arial",12,"bold"),padx=2,pady=2)
         lbl_cust_contact.grid(row=2,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Furnishing: Unfurnished Bathroom: 1 Balcony: 1",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=3,column=0,sticky=W)   

         lbl_cust_contact=Label(labelframeleft,text="Available from: Sept,2023  Floor No: Higher of 3 floors",font=("arial",10),padx=2,pady=2)
         lbl_cust_contact.grid(row=4,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="LeaseType: Family/ Bachelor Parking: 1 Covered and 1 Open Parking",font=("arial",10),padx=2,pady=2)
         lbl_cust_contact.grid(row=5,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Price Details",font=("arial",13,"bold"),padx=2,pady=2)
         lbl_cust_contact.grid(row=6,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Security: Rs.40,000 Brokerage: Rs.16,000",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=7,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Additional Details",font=("arial",13,"bold"),padx=2,pady=2)
         lbl_cust_contact.grid(row=8,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Build up area: 650 sq.ft Carpet Area: 420 sq.ft",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=9,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Age of property: 10 years Maini entrance facing: East",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=10,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Gate Commuinty",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=11,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="Offers",font=("arial",13,"bold"),padx=2,pady=2)
         lbl_cust_contact.grid(row=12,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="1. Free deep cleanng service",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=13,column=0,sticky=W)  

         lbl_cust_contact=Label(labelframeleft,text="2. Free rental agreement and free police verfication",font=("arial",12),padx=2,pady=2)
         lbl_cust_contact.grid(row=14,column=0,sticky=W)  

         
           
#*******************************Rightside img****************************************
         img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\15.jpg")
         img3=img3.resize((570,420),Image.LANCZOS)
         self.photoimg3=ImageTk.PhotoImage(img3)
         lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
         lblimg.place(x=560,y=55,width=570,height=420)
         
       
         
if __name__ == "__main__":
    root=Tk()
    obj=Flat5(root)
    root.mainloop()
    