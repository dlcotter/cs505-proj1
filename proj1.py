#!/usr/bin/python

from Tkinter import *
import MySQLdb
import pprint
  
def select_callback():
  username = username_str.get()
  first_name = first_name_str.get()
  last_name = last_name_str.get()
  age = age_str.get()
  sex = sex_bool.get()
  c = db.cursor(MySQLdb.cursors.DictCursor)
  q = "SELECT first_name,last_name,age,sex "\
      "FROM actors "\
      "JOIN users ON users.id = '{0}' "\
      "AND users.G >= actors.G "\
      "AND users.F >= actors.F "\
      "AND users.T >= actors.T "\
      "AND users.H >= actors.H "\
      "WHERE ('{1}' IN ('',first_name)) and "\
      "      ('{2}' IN ('',last_name)) and "\
      "      ('{3}' IN ('',age)) and "\
      "      ('{4}' IN ('',sex))".format(username,first_name,last_name,age,sex)
  print(q)
  c.execute(q)
  results.set('\t'.join(["First name","Last name","Age","Sex"]) + '\n')
  rows = c.fetchall()
  for row in rows:
    results.set(results.get() + row["first_name"] + '\t' + row["last_name"]  + '\t' + \
              str(row["age"]) + '\t' + ("Male" if row["sex"] == 0 else "Female") + '\t\n')
  print(results.get())

def insert_callback():
  first_name = first_name_str.get()
  last_name = last_name_str.get()
  age = age_str.get()
  sex = sex_bool.get()
  G = G_bool.get()
  F = F_bool.get()
  T = T_bool.get()
  H = H_bool.get()
  q = "INSERT INTO actors (first_name,last_name,age,sex,G,F,T,H) "\
      "VALUES ('{0}','{1}','{2}','{3}',1,{4},{5},{6})".format(first_name,last_name,age,sex,F,T,H)
  print(q)
  c = db.cursor()
  c.execute(q)
  db.commit()

def update_callback():
  username = username_str.get()
  first_name = first_name_str.get()
  last_name = last_name_str.get()
  age = age_str.get()
  sex = sex_bool.get()
  G = G_bool.get()
  F = F_bool.get()
  T = T_bool.get()
  H = H_bool.get()
  q = "UPDATE actors "\
      "JOIN users ON users.ID = '{0}' "\
      "AND users.G >= actors.G "\
      "AND users.F >= actors.F "\
      "AND users.T >= actors.T "\
      "AND users.H >= actors.H "\
      "SET actors.G=1,actors.F={5},actors.T={6},actors.H={7} "\
      "WHERE ('{1}' IN ('',first_name)) AND "\
      "      ('{2}' IN ('',last_name)) AND "\
      "      ('{3}' IN ('',age)) AND "\
      "      ('{4}' IN ('',sex)) ".format(username,first_name,last_name,age,sex,F,T,H)
  print(q)
  c = db.cursor()
  c.execute(q)
  db.commit()

def delete_callback():
  username = username_str.get()
  first_name = first_name_str.get()
  last_name = last_name_str.get()
  age = age_str.get()
  sex = sex_bool.get()
  q = "DELETE actors.* "\
      "FROM actors "\
      "JOIN users ON users.ID = '{0}' "\
      "AND users.G >= actors.G "\
      "AND users.F >= actors.F "\
      "AND users.T >= actors.T "\
      "AND users.H >= actors.H "\
      "WHERE ('{1}' IN ('',first_name)) and "\
      "      ('{2}' IN ('',last_name)) and "\
      "      ('{3}' IN ('',age)) and "\
      "      ('{4}' IN ('',sex))".format(username,first_name,last_name,age,sex)
  print(q)
  c = db.cursor()
  c.execute(q)
  db.commit()

db = MySQLdb.connect(user="root",db="cs505")
root = Tk()
results = StringVar()

username_str = StringVar()
username_lbl = Label(root,text="User")
username_lbl.grid(row=0,column=0,sticky=W)
Radiobutton(root,text="G",variable=username_str,value="G").grid(row=0,column=1,sticky=W)
Radiobutton(root,text="GF",variable=username_str,value="GF").grid(row=1,column=1,sticky=W)
Radiobutton(root,text="GT",variable=username_str,value="GT").grid(row=2,column=1,sticky=W)
Radiobutton(root,text="GH",variable=username_str,value="GH").grid(row=3,column=1,sticky=W)
Radiobutton(root,text="GFT",variable=username_str,value="GFT").grid(row=4,column=1,sticky=W)
Radiobutton(root,text="GFH",variable=username_str,value="GFH").grid(row=5,column=1,sticky=W)
Radiobutton(root,text="GFTH",variable=username_str,value="GFTH").grid(row=6,column=1,sticky=W)
username_str.set("G")

first_name_str = StringVar()
first_name_lbl = Label(root,text="First name")
first_name_lbl.grid(row=8,column=0,sticky=W)
first_name_tb = Entry(root,textvariable=first_name_str)
first_name_tb.grid(row=8,column=1,columnspan=2)

last_name_str = StringVar()
last_name_lbl = Label(root,text="Last name")
last_name_lbl.grid(row=10,column=0,sticky=W)
last_name_tb = Entry(root,textvariable=last_name_str)
last_name_tb.grid(row=10,column=1,columnspan=2)

age_str = StringVar()
age_lbl = Label(root,text="Age")
age_lbl.grid(row=20,column=0,sticky=W)
age_tb = Entry(root,textvariable=age_str)
age_tb.grid(row=20,column=1,columnspan=2)

sex_bool = BooleanVar()
sex_lbl = Label(root,text="Sex")
sex_lbl.grid(row=30,column=0,sticky=W)
Radiobutton(root,text="Male",variable=sex_bool,value=0).grid(row=30,column=1,sticky=W)
Radiobutton(root,text="Female",variable=sex_bool,value=1).grid(row=30,column=2,sticky=E)

compartments_lbl = Label(root,text="Compartment").grid(row=32,column=0,sticky=W)
disclaimer_lbl = Label(root,text="(INSERT only)").grid(row=33,column=0,sticky=W)
G_bool = BooleanVar()
F_bool = BooleanVar()
T_bool = BooleanVar()
H_bool = BooleanVar()
Checkbutton(root,text="G",variable=G_bool,state=DISABLED).grid(row=32,column=1,sticky=W)
Checkbutton(root,text="F",variable=F_bool).grid(row=32,column=2,sticky=W)
Checkbutton(root,text="T",variable=T_bool).grid(row=33,column=1,sticky=W)
Checkbutton(root,text="H",variable=H_bool).grid(row=33,column=2,sticky=W)
G_bool.set(1)

select_btn = Button(root,text="SELECT",command=select_callback)
select_btn.grid(row=40,column=1) 

insert_btn = Button(root,text="INSERT",command=insert_callback)
insert_btn.grid(row=40,column=2)

update_btn = Button(root,text="UPDATE",command=update_callback)
update_btn.grid(row=42,column=1) 

delete_btn = Button(root,text="DELETE",command=delete_callback)
delete_btn.grid(row=42,column=2) 

results_lbl_frame = LabelFrame(root,text="Results",padx=4,pady=4,relief=SUNKEN)
results_lbl_frame.grid(row=50,columnspan=3)
results_lbl = Label(results_lbl_frame,text=results,textvariable=results)
results_lbl.grid(row=60,columnspan=3,sticky=W)

root.mainloop()
