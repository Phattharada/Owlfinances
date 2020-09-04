from tkinter import *
from tkinter import ttk
import csv

#screen
Mafin = Tk()
Mafin.title('Mafinace')
Mafin.geometry('500x500')
###############################
with open ('shortnote.csv')as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)
	
# tab
tab = ttk.Notebook(Mafin)
tab.pack(fill=BOTH,expand=1)

F1 = Frame(tab)
F2 = Frame(tab)
F3 = Frame(tab)
F4 = Frame(tab)
#######################

#tab รายรับรายจ่าย
tab.add(F1,text='รายรับรายจ่าย')
tab1 = ttk.Notebook(F1)
tab1.pack(fill=BOTH,expand=1)

f1 = Frame(tab1)
ent = Frame(tab1)
ent.pack()
List = Frame(tab1)
List.pack()
G = Frame(tab1)
G.pack()

tab1.add(ent,text='บันทึกรายรับรายจ่าย')
tab1.add(List,text='รายการแสดงรายรับรายจ่าย')
tab1.add(G,text='กราฟแสดงรายรับรายจ่าย')

#รายรับ
list1=StringVar()
category1=StringVar()
mon1=DoubleVar()

l1 = Label(ent,text='รายรับ')
l1.place(x=20,y=20)
le1 = Label(ent,text='รายการ')
le1.place(x=20,y=40)
en1 = Entry(ent,textvariable=list1)
en1.place(x=20,y=60)
le2 = Label(ent,text='ประเภท')
le2.place(x=20,y=80)
en2 = Entry(ent,textvariable=category1)
en2.place(x=20,y=100)
le3 = Label(ent,text='จำนวนเงิน')
le3.place(x=20,y=120)
en3 = Entry(ent,textvariable=mon1)
en3.place(x=20,y=140)
save1 = Button(ent,text='บันทึก')
save1.place(x=30,y=170)

#รายจ่าย
list2=StringVar()
category2=StringVar()
mon2=DoubleVar()

l2 = Label(ent,text='รายจ่าย')
l2.place(x=200,y=20)
le21 = Label(ent,text='รายการ')
le21.place(x=200,y=40)
en21 = Entry(ent,textvariable=list2)
en21.place(x=200,y=60)
le22 = Label(ent,text='ประเภท')
le22.place(x=200,y=80)
en22 = Entry(ent,textvariable=category2)
en22.place(x=200,y=100)
le23 = Label(ent,text='จำนวนเงิน')
le23.place(x=200,y=120)
en23 = Entry(ent,textvariable=mon2)
en23.place(x=200,y=140)
save2 = Button(ent,text='บันทึก')
save2.place(x=210,y=170)

#########################

#tab ค่าน้ำค่าไฟ
tab.add(F2,text='ค่าน้ำค่าไฟ')
tab1 = ttk.Notebook(F2)
tab1.pack(fill=BOTH,expand=1)

mitor = Frame(tab1)
mitor.pack()
G = Frame(tab1)
G.pack()

tab1.add(mitor,text='บันทึกยูนิทการใช้น้ำและไฟฟ้า')
tab1.add(G,text='กราฟแสดงการใช้น้ำและไฟฟ้า')

#ค่าน้ำ
date1=StringVar()
unit1=DoubleVar()

le1 = Label(mitor,text='ยูนิทน้ำประปา')
le1.place(x=20,y=20)
le2 = Label(mitor,text='วันที่')
le2.place(x=20,y=40)
en2 = Entry(mitor,textvariable=date1)
en2.place(x=20,y=60)
le3 = Label(mitor,text='หน่วย')
le3.place(x=20,y=80)
en3 = Entry(mitor,textvariable=unit1)
en3.place(x=20,y=100)
save11 = Button(mitor,text='บันทึก')
save11.place(x=20,y=130)

#ค่าไฟ
date2=StringVar()
unit2=DoubleVar()

le21 = Label(mitor,text='ยูนิทไฟฟ้า')
le21.place(x=200,y=20)
le22 = Label(mitor,text='วันที่')
le22.place(x=200,y=40)
en22 = Entry(mitor,textvariable=date2)
en22.place(x=200,y=60)
le32 = Label(mitor,text='หน่วย')
le32.place(x=200,y=80)
en32 = Entry(mitor,textvariable=unit2)
en32.place(x=200,y=100)
save12 = Button(mitor,text='บันทึก')
save12.place(x=200,y=130)
##########################
tab.add(F3,text='ธนาคาร')
#############
tab.add(F4,text='ภาพรวม')
###########################################################
'''
menul = Menu(Mafin)
Mafin.config(menu=menul)

menus = Menu(menul,tearoff=0)

menul.add_cascade(label='menu',menu=menus)
'''
##################################################





Mafin.mainloop() 