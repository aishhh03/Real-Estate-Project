from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Flatbooking:
     def  __init__(self,root):
         self.root=root
         self.root.title("Real Estate")
         self.root.geometry("1137x480+225+214")
         
         #*******************variable****************************
         self.var_contact=StringVar()
         self.var_checkin=StringVar()
         self.var_checkout=StringVar()
         self.var_flattype=StringVar()
         self.var_flatavailable=StringVar()
         self.var_rent=StringVar()
         self.var_agreementdays=StringVar()
         self.var_paidtax=StringVar()
         self.var_subtotal=StringVar()
         self.var_total=StringVar()
               
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
         labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="FLATBOOKING",font=("times new roman",12,"bold"),padx=2)
         labelframeleft.place(x=5,y=50,width=425,height=430)

#************************lbls and entries************************
         #cust_ref
         lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_cust_contact.grid(row=0,column=0,sticky=W)   
         
         entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))     
         entry_contact.grid(row=0,column=1,sticky=W) 
         
         #fetch Data btn
         btnfetchdata=Button(labelframeleft,command=self.fetch_contact,text="FetchData",font=("arial",10,"bold"),bg="black",fg="gold",width=7)
         btnfetchdata.place(x=340,y=1)
         
         #check-in date
         check_in_date=Label(labelframeleft,text="Effective Date",font=("arial",12,"bold"),padx=2,pady=4)
         check_in_date.grid(row=1,column=0,sticky=W)   
         
         txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=28,font=("arial",13,"bold"))     
         txtcheck_in_date.grid(row=1,column=1) 
         
         #check out date
         lbl_check_out=Label(labelframeleft,text="End Date",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_check_out.grid(row=2,column=0,sticky=W)   
         
         txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=28,font=("arial",13,"bold"))     
         txt_check_out.grid(row=2,column=1) 
         
         #flat type
         lbl_flattype=Label(labelframeleft,text="Flat Type",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_flattype.grid(row=6,column=0,sticky=W)   
         
         conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
         my_cursor=conn.cursor()
         my_cursor.execute(" select FlatType from details")
         ide=my_cursor.fetchall()
         
         combo_FlatType=ttk.Combobox(labelframeleft,textvariable=self.var_flattype,width=26,font=("arial",13,"bold"))     
         combo_FlatType["value"]=ide
         combo_FlatType.current(0)
         combo_FlatType.grid(row=6,column=1) 
         
         #available flat
         lblFlatavailable=Label(labelframeleft,text="Flat No",font=("arial",12,"bold"),padx=2,pady=4)
         lblFlatavailable.grid(row=4,column=0,sticky=W)   
         
         #txtFlatavailable=ttk.Entry(labelframeleft,textvariable=self.var_flatavailable,width=28,font=("arial",13,"bold"))     
         #txtFlatavailable.grid(row=4,column=1) 
         
         conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
         my_cursor=conn.cursor()
         my_cursor.execute(" select FlatNo from details")
         rows=my_cursor.fetchall()
         
         combo_FlatNo=ttk.Combobox(labelframeleft,textvariable=self.var_flatavailable,width=26,font=("arial",13,"bold"))     
         combo_FlatNo["value"]=rows
         combo_FlatNo.current(0)
         combo_FlatNo.grid(row=4,column=1) 
         
         #Rent
         lblRent=Label(labelframeleft,text="Rent Rate",font=("arial",12,"bold"),padx=2,pady=4)
         lblRent.grid(row=5,column=0,sticky=W)   
         
         txtRent=ttk.Entry(labelframeleft,textvariable=self.var_rent,width=28,font=("arial",13,"bold"))     
         txtRent.grid(row=5,column=1) 
         
         #Agreement of days
         lbl_Agreementdays=Label(labelframeleft,text="1 Year Agreement",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_Agreementdays.grid(row=3,column=0,sticky=W)   
         
         txtAgreementdays=ttk.Entry(labelframeleft,textvariable=self.var_agreementdays,width=28,font=("arial",13,"bold"))     
         txtAgreementdays.grid(row=3,column=1) 
         
         #Paid Tax
         lbl_Paidtax=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=4)
         lbl_Paidtax.grid(row=7,column=0,sticky=W)   
         
         txt_Paidtax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=28,font=("arial",13,"bold"))     
         txt_Paidtax.grid(row=7,column=1) 
         
         #Sub Total
         lblSubTotal=Label(labelframeleft,text="Total Amount",font=("arial",12,"bold"),padx=2,pady=4)
         lblSubTotal.grid(row=8,column=0,sticky=W)   
         
         txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_subtotal,width=28,font=("arial",13,"bold"))     
         txtSubTotal.grid(row=8,column=1) 
         
         #Total Cost
         lblTotalCost=Label(labelframeleft,text="Amount Received",font=("arial",12,"bold"),padx=2,pady=4)
         lblTotalCost.grid(row=9,column=0,sticky=W)   
         
         txtTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=28,font=("arial",13,"bold"))     
         txtTotalCost.grid(row=9,column=1) 
         
#*******************************Bill BTn***************************
         btnBill=Button(labelframeleft,text="Total Amt",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnBill.grid(row=10,column=0,padx=1,sticky=W)
         
         
#*********************************btns***********************************
         btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
         btn_frame.place(x=0,y=350,width=412,height=40)
         
         btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnAdd.grid(row=0,column=0,padx=1)
         
         btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnUpdate.grid(row=0,column=1,padx=1)
         
         btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnDelete.grid(row=0,column=2,padx=1)
         
         btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
         btnReset.grid(row=0,column=3,padx=1)
         
         #*******************************Rightside img****************************************
         img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\managementsystem\MSImages\2.jpg")
         img3=img3.resize((450,250),Image.LANCZOS)
         self.photoimg3=ImageTk.PhotoImage(img3)
         lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
         lblimg.place(x=670,y=55,width=450,height=250)
         
 #***********************************table frame search system***************************************
         Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
         Table_Frame.place(x=435,y=280,width=860,height=260)
         
         lblSearchBy=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
         lblSearchBy.grid(row=0,column=0,sticky=W) 
         
         self.search_var=StringVar()
         combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,width=22,font=("arial",13,"bold"),state="readonly")  
         combo_search["value"]=("Contact","AvailableFlat")   
         combo_search.current(0)
         combo_search.grid(row=0,column=1,padx=1)
         
         self.txt_search=StringVar()
         txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=22,font=("arial",13,"bold"))     
         txtSearch.grid(row=0,column=2,padx=1) 
         
         btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=9)
         btnSearch.grid(row=0,column=3,padx=1)
         
         btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=9)
         btnShowAll.grid(row=0,column=4,padx=1)
         
#***********************************Shhow Data Tbl*************************
         details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
         details_table.place(x=0,y=50,width=700,height=130)
         
         scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
         
         self.flat_table=ttk.Treeview(details_table,column=("contact","checkinDate","checkoutDate","flatType","availableFlat","rent","agreementDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         
         scroll_x.config(command=self.flat_table.xview) 
         scroll_y.config(command=self.flat_table.yview)         
         
         self.flat_table.heading("contact",text="Contact")
         self.flat_table.heading("checkinDate",text="CheckInDate")
         self.flat_table.heading("checkoutDate",text="CheckOutDate")
         self.flat_table.heading("flatType",text="FlatType")
         self.flat_table.heading("availableFlat",text="AvailableFlat")
         self.flat_table.heading("rent",text="Rent")
         self.flat_table.heading("agreementDays",text="AgreementDays")
         
         self.flat_table["show"]="headings"
         
         self.flat_table.column("contact",width=100)
         self.flat_table.column("checkinDate",width=100)
         self.flat_table.column("checkoutDate",width=100)
         self.flat_table.column("flatType",width=100)
         self.flat_table.column("availableFlat",width=100)
         self.flat_table.column("rent",width=100)
         self.flat_table.column("agreementDays",width=100)
         self.flat_table.pack(fill=BOTH,expand=1)
         self.flat_table.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()
         
      # add data
     def add_data(self):
        if self.var_contact.get()=="" or self.var_flattype.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into flat values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                               self.var_contact.get(),
                                                                               self.var_checkin.get(),
                                                                               self.var_checkout.get(),
                                                                               self.var_flattype.get(),
                                                                               self.var_flatavailable.get(),
                                                                               self.var_rent.get(),
                                                                               self.var_agreementdays.get()
                                                                                        
                                                                                        
                                                                                        
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Flat Booked",parent=self.root)
            except Exception as es: 
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
          #************fetchdata      
     def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from flat")
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
        
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_flattype.set(row[3]),
        self.var_flatavailable.set(row[4]),
        self.var_rent.set(row[5]),
        self.var_agreementdays.set(row[6])
        
    # Update________Function
                                                                                        
     def update(self):
         if self.var_contact.get()=="":
             messagebox.showerror("Error","Please enter mobile number",parent=self.root)
         else:
             conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
             my_cursor=conn.cursor()
             my_cursor.execute("update flat set CheckInDate=%s,CheckOutDate=%s,FlatType=%s,AvailableFlat=%s,Rent=%s,AgreementDays=%s where Contact=%s",(
                 
                                                                                                                                                    self.var_contact.get(),
                                                                                                                                                    self.var_checkin.get(),
                                                                                                                                                    self.var_checkout.get(),
                                                                                                                                                    self.var_flattype.get(),
                                                                                                                                                    self.var_flatavailable.get(),
                                                                                                                                                    self.var_rent.get(),
                                                                                                                                                    self.var_agreementdays.get()
                                                                                                                                                   
                                                                                                                                                                   ))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Update","Flat details has been updated successfully",parent=self.root)
             
    # DELETE____________FUNCTiON
     def mDelete(self):
             mDelete=messagebox.askyesno("Flat System","Do you want delete this flat",parent=self.root)
             if mDelete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
                my_cursor=conn.cursor()
                query="delete from flat where Contact=%s"
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
             else:
                 if not mDelete:
                     return
             conn.commit()
             self.fetch_data()
             conn.close()  
    # RESET_______
     def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_flattype.set(""),
        self.var_flatavailable.set(""),
        self.var_rent.set(""),
        self.var_agreementdays.set(""),
        self.var_paidtax.set(""),
        self.var_subtotal.set(""),
        self.var_total.set("")
               
       
        
         
         
    #**************************************************All DataFectch************************     
     def fetch_contact(self):
        if self.var_contact.get()=="":
                messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
           my_cursor=conn.cursor()
           query=("select Name from customer where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value) 
           row=my_cursor.fetchone()
           
           if row==None:
             messagebox.showerror("Erro","This Number Not Found",parent=self.root)
           else:
             conn.commit()
             conn.close() 
             
             showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
             showDataframe.place(x=440,y=60,width=235,height=220)   
             
             lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
             lblName.place(x=0,y=0)
             
             lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
             lbl.place(x=90,y=0)
          #**********gender*********************
           conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
           my_cursor=conn.cursor()
           query=("select Gender from customer where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value) 
           row=my_cursor.fetchone()
                    
           lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
           lblGender.place(x=0,y=30)
             
           lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl2.place(x=90,y=30)
          
          #***************mobile*********************
           conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
           my_cursor=conn.cursor()
           query=("select Mobile from customer where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value) 
           row=my_cursor.fetchone()
                    
           lblMobile=Label(showDataframe,text="Mobile:",font=("arial",12,"bold"))
           lblMobile.place(x=0,y=60)
             
           lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl3.place(x=90,y=60)
           
           #***************area*********************
           conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
           my_cursor=conn.cursor()
           query=("select Area from customer where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value) 
           row=my_cursor.fetchone()
                    
           lblArea=Label(showDataframe,text="Area/City:",font=("arial",12,"bold"))
           lblArea.place(x=0,y=90)
             
           lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl4.place(x=90,y=90)
          
          #***************nationality*********************
           conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
           my_cursor=conn.cursor()
           query=("select Nationality from customer where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value) 
           row=my_cursor.fetchone()
                    
           lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
           lblNationality.place(x=0,y=120)
             
           lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl5.place(x=90,y=120)
           
           #***************Id Proof Type*********************
           conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
           my_cursor=conn.cursor()
           query=("select IdProof from customer where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value) 
           row=my_cursor.fetchone()
                    
           lblIdProofType=Label(showDataframe,text="Id Proof:",font=("arial",12,"bold"))
           lblIdProofType.place(x=0,y=150)
             
           lbl6=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl6.place(x=90,y=150)
          
          #***************Pan*********************
           conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
           my_cursor=conn.cursor()
           query=("select Pan from customer where Mobile=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value) 
           row=my_cursor.fetchone()
                    
           lblPan=Label(showDataframe,text="PAN:",font=("arial",12,"bold"))
           lblPan.place(x=0,y=180)
             
           lbl7=Label(showDataframe,text=row,font=("arial",12,"bold"))
           lbl7.place(x=90,y=180)
           
           #_____Search System
           
     def search(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="aishwarya09#",database="management_system")
         my_cursor=conn.cursor()
         
         my_cursor.execute("select * from flat where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
         rows=my_cursor.fetchall()
         if len (rows)!=0:
             self.flat_table.delete(*self.flat_table.get_children())
             for i in rows:
                 self.flat_table.insert("",END,values=i)
             conn.commit()
             conn.close()
             
          
     def total(self):
      inDate=self.var_checkin.get()
      outDate=self.var_checkout.get()
      inDate=datetime.strptime(inDate,"%d/%m/%Y")
      outDate=datetime.strptime(outDate,"%d/%m/%Y")
      self.var_agreementdays.set(abs(outDate-inDate).days)
      
      if (self.var_rent.get()=="10000" and self.var_flattype.get()=="{1 BHK}"):
        q1=float(10000)
        q2=float(1000)
        q3=float(self.var_agreementdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(Tax)
        self.var_subtotal.set(ST)
        self.var_total.set(TT)
        
      elif (self.var_rent.get()=="15000" and self.var_flattype.get()=="{2 BHK}"):
        q1=float(15000)
        q2=float(1000)
        q3=float(self.var_agreementdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(Tax)
        self.var_subtotal.set(ST)
        self.var_total.set(TT)
     

      elif (self.var_rent.get()=="20000" and self.var_flattype.get()=="{3 BHK}"):
        q1=float(20000)
        q2=float(1000)
        q3=float(self.var_agreementdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(Tax)
        self.var_subtotal.set(ST)
        self.var_total.set(TT)
          
          

         
         
         
         
         
         
         
         
if __name__ == "__main__":
    root=Tk()
    obj=Flatbooking(root)
    root.mainloop()