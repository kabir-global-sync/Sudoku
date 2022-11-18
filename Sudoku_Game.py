from tkinter import *
from tkinter import messagebox as msg
import random
import sudokus as sdk

root = Tk()
root.title('Sudoku Game')
root.geometry('400x480')
g_font = ('Roboto', 25)
paned_row_1 = PanedWindow(root, bd=3, relief='raised', bg='black')
paned_row_1.pack(fill='both', expand=1)
row1_box1 = PanedWindow(paned_row_1, bd=3, relief='groove', orient=HORIZONTAL)
row1_box2 = PanedWindow(paned_row_1, bd=3, relief='groove', orient=HORIZONTAL)
row1_box3 = PanedWindow(paned_row_1, bd=3, relief='groove', orient=HORIZONTAL)
paned_row_1.add(row1_box1, width=130, height=20)
paned_row_1.add(row1_box2, width=130, height=20)
paned_row_1.add(row1_box3, width=130, height=20)

paned_row_2 = PanedWindow(root, bd=3, relief='raised', bg='black')
paned_row_2.pack(fill='both', expand=1)
row2_box1 = PanedWindow(paned_row_2, bd=3, relief='groove', orient=HORIZONTAL)
row2_box2 = PanedWindow(paned_row_2, bd=3, relief='groove', orient=HORIZONTAL)
row2_box3 = PanedWindow(paned_row_2, bd=3, relief='groove', orient=HORIZONTAL)
paned_row_2.add(row2_box1, width=130, height=20)
paned_row_2.add(row2_box2, width=130, height=20)
paned_row_2.add(row2_box3, width=130, height=20)

paned_row_3 = PanedWindow(root, bd=3, relief='raised', bg='black')
paned_row_3.pack(fill='both', expand=1)
row3_box1 = PanedWindow(paned_row_3, bd=3, relief='groove', orient=HORIZONTAL)
row3_box2 = PanedWindow(paned_row_3, bd=3, relief='groove', orient=HORIZONTAL)
row3_box3 = PanedWindow(paned_row_3, bd=3, relief='groove', orient=HORIZONTAL)
paned_row_3.add(row3_box1, width=130, height=20)
paned_row_3.add(row3_box2, width=130, height=20)
paned_row_3.add(row3_box3, width=130, height=20)


panelDict={0:row1_box1,1:row1_box2,2:row1_box3,3:row2_box1,4:row2_box2,5:row2_box3,6:row3_box1,7:row3_box2,8:row3_box3}

row1_box1_item = []
row1_box2_item = []
row1_box3_item = []

row2_box1_item = []
row2_box2_item = []
row2_box3_item = []

row3_box1_item = []
row3_box2_item = []
row3_box3_item = []

temp=[]

boxDict={0:row1_box1_item,1:row1_box2_item,2:row1_box3_item,3:row2_box1_item,4:row2_box2_item,5:row2_box3_item,6:row3_box1_item,7:row3_box2_item,8:row3_box3_item}
for box in boxDict:
    for i in range(3):
        for j in range(3):
            e = Entry(panelDict[box], width=2, font=g_font,justify="center")
            e.grid(row=i, column=j)
            temp.append(e)
        boxDict[box].append(temp)
        temp=[]

arr=sdk.sudokuChooser()
for i in range(random.choice([6,8,7,9,6,7,8,9,8])): #selecting all the nine big boxes
    for j in range(random.choice([2,3,4,2,3])): #select j number of small boxes
        for k in range(j):
            c1=random.choice([0,1,2])
            c2=random.choice([0,1,2])
            if boxDict[i][c1][c2].get()=="":
                boxDict[i][c1][c2].insert(0,arr[i][c1][c2])


'''
for i in range(3):
    for j in range(3):
        e = Entry(row1_box1, width=2, font=g_font)
        e.grid(row=i, column=j)
        row1_box1_item.append(e)


##########################################

for i in range(3):
    for j in range(3):
        e = Entry(row1_box2, width=2, font=g_font)
        e.grid(row=i, column=j)
        row1_box2_item.append(e)
#################################################

for i in range(3):
    for j in range(3):
        e = Entry(row1_box3, width=2, font=g_font)
        e.grid(row=i, column=j)
        row1_box3_item.append(e)
######################################################################
######################################################################

for i in range(3):
    for j in range(3):
        e = Entry(row2_box1, width=2, font=g_font)
        e.grid(row=i, column=j)
        row2_box1_item.append(e)
###################################

for i in range(3):
    for j in range(3):
        e = Entry(row2_box2, width=2, font=g_font)
        e.grid(row=i, column=j)
        row2_box2_item.append(e)
###################################

for i in range(3):
    for j in range(3):
        e = Entry(row2_box3, width=2, font=g_font)
        e.grid(row=i, column=j)
        row2_box3_item.append(e)
######################################################################
######################################################################

for i in range(3):
    for j in range(3):
        e = Entry(row3_box1, width=2, font=g_font)
        e.grid(row=i, column=j)
        row3_box1_item.append(e)
###################################

for i in range(3):
    for j in range(3):
        e = Entry(row3_box2, width=2, font=g_font)
        e.grid(row=i, column=j)
        row3_box2_item.append(e)
###################################

for i in range(3):
    for j in range(3):
        e = Entry(row3_box3, width=2, font=g_font)
        e.grid(row=i, column=j)
        row3_box3_item.append(e)

n=random.randint(1,4)
for k in range(n):
    i=random.randint(1,8)
    num=random.randint(1,9)
    row1_box1_item[i].insert(0, f'{num}')
'''

def checker():
    count=0
    for i in range(9):
        box=boxDict[i]
        for j in range(3):
            if int(box[0][j].get())==arr[i][0][j] and int(box[1][j].get())==arr[i][1][j] and int(box[2][j].get())==arr[i][2][j]:
                count+=3
            else:
                msg.showwarning('Sudoku Status','Wrong Arrangement!')
                break
    if count==81:
        msg.showinfo('Sudoku Status','Correct Arrangement!')
                


check_btn=Button(root,text='Check',font=('FixedSys',13),command=checker,bg="black",fg='white')
check_btn.pack(pady=10)
mainloop()
