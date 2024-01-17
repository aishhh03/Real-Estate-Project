from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from flat1 import Flat1
from flat2 import Flat2
from flat3 import Flat3
from flat4 import Flat4
from flat5 import Flat5
from flat6 import Flat6
from flat7 import Flat7
from flat8 import Flat8
from flat9 import Flat9
from flat10 import Flat10
from flat11 import Flat11
from flat12 import Flat12
#import flatts 

class FlatProfile:
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
         main_frame.place(x=0,y=190,width=1450,height=560)
         
         #*****************************menu**********************
         lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_menu.place(x=0,y=0,width=230)
         
         #*****************************btn frm***********************
         btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
         btn_frame.place(x=0,y=35,width=228,height=450)
        
         
         cust_btn=Button(btn_frame,text="FLAT 1",command=self.flatprofile1,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         cust_btn.grid(row=0,column=0,pady=1)
         
         room_btn=Button(btn_frame,text="FLAT 2",command=self.flatprofile2,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         room_btn.grid(row=1,column=0,pady=1)
         
         detail_btn=Button(btn_frame,text="FLAT 3",command=self.flatprofile3,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         detail_btn.grid(row=2,column=0,pady=1)
         
         report_btn=Button(btn_frame,text="FLAT 4",command=self.flatprofile4,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         report_btn.grid(row=3,column=0,pady=1)
         
         logout_btn=Button(btn_frame,text="FLAT 5",command=self.flatprofile5,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         logout_btn.grid(row=4,column=0,pady=1)
         
         one_btn=Button(btn_frame,text="FLAT 6",command=self.flatprofile6,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         one_btn.grid(row=5,column=0,pady=1)
         
         two_btn=Button(btn_frame,text="FLAT 7",command=self.flatprofile7,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         two_btn.grid(row=6,column=0,pady=1)
         
         three_btn=Button(btn_frame,text="FLAT 8",command=self.flatprofile8,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         three_btn.grid(row=7,column=0,pady=1)
         
         four_btn=Button(btn_frame,text="FLAT 9",command=self.flatprofile9,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         four_btn.grid(row=8,column=0,pady=1)
         
         five_btn=Button(btn_frame,text="FLAT 10",command=self.flatprofile10,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         five_btn.grid(row=9,column=0,pady=1)
         
         six_btn=Button(btn_frame,text="FLAT 11",command=self.flatprofile11,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         six_btn.grid(row=10,column=0,pady=1)
         
         seven_btn=Button(btn_frame,text="FLAT 12",command=self.flatprofile11,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         seven_btn.grid(row=11,column=0,pady=1)
        
        #*********************************right side img***********************************
         img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\3.jpg")
         img3=img3.resize((1140,510),Image.LANCZOS)
         self.photoimg3=ImageTk.PhotoImage(img3)
         
         lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
         lblimg1.place(x=225,y=0,width=1140,height=510)  
         

     def flatprofile1(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat1(self.new_window)
      
     def flatprofile2(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat2(self.new_window)
    
    
     def flatprofile3(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat3(self.new_window)
      
     def flatprofile4(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat4(self.new_window)
      
     def flatprofile5(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat5(self.new_window)
      
     def flatprofile6(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat6(self.new_window)
        
     def flatprofile7(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat7(self.new_window)
        
     def flatprofile8(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat8(self.new_window)
   
     def flatprofile9(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat9(self.new_window)
        
     def flatprofile10(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat10(self.new_window)

     def flatprofile11(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat11(self.new_window)

     def flatprofile12(self):
        self.new_window= Toplevel(self.root)
        self.app=Flat12(self.new_window)



         
         
if __name__ == "__main__":
    root=Tk()
    obj=FlatProfile(root)
    root.mainloop()