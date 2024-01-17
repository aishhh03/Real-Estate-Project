from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class FlatDetails:
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
         labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Flat Add",font=("times new roman",12,"bold"),padx=2)
         labelframeleft.place(x=5,y=50,width=540,height=350)

#************************lbls and entries************************
         #floor
         lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_floor.grid(row=0,column=0,sticky=W)
            
         self.var_floor=StringVar()
         entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))     
         entry_floor.grid(row=0,column=1,sticky=W) 
        
        #flat No
         lbl_flatNo=Label(labelframeleft,text="Flat No",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_flatNo.grid(row=1,column=0,sticky=W)  
          
         self.var_flatNo=StringVar()
         entry_flatNo=ttk.Entry(labelframeleft,textvariable=self.var_flatNo,width=20,font=("arial",13,"bold"))     
         entry_flatNo.grid(row=1,column=1,sticky=W) 
         
         #flat type
         lbl_flattype=Label(labelframeleft,text="Flat Type",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_flattype.grid(row=2,column=0,sticky=W) 
           
         self.var_flatType=StringVar()
         entry_flattype=ttk.Entry(labelframeleft,textvariable=self.var_flatType,width=20,font=("arial",13,"bold"))     
         entry_flattype.grid(row=2,column=1,sticky=W) 
         
         #deposite
         lbl_deposite=Label(labelframeleft,text="Deposite",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_deposite.grid(row=3,column=0,sticky=W)  
          
         self.var_deposite=StringVar()
         entry_deposite=ttk.Entry(labelframeleft,textvariable=self.var_deposite,width=20,font=("arial",13,"bold"))     
         entry_deposite.grid(row=3,column=1,sticky=W) 
         
         #flat rate rent
         lbl_flatrate=Label(labelframeleft,text="Flat Rate",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_flatrate.grid(row=4,column=0,sticky=W)
            
         self.var_flatrate=StringVar()
         entry_flatrate=ttk.Entry(labelframeleft,textvariable=self.var_flatrate,width=20,font=("arial",13,"bold"))     
         entry_flatrate.grid(row=4,column=1,sticky=W) 
#*********************************btns***********************************
         btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
         btn_frame.place(x=0,y=200,width=412,height=40)
         
         btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnAdd.grid(row=0,column=0,padx=1)
         
         btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnUpdate.grid(row=0,column=1,padx=1)
         
         btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnDelete.grid(row=0,column=2,padx=1)
         
         btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnReset.grid(row=0,column=3,padx=1)

#***********************************table frame search system***************************************
         Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
         Table_Frame.place(x=600,y=55,width=500,height=345)
         
         
         scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
         
         self.flat_table=ttk.Treeview(Table_Frame,column=("floor","flatNo","flatType","deposite","flatrate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         
         scroll_x.config(command=self.flat_table.xview) 
         scroll_y.config(command=self.flat_table.yview)  
         
         
         self.flat_table.heading("floor",text="Floor")
         self.flat_table.heading("flatNo",text="Flat No")
         self.flat_table.heading("flatType",text="Flat Type")
         self.flat_table.heading("deposite",text="Deposite")
         self.flat_table.heading("flatrate",text="Flat Rate")
        
         
         self.flat_table["show"]="headings"
         
         self.flat_table.column("floor",width=100)
         self.flat_table.column("flatNo",width=100)
         self.flat_table.column("flatType",width=100)
         self.flat_table.column("deposite",width=100)
         self.flat_table.column("flatrate",width=100)
        
         self.flat_table.pack(fill=BOTH,expand=1) 
         self.flat_table.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()  
         
     # add data
     def add_data(self):
        if self.var_floor.get()=="" or self.var_flatType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s,%s,%s)",(
                                                                               self.var_floor.get(),
                                                                               self.var_flatNo.get(),
                                                                               self.var_flatType.get(),
                                                                               self.var_deposite.get(),
                                                                               self.var_flatrate.get()
                                                                               
                                                                               
                                                                                        
                                                                                        
                                                                                        
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Flat Added Successfully",parent=self.root)
            except Exception as es: 
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
                
          #************fetchdata      
     def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from details")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
          self.flat_table.delete(*self.flat_table.get_children())
          for i in rows:
              self.flat_table.insert("",END,values=i)
         conn.commit()
         conn.close()
         
    #get_cursor 
     def get_cursor(self,event=""):
        cursor_row=self.flat_table.focus()
        content=self.flat_table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0]),
        self.var_flatNo.set(row[1]),
        self.var_flatType.set(row[2]),
        self.var_deposite.set(row[3]),
        self.var_flatrate.set(row[4])
        

             
    # Update________Function
                                                                                        
     def update(self):
         if self.var_floor.get()=="":
             messagebox.showerror("Error","Please enter mobile number",parent=self.root)
         else:
             conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
             my_cursor=conn.cursor()
             my_cursor.execute("update details set FlatNo=%s,FlatType=%s,Deposite=%s,FlatRate=%s where Floor=%s", (
                                                                                                            self.var_floor.get(),
                                                                                                            self.var_flatNo.get(),
                                                                                                            self.var_flatType.get(),
                                                                                                            self.var_deposite.get(),
                                                                                                            self.var_flatrate.get()
                                                                                                                                           
                                                                                                                           ))
             conn.commit()  
             self.fetch_data()                                                                                                                                                                                           
             conn.close()
             messagebox.showinfo("Update","New Flat details has been updated successfully",parent=self.root)
             
    # DELETE____________FUNCTiON
     def mDelete(self):
             mDelete=messagebox.askyesno("Flat System","Do you want delete this flat",parent=self.root)
             if mDelete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
                my_cursor=conn.cursor()
                query="delete from details where Floor=%s"
                value=(self.var_floor.get(),)
                my_cursor.execute(query,value)
             else:
                 if not mDelete:
                     return
             conn.commit()
             self.fetch_data()
             conn.close() 
             
 # RESET_______
     def reset(self):
        self.var_floor.set(""),
        self.var_flatNo.set(""),
        self.var_flatType.set(""),
        self.var_deposite.set(""),
        self.var_flatrate.set("")
             
         
         
         










if __name__ == "__main__":
    root=Tk()
    obj=FlatDetails(root)
    root.mainloop()