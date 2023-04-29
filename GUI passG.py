from tkinter import *
import pyperclip
import random as rd
import os

win = Tk()
win.title("PassGenerator")
win.resizable(0, 0)

base = ""
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

amal = ['+', '-', '*', '^', '/']

symbols = ['?', '!', '@', '#', '$', '%', '&', '(', ')', '_']

upperletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

List_saves = []

def generate():
    global base
    global x
    global pwd
    length = int(Scle.get())
    base = ""
    x = len(pwd) - 1
    if (var_4.get() == 0):
        input_pass.set("GetBetter")
    elif (var_4.get() == 1):
        while length != 0:
            length -= 1
            rd_pass = pwd[rd.randint(0, x)]
            base = str(base) + str(rd_pass)
            input_pass.set(base)

def dark_mode():
    Frm_choose.configure(bg="#2C3539", fg="#C2DFFF")
    btn_rd.configure(bg="#36454F", fg="#C2DFFF", activebackground="#8D918D")
    btn_saves.configure(bg="#36454F", fg="#C2DFFF", activebackground="#8D918D")
    btn_darkmode.configure(bg="#36454F", fg="#C2DFFF", activebackground="#8D918D", command= lambda:light_mode())

    Frm_Generator.configure(bg="#2C3539")
    Scle.configure(bg="#2C3539", fg="#C2DFFF", activebackground="#C2DFFF")

    checkbox_1.configure(bg="#2C3539", fg="#C2DFFF", selectcolor="#000000", activebackground="#2C3539", )
    checkbox_2.configure(bg="#2C3539", fg="#C2DFFF", selectcolor="#000000", activebackground="#2C3539", )
    checkbox_3.configure(bg="#2C3539", fg="#C2DFFF", selectcolor="#000000", activebackground="#2C3539", )
    checkbox_4.configure(bg="#2C3539", fg="#C2DFFF", selectcolor="#000000", activebackground="#2C3539", )

    btn_generate.configure(bg="#2E1A47", fg="#C2DFFF")

    btn_save.configure(bg="black", fg="#ADDFFF")

    Frm_Saves.configure(bg="#2C3539")
    List.configure(bg="#2C3539", fg="#C2DFFF")
    btn_copy.configure(bg="#1F6357", fg="#AAF0D1")
    btn_delete.configure(bg="#1F6357", fg="#AAF0D1")

    Lighting_mode.set("LightMode")

def light_mode():
    Frm_choose.configure(bg="white", fg="black")
    btn_rd.configure(bg="white", fg="black", activebackground="#E5E4E2")
    btn_saves.configure(bg="white", fg="black", activebackground="#E5E4E2")
    btn_darkmode.configure(bg="white", fg="black", activebackground="#E5E4E2", command= lambda:dark_mode())

    Frm_Generator.configure(bg="white")
    Scle.configure(bg="white", fg="#3D3C3A", activebackground="#3D3C3A")

    checkbox_1.configure(bg="white", fg="black", selectcolor="white", activebackground="white")
    checkbox_2.configure(bg="white", fg="black", selectcolor="white", activebackground="white")
    checkbox_3.configure(bg="white", fg="black", selectcolor="white", activebackground="white")
    checkbox_4.configure(bg="white", fg="black", selectcolor="white", activebackground="white")

    btn_generate.configure(bg="#98AFC7", fg="black")

    btn_save.configure(bg="#ADDFFF", fg="black")

    Frm_Saves.configure(bg="white")
    List.configure(bg="white", fg="black")
    btn_copy.configure(bg="#ADDFFF", fg="black")
    btn_delete.configure(bg="#ADDFFF", fg="black")

    Lighting_mode.set("DarkMode")

def includings():
    global pwd
    global x
    global amal
    global upperletters
    try:
        if (var_1.get() == 1):
            pwd = pwd + amal
        elif(var_1.get() == 0):
            pwd = [i for i in pwd if i not in amal]
        if (var_2.get() == 1):
            pwd = pwd + symbols
        elif(var_2.get() == 0):
            pwd = [i for i in pwd if i not in symbols]
        if (var_3.get() == 1):
            pwd = pwd + upperletters
        elif(var_3.get() == 0):
            pwd = [i for i in pwd if i not in upperletters]
    except:
        pass

def copy_save():
    if (input_pass.get() != "" and input_pass.get() != "GetBetter" and input_pass.get() != List.get("end")):
        pyperclip.copy(input_pass.get())
        List_saves.append(input_pass.get())
        List.insert("end", input_pass.get())
    else:
        pass

def list_copy():
    try:
        y = List.curselection()
        pyperclip.copy(List.get(y))
    except:
        pass

def list_delete():
    try:
        y = List.curselection()
        List.delete(y)
    except:
        pass

def saves_frame():
    Frm_Generator.pack_forget()
    Frm_Saves.pack(side=RIGHT)

def rd_frame():
    Frm_Saves.pack_forget()
    Frm_Generator.pack(side=RIGHT)

###Frame Choose###
Frm_choose = LabelFrame(win, width=120, height=350, text="Modes", bg="white", fg="black")
Frm_choose.pack(side=LEFT)

Lighting_mode = StringVar()
Lighting_mode.set("DarkMode")

btn_rd = Button(Frm_choose, text="Rd Pass", height=2, width=10, cursor="hand2", relief=GROOVE, bg="white", fg="black", activebackground="#E5E4E2", command=rd_frame)
btn_saves = Button(Frm_choose, text="Copies", height=2, width=10, cursor="hand2", relief=GROOVE, bg="white", fg="black", activebackground="#E5E4E2", command=saves_frame)
btn_darkmode = Button(Frm_choose, textvariable=Lighting_mode, height=2, width=10, cursor="hand2", bg="white", fg="black", activebackground="#E5E4E2", relief=GROOVE, command= lambda: dark_mode())

btn_rd.place(x=20, y=40)
btn_saves.place(x=20, y=120)
btn_darkmode.place(x=20, y=200)

###Frame Genetator###
Frm_Generator = Frame(win, width=400, height=350, bg="white")
Frm_Generator.pack(side=RIGHT)

#Scale
Scale_var = DoubleVar()
Scle = Scale(Frm_Generator, from_=1, to=20, variable=Scale_var, length=300, width=20, orient= HORIZONTAL, borderwidth=0, border=0, highlightthickness=0, bg="white", fg="#3D3C3A", activebackground="#3D3C3A")
Scle.place(x=50 , height=70)
Scle.set(8)

#CheckBoxes
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()

var_4.set(1)

checkbox_1 = Checkbutton(Frm_Generator, text="Include amal riazi", font=("Vani", 11), variable=var_1, onvalue=1, offvalue=0, cursor="hand2", bg="white", fg="black", selectcolor="white", activebackground="white", command=includings)
checkbox_2 = Checkbutton(Frm_Generator, text="Include symbols", font=("Vani", 11), variable=var_2, onvalue=1, offvalue=0, cursor="hand2", bg="white", fg="black", selectcolor="white", activebackground="white", command=includings)
checkbox_3 = Checkbutton(Frm_Generator, text="Include Upperletters", font=("Vani", 11), variable=var_3, onvalue=1, offvalue=0, cursor="hand2", bg="white", fg="black", selectcolor="white", activebackground="white", command=includings)
checkbox_4 = Checkbutton(Frm_Generator, text="Are you ok?", font=("Vani", 11), variable=var_4, onvalue=1, offvalue=0, cursor="hand2", bg="white", fg="black", selectcolor="white", activebackground="white")

checkbox_1.place(x= 20, y=100)
checkbox_2.place(x= 220, y=100)
checkbox_3.place(x= 20, y=150)
checkbox_4.place(x= 220, y=150)

#result
input_pass = StringVar()
Frm_input = Frame(Frm_Generator, width=300, height=50, highlightbackground="black", highlightcolor="black", highlightthickness=3)
Frm_input.place(x=45, y=230)

Ent_input = Entry(Frm_input, justify=CENTER, textvariable=input_pass, font=('arial', 16, 'bold'), width=25, cursor="arrow", state=DISABLED, disabledbackground='white', disabledforeground='black')
Ent_input.pack()

#Generate button
btn_generate = Button(Frm_Generator, text="Generate", width=8, height=3, relief=GROOVE, bg="#98AFC7", cursor="hand2", borderwidth=2,  activebackground='#D5D6EA', command=generate)
btn_generate.place(x= 160, y= 280)

#Save Button
btn_save = Button(Frm_Generator, text="copy", width=5, height=1, relief=GROOVE, bg="#ADDFFF", cursor="hand2", borderwidth=2,  activebackground='#D5D6EA', command=lambda: copy_save())
btn_save.place(x= 355, y=234)

###Frame_Saves###
Frm_Saves= Frame(win, width=400, height=350, bg="white")

scroll_y = Scrollbar(Frm_Saves,orient=VERTICAL)
scroll_y.pack(side=RIGHT, fill=Y)
List = Listbox(Frm_Saves, yscrollcommand=scroll_y.set, selectmode=SINGLE, width=63, height=18, borderwidth=0, border=0, bg="white", fg="black")
scroll_y.config(command=List.yview)
List.pack()

btn_delete = Button(Frm_Saves, text="delete", width=53, height=1, relief=GROOVE, bg="#ADDFFF", cursor="hand2", borderwidth=2,  activebackground='#00827F', command=list_delete)
btn_delete.pack(side=BOTTOM)

btn_copy = Button(Frm_Saves, text="copy", width=53, height=1, relief=GROOVE, bg="#ADDFFF", cursor="hand2", borderwidth=2,  activebackground='#00827F', command=list_copy)
btn_copy.pack(side=BOTTOM)

win.mainloop()
