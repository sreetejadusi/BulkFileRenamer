from tkinter import *
from tkinter import filedialog
import os

# ----------------------COMMANDS----------------------------
filelist = []
pathlist = []


class AddFolder:
    def addfolder(self):
        self.folder = filedialog.askdirectory()
        for x in os.listdir(self.folder):
            filelist.append(x)
        for x in filelist:
            sourcelist.insert(END, x)

        for i in filelist:
            self.filepath = os.path.join(self.folder, i)
            pathlist.append(self.filepath)


class AddFiles:
    def addfiles(self):
        self.files = filedialog.askopenfilenames()
        for x in self.files:
            pathlist.append(x)
            filelist.append(os.path.basename(x))
            sourcelist.insert(END, os.path.basename(x))


class Clear:
    def clear(self):
        filelist.clear()
        pathlist.clear()
        sourcelist.delete(0, END)


class Sort:
    def sort(self):
        filelist.sort()
        pathlist.sort()
        sourcelist.delete(0, END)
        for x in filelist:
            sourcelist.insert(END, x)


# ----------------------GUI---------------------------------
window = Tk()
window.geometry("800x700")
window.config(bg="blue")
window.title("Renamer by Sree Teja Dusi")

# ----------------------FIRSTFRAME---------------------------
firstframe = Frame(window, bg="blue", padx=10, pady=10)
selection = Label(firstframe, text="Source Files", fg="white", bg="blue", font=("Arial", 12))
addfolder = Button(firstframe, text="Add Folder", bg="white", fg="#00008b", padx=2, bd=2, width=10,
                   command=AddFolder().addfolder)
addfiles = Button(firstframe, text="Add Files", bg="white", fg="#00008b", padx=2, bd=2, width=10,
                  command=AddFiles().addfiles)
removesel = Button(firstframe, text="Remove Selection", bg="white", fg="#00008b", padx=2, bd=2, width=10)
clear = Button(firstframe, text="Clear", bg="white", fg="#00008b", padx=2, bd=2, width=10, command=Clear().clear)
sort = Button(firstframe, text="Sort", bg="white", fg="#00008b", padx=2, bd=2, width=10, command=Sort().sort)
preview = Button(firstframe, text="Preview", bg="white", fg="#00008b", padx=2, bd=2, width=10)
rename = Button(firstframe, text="Rename", bg="yellow", fg="#00008b", padx=2, bd=2, width=10)

# ----------------------SECONDFRAME--------------------------
secondframe = Frame(window, bg="blue", padx=10, pady=10)
scrollone = Scrollbar(secondframe)
sourcelist = Listbox(secondframe, bg="#00008b", fg="white", selectmode=MULTIPLE)
sourcelist.config(yscrollcommand=scrollone.set, width=114)
scrollone.config(command=sourcelist.yview)

# ----------------------THIRDFRAME---------------------------
thirdframe = Frame(window, bg="blue", padx=10, pady=10)
modified = Label(thirdframe, text="Renamed Files", fg="white", bg="blue", font=("Arial", 12))
total = Label(thirdframe, text="Total Files To Be Renamed: ", bg="blue", fg="white", font=("Arial", 12))
current = Label(thirdframe, text="Current Operation: ", bg="blue", fg="white", font=("Arial", 12))

# ----------------------FOURTHFRAME-------------------------

fourthframe = Frame(window, bg="blue", padx=10, pady=10)
scrolltwo = Scrollbar(fourthframe)
renamedlist = Listbox(fourthframe, bg="#00008b", fg="white")
renamedlist.config(yscrollcommand=scrolltwo.set, width=114)
scrolltwo.config(command=renamedlist.yview)

# -----------------------FIFTHFRAME-------------------------
dropdown = ['Including Extension', 'Excluding Extension']
extchoice = StringVar()
extchoice.set('Excluding Extension')
fifthframe = Frame(window, bg="blue", padx=10, pady=10)

# FIFTHSUBONE

fifthsubone = Frame(fifthframe, bg="blue", padx=10, pady=10)
checkboxreplacevar = IntVar()
checkboxreplace = Checkbutton(fifthsubone,
                              text="Replace",
                              variable=checkboxreplacevar,
                              onvalue=1,
                              offvalue=0,
                              bg="blue",
                              fg="black",
                              activeforeground="black",
                              activebackground="blue",
                              font=("Arial", 12)
                              )
entryreplace = Entry(fifthsubone, bg="white", fg="black", font=("Arial", 12), width=16)
casecheckreplacevar = IntVar()
casecheckreplace = Checkbutton(fifthsubone,
                               text="(case-sensitive) with,",
                               variable=casecheckreplacevar,
                               onvalue=1,
                               offvalue=0,
                               bg="blue",
                               fg="black",
                               activeforeground="black",
                               activebackground="blue",
                               font=("Arial", 12)
                               )
entryreplacewith = Entry(fifthsubone, bg="white", fg="black", font=("Arial", 12), width=16)
isextreplace = OptionMenu(fifthsubone, extchoice, *dropdown)

# FIFTHSUBTWO
checkboxremovevar = IntVar()
leftorrightdd = ['left', 'right']
lrddchoice = StringVar()
lrddchoice.set("left")
fifthsubtwo = Frame(fifthframe, bg="blue", padx=10, pady=10)
checkboxremove = Checkbutton(fifthsubtwo,
                             text="Remove",
                             onvalue=1,
                             offvalue=0,
                             variable=checkboxremovevar,
                             bg="blue",
                             fg="black",
                             activeforeground="black",
                             activebackground="blue",
                             font=("Arial", 12)
                             )
entryremove = Entry(fifthsubtwo, bg="white", fg="black", font=("Arial", 12), width=7)
labelstarting = Label(fifthsubtwo, bg="blue", fg="white", font=("Arial", 12), text="characters, starting(including)")
entryremoveincl = Entry(fifthsubtwo, bg="white", fg="black", font=("Arial", 12), width=7)
labelfromthe = Label(fifthsubtwo, bg="blue", fg="white", font=("Arial", 12), text="from the")
leftorright = OptionMenu(fifthsubtwo, lrddchoice, *leftorrightdd)
isextremove = OptionMenu(fifthsubtwo, extchoice, *dropdown)

# FIFTHSUBTHREE
caselist = ['First Letter Upper', 'UPPER', 'lower']
casechoice = StringVar()
casechoice.set('First Letter Upper')
fifthsubthree = Frame(fifthframe, bg="blue", padx=10, pady=10)
checkboxcasevar = IntVar()
checkboxcase = Checkbutton(fifthsubthree,
                           text="Change case to",
                           onvalue=1,
                           offvalue=0,
                           variable=checkboxcasevar,
                           bg="blue",
                           fg="black",
                           activeforeground="black",
                           activebackground="blue",
                           font=("Arial", 12)
                           )
case = OptionMenu(fifthsubthree, casechoice, *caselist)
isextcase = OptionMenu(fifthsubthree, extchoice, *dropdown)

# FIFTHSUBFOUR
poslist = ['start', 'end']
poschoice = StringVar()
poschoice.set('start')
fifthsubfour = Frame(fifthframe, bg="blue", padx=10, pady=10)
checkboxaddvar = IntVar()
checkboxadd = Checkbutton(fifthsubfour,
                          text="Add text,",
                          variable=checkboxaddvar,
                          onvalue=1,
                          offvalue=0,
                          bg="blue",
                          fg="black",
                          activeforeground="black",
                          activebackground="blue",
                          font=("Arial", 12)
                          )
entrytext = Entry(fifthsubfour, bg="white", fg="black", font=("Arial", 12), width=20)
labeltext = Label(fifthsubfour, bg="blue", fg="white", font=("Arial", 12), text="to the")
position = OptionMenu(fifthsubfour, poschoice, *poslist)
labeltexttwo = Label(fifthsubfour, bg="blue", fg="white", font=("Arial", 12), text="end of each filename")
isextcase = OptionMenu(fifthsubthree, extchoice, *dropdown)

# FRAMES
firstframe.pack()
secondframe.pack()
thirdframe.pack()
fourthframe.pack()
fifthframe.pack()
# FIFTHSUBS
fifthsubone.pack()
fifthsubtwo.pack()
fifthsubthree.pack()
fifthsubfour.pack()

# Elements
# FIRST FRAME
selection.grid(row=1, column=1, padx=10)
addfolder.grid(row=1, column=3, padx=10)
addfiles.grid(row=1, column=5, padx=10)
clear.grid(row=1, column=7, padx=10)
sort.grid(row=1, column=9, padx=10)
preview.grid(row=1, column=11, padx=10)
rename.grid(row=1, column=13, padx=10)
# SECONDFRAME
sourcelist.pack(side=LEFT)
scrollone.pack(side=RIGHT, fill=BOTH)

# THIRDFRAME
modified.pack(side=LEFT)
total.pack(side=LEFT, padx=10)
current.pack(side=RIGHT, padx=120)

# FOURTHFRAME
renamedlist.pack(side=LEFT)
scrolltwo.pack(side=RIGHT, fill=BOTH)

# FIFTHFRAME
# FIFTHSUBONE
checkboxreplace.pack(side=LEFT)
entryreplace.pack(side=LEFT)
casecheckreplace.pack(side=LEFT)
entryreplacewith.pack(side=LEFT)
isextreplace.pack(side=RIGHT, padx=5)

# FIFTHSUBTWO
checkboxremove.pack(side=LEFT)
entryremove.pack(side=LEFT)
labelstarting.pack(side=LEFT)
entryremoveincl.pack(side=LEFT)
labelfromthe.pack(side=LEFT)
leftorright.pack(side=LEFT, padx=5)
isextremove.pack(side=RIGHT)
# FIFTHSUBTHREE
checkboxcase.pack(side=LEFT)
case.pack(side=LEFT)
isextcase.pack(side=RIGHT, padx=5)

# FIFTHSUBFOUR
checkboxadd.pack(side=LEFT)
entrytext.pack(side=LEFT)
labeltext.pack(side=LEFT)
position.pack(side=LEFT, padx=5)
labeltexttwo.pack(side=LEFT)
isextcase.pack(side=LEFT)

window.mainloop()
