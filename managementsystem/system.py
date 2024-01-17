from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from customer import Cust_Win
from flat import Flatbooking
from details import FlatDetails
from owner import Owner 
from system1 import FlatProfile
#import flatts 

class ManagementSystem:
     def  __init__(self,root):
         self.root=root
         self.root.title("Real Estate")
         self.root.geometry("1550x800+0+0")
         
         #************************1st Img**************************
         img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\istockphoto-1058166532-612x612.jpg")
         img1=img1.resize((1365,140),Image.LANCZOS)
         self.photoimg1=ImageTk.PhotoImage(img1)
         
         lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
         lblimg.place(x=0,y=0,width=1365,height=140)         
         
         # ****************************logo***********************
         img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\logo.png")
         img2=img2.resize((230,140),Image.LANCZOS)
         self.photoimg2=ImageTk.PhotoImage(img2)
         
         lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
         lblimg.place(x=0,y=0,width=230,height=140) 
         
         #*******************************title*******************************
         lbl_title=Label(self.root,text="Real Estate",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_title.place(x=0,y=140,width=1550,height=50)
         
         #*****************************in frame***********************
         main_frame=Frame(self.root,bd=4,relief=RIDGE)
         main_frame.place(x=0,y=190,width=1450,height=520)
         
         #*****************************menu**********************
         lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_menu.place(x=0,y=0,width=230)
         
         #*****************************btn frm***********************
         btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
         btn_frame.place(x=0,y=35,width=228,height=190)
         
         cust_btn=Button(btn_frame,text="CUSTOMER REG",command=self.cust_detail,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         cust_btn.grid(row=0,column=0,pady=1)
         
         room_btn=Button(btn_frame,text="FLATBOOKING",command=self.flatbooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         room_btn.grid(row=1,column=0,pady=1)
         
         detail_btn=Button(btn_frame,text="FLATRATE",command=self.flatdetails,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         detail_btn.grid(row=2,column=0,pady=1)
         
         report_btn=Button(btn_frame,text="OWNERDETAIILS",width=22,command=self.owner,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         report_btn.grid(row=3,column=0,pady=1)
         
         logout_btn=Button(btn_frame,text="FLAT",width=22,command=self.flatimg,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         logout_btn.grid(row=4,column=0,pady=1)
         
            
         #*********************************right side img***********************************
         img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\3.jpg")
         img3=img3.resize((1140,510),Image.LANCZOS)
         self.photoimg3=ImageTk.PhotoImage(img3)
         
         lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
         lblimg1.place(x=225,y=0,width=1140,height=510) 
         
         
         #*******************************************down images***************************
         img4=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\4.jpg")
         img4=img4.resize((230,150),Image.LANCZOS)
         self.photoimg4=ImageTk.PhotoImage(img4)
         
         lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
         lblimg1.place(x=0,y=225,width=230,height=150) 
         
         img5=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\8.jpg")
         img5=img5.resize((230,140),Image.LANCZOS)
         self.photoimg5=ImageTk.PhotoImage(img5)
         
         lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
         lblimg1.place(x=0,y=370,width=230,height=140) 
         
         
     def cust_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
         
     def flatbooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Flatbooking(self.new_window)
         
     def flatdetails(self):
        self.new_window=Toplevel(self.root)
        self.app=FlatDetails(self.new_window)

     def owner(self):
        self.new_window=Toplevel(self.root)
        self.app=Owner(self.new_window)
        
     def flatimg(self):
        self.new_window= Toplevel(self.root)
        self.app=FlatProfile(self.new_window)
      
   
        
     
        
     
         
               
         
if __name__ == "__main__":
    root=Tk()
    obj=ManagementSystem(root)
    root.mainloop()