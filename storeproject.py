from tkinter import *
from tkinter import filedialog
import sqlite3
from datetime import*
from PIL import ImageTk,Image
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
try:
	image_data=sqlite3.connect("imagedb")
	image_data.execute('''CREATE TABLE IMG(NAME TEXT NOT NULL,IMAGE TEXT)''')
	image_data.close()
except:
	pass
try:
	storedata=sqlite3.connect("storedb")
	storedata.execute('''CREATE TABLE STOR(NAME TEXT NOT NULL, PRICE REAL NOT NULL, NUM REAL NOT NULL)''')
	storedata.close()
except:
	pass
try:
	history_data=sqlite3.connect("historydb")
	history_data.execute(''' CREATE TABLE HIST (NAME TEXT NOT NULL,TYPE TEXT NOT NULL,DATE TEXT NOT NULL,PRICE REAL NOT NULL,NUM REAL NOT NULL)''')
	histort_data.close()
except:
	pass
############start##############
l2=list()
z2=list()


def start_open():
	btn_show_h.place(relx=0.5,rely=0.25,relheight=0.25,relwidth=0.5)
	btn_store.place(relx=0,rely=0,relheight=0.25,relwidth=0.5)
	btn_sells.place(relx=0.5,rely=0,relheight=0.25,relwidth=0.5)
	btn_buys.place(relx=0,rely=0.25,relheight=0.25,relwidth=0.5)
	btn_exit.place(relx=0,rely=0.75,relheight=0.2,relwidth=1)
def back_start():
	btn_show_h.place_forget()
	btn_store.place_forget()
	btn_sells.place_forget()
	btn_buys.place_forget()
	btn_exit.place_forget()
def back_store():
	start_open()
	label_name_store.place_forget()
	label_num_store.place_forget()
	label_price_store.place_forget()
	btn_add_photo.place_forget()
	name_s.place_forget()
	price_s.place_forget()
	num_s.place_forget()
	btn_new_s.place_forget()
	btn_add_s.place_forget()
	btn_back_s.place_forget()
	btn_show_s.place_forget()
def back_sell():
	start_open()
	for i in label_sell:
		i.destroy()
	btn_sub.pack_forget()
	can_sell.place_forget()	#i.destroy()
	option_sell.destroy()
	#name_s.pack_forget()
	label_num_store.place_forget()
	num_s.pack_forget()
	btn_sell.place_forget()
	btn_back_se.place_forget()
def back_buy():
	pass
def show_back():
	#store_open()
	#for p in z:
		#p.pack_forget()
	scroll.place_forget()
	btn_empty_sh.pack_forget()
	btn_back_sh.pack_forget()
	can.place_forget()

def his_back():
	start_open()
	btn_back_h.pack_forget()
	btn_empty_h.pack_forget()
	scroll_h.place_forget()
	can_h.place_forget()


def store_open():
	back_start()
	label_name_store.place(relx=0.0,rely=0.1,relheight=0.1,relwidth=0.300)
	label_num_store.place(relx=0.0,rely=0.25,relheight=0.1,relwidth=0.300)
	label_price_store.place(relx=0.0,rely=0.35,relheight=0.1,relwidth=0.300)
	btn_add_photo.place(relx=0.600,rely=0.100,relheight=0.07,relwidth=0.100)
	name_s.place(relx=0.25,rely=0.1,relheight=0.1,relwidth=0.300)
	price_s.place(relx=0.25,rely=0.350,relheight=0.1,relwidth=0.300)
	num_s.place(relx=0.25,rely=0.250,relheight=0.1,relwidth=0.300)
	btn_new_s.place(relx=0.100,rely=0.500,relheight=0.2,relwidth=0.200)
	btn_add_s.place(relx=0.3,rely=0.500,relheight=0.200,relwidth=0.200)
	btn_back_s.place(relx=0,rely=0.800,relheight=0.20,relwidth=1.0)
	btn_show_s.place(relx=0.5,rely=0.5,relheight=0.2,relwidth=0.2)
def sell_op(name_se_li):
	global name_sell,option_sell,frame_sell,list_sells,dict_sells,dict_label
	list_sells=list()
	dict_sells=dict()
	dict_label=dict()
	name_sell=StringVar()
	name_sell.set("")
	if len(name_se_li)!=0:
		if name_se_li[0] == "that is not any product":
			name_se_li.pop(0)
	if name_se_li == []:
		name_se_li.append("that is not any product")
	option_sell=OptionMenu(main,name_sell,*name_se_li)
	option_sell.pack()
	can_sell.place(relx=0.3,rely=0.15,relheight=0.45,relwidth=0.45)
	scroll_sell.place(relx=0.95,rely=0,relheight=1,relwidth=0.05)
	can_sell.update_idletasks()
	can_sell.configure(scrollregion=can_sell.bbox("all"),yscrollcommand=scroll_sell.set)
	#name_sell.trace("w",sell)
label_sell=list()
def sell_sub():
	global list_sells,dict_sells,y
	if float(num_s.get()) < float(num_sell_limit[name_sell.get()]):
		if name_sell.get() in list_sells:
		       dict_label[name_sell.get()].destroy()
		#list_sells=list(list_sells)
		title_label_sell=Label(frame_sell,text="name\t\t\tnumber")
		title_label_sell.pack()
		l=Label(frame_sell,text=f"{name_sell.get()}\t\t\t{num_s.get()}")
		list_sells.append(name_sell.get())
		#list_sells=set(list_sells)
		dict_label[name_sell.get()]=l
		dict_sells[name_sell.get()]=num_s.get()
		label_error_less_num.pack_forget()
		l.pack()
		label_sell.append(l)

	else:
		label_error_less_num.pack()
def sell_open():
	back_start()
	sell_op(name_se_li)
	label_num_store.place(relx=0.25,rely=0.05,relheight=0.05,relwidth=0.1)
	#name_s.pack()
	num_s.pack()
	btn_sub.pack()
	btn_sell.place(relx=0.0,rely=0.65,relheight=0.15,relwidth=1)
	btn_back_se.place(relx=0.0,rely=0.8,relheight=0.15,relwidth=1)
def hist_open():
	btn_his.pack()
	btn_total.pack()
	btn_add.pack()
	btn_take.pack()
	btn_back.pack()
def buys_open():
	pass
def show_hist():
	global new_list_h
	back_start()
	lab_h(new_list_h)
	new_list_h=[]
	btn_empty_h.pack()
	btn_back_h.pack()
	can_h.update_idletasks()
	can_h.configure(scrollregion=can_h.bbox("all"),yscrollcommand=scroll_h.set)
	can_h.place(x=0,y=0,relwidth=1,relheight=1)
	scroll_h.place(rely=0,relx=0.95,relheight=1)
###########################
name_l=list()
num_l=list()
def plt_show():
	startdata=sqlite3.connect("historydb")
	startdata_cur=startdata.cursor()
	name=startdata_cur.execute('''SELECT NAME from HIST''').fetchall()
	num=startdata_cur.execute('''SELECT NUM from HIST''').fetchall()
	startdata.commit()
	startdata.close()
	for i in name:
		name_l.append(i[0])
	for n in num:
		num_l.append(n[0])
	print(name_l)
	print(num_l)
	plt.bar(name_l,num_l)
	plt.show()
#____________#__________#
def cheak_add():
	global new_a_n
	new_a_n=Toplevel(main)
	btn_yes=Button(new_a_n,text="yes",command=add_num)
	btn_yes.pack()
	btn_no=Button(new_a_n,text="no",command=lambda : new_a_n.destroy())
	btn_no.pack()
x=0
#__________#___________#
def choose_photo():
	global myimage,x,ext
	main.filename=filedialog.askopenfilename(initialdir="c:/" ,title="choose file" ,filetypes=[("all files","*")])
	myimage=Image.open(main.filename)
	img=main.filename
	ind=int(img.find("."))
	ext=img[ind:len(img)]
	print(ext)
	print(main.filename)
	x=1
#____________#_____________#
def new_store():
	global x,new_list,num_new_list
	storedata=sqlite3.connect("storedb")
	storedata_cur=storedata.cursor()
	store_name_list=storedata_cur.execute('''SELECT NAME from STOR ''').fetchall()
	g=[]

	for row in store_name_list:
		g.append(row[0])
	storedata.commit()
	storedata.close()
	name=str(name_s.get())
	price=float(price_s.get())
	num=float(num_s.get())
	if name_s.get() in g:
		btn_new_s.config(text="found")
	else:
		storedata=sqlite3.connect("storedb")
		storedata_cur=storedata.cursor()
		storedata_cur.execute('''INSERT INTO STOR (NAME,PRICE,NUM) VALUES(?,?,?)''', (name,price,num))
		storedata.commit()
		storedata.close()
		new_list.append([name,price,num])
		num_new_list+=1
		print("insert sucsses")
		if x != 0:
			image=os.getcwd()+"\\photo_store"+"\\"+name_s.get()+ext
			myimage.save(os.getcwd()+"\\photo_store"+"\\"+name_s.get()+ext)
			#Label(main,text=f"{g}").pack()
			print(image)
			image_data=sqlite3.connect("imagedb")
			image_data.execute('''INSERT INTO IMG (NAME,IMAGE) VALUES(?,?)''', (name,image))
			image_data.commit()
			image_data.close()
			print(image)
			x=0
				#btn_new.config(text="insert")
	#except:
			#t=Toplevel(main)
			#Label(t,text="that an error").pack()
#________________#___________#
def add_num():
	global num_dict
	if True:
		new_a_n.destroy()
		storedata=sqlite3.connect("storedb")
		storedata_cur=storedata.cursor()
		name=str(name_s.get())
		num=float(num_s.get())
		data_num=storedata_cur.execute('''SELECT NUM FROM STOR WHERE NAME=?''',([name]))
		new_num=num+float(list(data_num)[0][0])
		storedata_cur.execute('''UPDATE STOR SET NUM=? WHERE NAME=?''',(new_num,name))
		storedata.commit()
		storedata.close()
		num_dict[name].config(text=f"{new_num}")
		#btn_add.config(text="sucsses")
		#btn_add.config(bg="green")
		#btn_add.after(1000,re)
	#except:
		#t=Toplevel(main)
		#Label(t,text="that an error").pack()

#_______________#_____________#
def re():
   btn_add.config(text="addnum")
   btn_add.config(bg="white")
#______________#______________#
###########################
#______________#_______________#
def check_sell():
	global new_s
	new_s=Toplevel(main)
	btn_yes=Button(new_s,text="yes",command=sell)
	btn_no=Button(new_s,text="no",command= lambda : new.destroy())
	btn_yes.pack()
	btn_no.pack()
#______________#_______________#
def sell():
	global num_dict
	new_s.destroy()
	#try:
	for name in list_sells:
		#name=str()
		print(name)
		num=float(dict_sells[str(name)])
		type="input"
		date=str(datetime.now())
		storedata=sqlite3.connect("storedb")
		storedata_cur=storedata.cursor()
		sell_num=list(storedata_cur.execute(''' SELECT NUM FROM STOR WHERE NAME=?''',([name])))[0][0]
		mainrice=list(storedata_cur.execute(''' SELECT PRICE FROM STOR WHERE NAME=?''',([name])))[0][0]
		num_new=sell_num-num
		price=float(num*mainrice)
		storedata_cur.execute(''' UPDATE STOR SET NUM=? WHERE NAME=?''',(num_new,name))
		storedata.commit()
		storedata.close()
		num_dict[name].config(text=f"{num_new}")
		#btn_sell.config(text="sucsses")
		history_data=sqlite3.connect("historydb")
		history_data_cur=history_data.cursor()
		history_data_cur.execute('''INSERT INTO HIST (NAME,TYPE,DATE,PRICE,NUM) VALUES(?,?,?,?,?)''',(name,type,date,price,num))
		history_data.commit()
		history_data.close()
		new_list_h.append([name,type,date,price])
		for i in label_sell:
			i.destroy()




	#except:
	#t=Toplevel(main
	#Label(t,text="that an error").pack()

#_______________#______________#
################################
#________________#_____________#
#________________#_____________#
##########################

def empty():
   new.destroy()
   startdata=sqlite3.connect("historydb")
   startdata_cur=startdata.cursor()
   startdata_cur.execute('''DELETE from HIST''')
   startdata.commit()
   startdata.close()

#_______________#_____________#
def check_empty_s():
	global new
	new=Toplevel(main)
	btn_yes=Button(new,text="yes",command=empty_s)
	btn_no=Button(new,text="no",command= lambda : new.destroy())
	btn_yes.pack()
	btn_no.pack()
#########################
def show_store():
	global new_list
	lab(new_list)
	new_list=[]
	btn_back_sh.pack()
	btn_empty_sh.pack()
	can.update_idletasks()
	can.configure(scrollregion=can.bbox("all"),yscrollcommand=scroll.set)
	can.place(x=0,y=0,relwidth=1,relheight=1)
	scroll.place(rely=0,relx=0.95,relheight=1)
#_______________#_____________#
def empty_s():
	global num_dict,num_sell_limit,name_se_li,num_sell_limit,empty_sh_list,num_new_list
	new.destroy()
	startdata=sqlite3.connect("storedb")
	startdata_cur=startdata.cursor()
	startdata_cur.execute('''DELETE from STOR''')
	startdata.commit()
	startdata.close()
	num_sell_limit=[]
	name_se_li=[]
	num_dict={}
	num_sell_limit={}
	for i in empty_sh_list:
		for n in i:
			n.destroy()
	empty_sh_list=[]
	num_new_list=0

	show_store()
#_______________#_______________#
def check_empty_h():
	global new_h
	new_h=Toplevel(main)
	btn_yes=Button(new_h,text="yes",command=empty_h)
	btn_no=Button(new_h,text="no",command= lambda : new_h.destroy())
	btn_yes.pack()
	btn_no.pack()
#__________________#________________#
####################################
#_________________#____________#
#_________________#______________#
#______________#_____________#
#_______________#______________#
#_____________#________________#
def empty_h():
	global name_list_h,empty_h_list
	new_h.destroy()
	mon=sqlite3.connect("historydb")
	mon_cur=mon.cursor()
	mon_cur.execute('''DELETE FROM HIST ''')
	mon.commit()
	mon.close()
	name_list_h=[]
	for i in empty_h_list:
		for n in i:
			n.destroy()

#_______________#_______________#
def exit():
	main.destroy()
main=Tk()
main.geometry("650x550")
btn_store=Button(main,text="store",command=store_open,bg="white")
btn_sells=Button(main,text="sells",command=sell_open,bg="white")
btn_buys=Button(main,text="activity",command=plt_show,bg="white")
btn_exit=Button(main,text="exit",command=exit,bg="red")
btn_show_h=Button(main,text="history",command=show_hist,bg="white")
btn_add_photo=Button(main,text="image",command=choose_photo,bg="yellow")
btn_new_s=Button(main,text="new",command=new_store,bg="yellow")
btn_add_s=Button(main,text="add num",command=cheak_add,bg="yellow")
btn_show_s=Button(main,text="show",command=show_store,bg="yellow")
btn_back_s=Button(main,text="back",command=back_store)
btn_sell=Button(main,text="sell",command=check_sell,bg="yellow")
#btn_buy=Button(main,text="buy",command=check_buy)
btn_back_se=Button(main,text="back",command=back_sell,bg="red")
btn_his=Button(main,text="history",command=hist_open)
#btn_total=Button(main,text="total",command=total)
#btn_add_m=Button(main,text="add",command=add)
#btn_take=Button(main,text="take",command=take)
btn_sub=Button(main,text="submit",command=sell_sub)


name=Entry(main)
price_s=Entry(main)
num=Entry(main)
name_s=Entry(main)
num_b=Entry(main)
name_b=Entry(main)
num_s=Entry(main)
total_l=Label(main,text=" ")
main_enter=Entry(main)
label_name_store=Label(main,text="name")
label_num_store=Label(main,text="number")
label_price_store=Label(main,text="price")
label_error_less_num=Label(main,text="this number is more than the number in the store")
can_sell=Canvas(main,bg="white")
frame_sell=Frame(can_sell)
scroll_sell=Scrollbar(can_sell,orient="vertical",command=can_sell.yview,bg="green")
can_sell.create_window(0,0,anchor="nw",window=frame_sell)
can=Canvas(main)
scroll=Scrollbar(main,orient="vertical",command=can.yview)
frame=Frame(can)
can.create_window(0,0,window=frame)
img_lab=dict()
lab1=list()
l=list()
z=list()
startdata=sqlite3.connect("storedb")
startdata_cur=startdata.cursor()
_list=startdata_cur.execute('''SELECT * from STOR''').fetchall()
startdata.commit()
startdata.close()
num_dict=dict()
num_sell_limit=dict()
name_se_li=list()
empty_sh_list=list()
def lab(_list):
	global z,l,name_se_li
	for row in _list:
		space=Label(frame,text=" ",bg="red")#.pack()
		space.pack()
		name_sh=Label(frame,text=f"name:{row[0]}")#.pack()
		name_sh.pack()
		name_se_li.append(row[0])
		price_sh=Label(frame,text=f"price:{row[1]}")#.pack()
		price_sh.pack()
		num_sh=Label(frame,text=f"number:{row[2]}")#.pack()
		num_sh.pack()
		num_dict[row[0]]=num_sh
		num_sell_limit[row[0]]=row[2]
		empty_sh_list.append([space,name_sh,price_sh,num_sh])
		im(row[0])
		#z=[]
		#l=[]
def im(name):
	global ler
	ler=0
	ch=list()
	image_data=sqlite3.connect("imagedb")
	image=list(image_data.execute('''SELECT * from IMG '''))
	print(image)
	image_data.close()
	for v in image:
		img_lab[v[0]]=v[1]
	print(img_lab.keys())
	if name in img_lab.keys() and not(name in ch) :
		m=ImageTk.PhotoImage(Image.open(img_lab[name]))
		l.append(m)
		le=len(l)
		print(le)
		for n in l:
			ler+=1
			if ler==le:
				print(ler)
				image_sh=Label(frame,image=n)
				z.append(image_sh)
				empty_sh_list[len(empty_sh_list)-1].append(image_sh)
				#print(ler)
		for p in z:
			p.pack()
		ch.append(name)
lab(_list)
new_list=list()
num_new_list=0
btn_back_sh=Button(main,text="back",command=show_back)
btn_empty_sh=Button(frame,text="empty",command=check_empty_s)


can_h=Canvas(main)
scroll_h=Scrollbar(main,orient="vertical",command=can.yview)
frame_h=Frame(can_h)
can_h.create_window(0,0,window=frame_h)
#img_lab_h=dict()
lab1_h=list()
l_h=list()
z_h=list()
startdata=sqlite3.connect("historydb")
startdata_cur=startdata.cursor()
_list_h=startdata_cur.execute('''SELECT * from HIST''').fetchall()
startdata.commit()
startdata.close()
print(_list_h)
empty_h_list=list()
def lab_h(_list_h):
	global z_h,l_h
	for row in _list_h:
		print(row)
		space_h=Label(frame_h,text="  ")
		space_h.pack()
		name_h=Label(frame_h,text=f"product:{row[0]}")
		name_h.pack()
		statue_h=Label(frame_h,text=f"input or out put:{row[1]}")
		statue_h.pack()
		date_h=Label(frame_h,text=f"date of opertion:{row[2]}")
		date_h.pack()
		price_h=Label(frame_h,text=f"price:{row[3]}")
		price_h.pack()
		#im(row[0])
		empty_h_list.append([space_h,name_h,price_h,statue_h,date_h])
		#z=[]
		#l=[]
lab_h(_list_h)
new_list_h=list()
#num_new_list_h=0

btn_empty_h=Button(frame_h,text="empty",command=check_empty_h)
btn_back_h=Button(frame_h,text="back",command=his_back)
btn_back_sh=Button(main,text="back",command=show_back)
btn_empty_sh=Button(frame,text="empty",command=check_empty_s)
num_new_list=0
start_open()
######################
'''
##########
##########
##########
'''
mainloop()
