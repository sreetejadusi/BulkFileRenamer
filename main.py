from tkinter import *
from tkinter import filedialog
from pathlib import Path
import os

# ----------------------COMMANDS----------------------------
pathlist = []
filenames = []
extensions = []
renamelist = []


class AddFolder:
    def addfolder(self):
        self.folder = filedialog.askdirectory()
        for x in os.listdir(self.folder):
            pathlist.append(os.path.join(self.folder, x))
            filenames.append(Path(x).stem)
            splitter = x.split(".")
            extensions.append(splitter[-1])
        for x in pathlist:
            sourcelist.insert(END, os.path.basename(x))
        renamedlist.delete(0, END)


class AddFiles:
    def addfiles(self):
        self.files = filedialog.askopenfilenames()
        for x in self.files:
            pathlist.append(x)
            filenames.append(Path(x).stem)
            extensions.append(Path(x).name.split(".")[-1])
            sourcelist.insert(END, os.path.basename(x))
        renamedlist.delete(0, END)


class Clear:
    def clear(self):
        pathlist.clear()
        filenames.clear()
        extensions.clear()
        sourcelist.delete(0, END)


class Sort:
    def sort(self):
        pathlist.sort()
        filenames.sort()
        extensions.sort()
        sourcelist.delete(0, END)
        for x in pathlist:
            sourcelist.insert(END, os.path.basename(x))

class Rename:
    def rename(self):
        renamedlist.delete(0, END)
        def replace():
            if checkboxvar.get() == 1:
                replaced = []
                renamedfiles = []
                for x in list(filenames):
                    if entryreplace.get() in x:
                        replaced.append(x.replace(entryreplace.get(), entryreplacewith.get()))
                    else:
                        replaced.append(x)

                zipper = dict(zip(replaced, extensions))
                for x, y in zipper.items():
                    renamedfiles.append(x + '.' + y)
                zipper2 = dict(zip(pathlist, renamedfiles))
                for x, y in zipper2.items():
                    renamelist.append(os.path.join(os.path.dirname(x), y))
                tempdict = dict(zip(pathlist, renamelist))
                for key, value in tempdict.items():
                    os.rename(key, value)
                pathlist.clear()
                filenames.clear()
                renamelist.clear()
                extensions.clear()
                for x in list(renamelist):
                    renamedlist.insert(END, os.path.basename(X))
                sourcelist.delete(0, END)

        def remove():
            if checkboxvar.get() == 3 and lrddchoice.get() == "left":
                removed = []
                removedpath = []
                for x in list(filenames):
                    removed.append(x[int(entryremove.get()):len(x)])
                dict1 = dict(zip(removed, extensions))
                for x, y in dict1.items():
                    removedpath.append(x + '.' + y)
                dict2 = dict(zip(pathlist, removedpath))
                for x, y in dict2.items():
                    renamelist.append(os.path.join(os.path.dirname(x), y))
                finaldict = dict(zip(pathlist, renamelist))
                for x, y in finaldict.items():
                    os.rename(x, y)
                pathlist.clear()
                filenames.clear()
                extensions.clear()
                sourcelist.delete(0, END)
                for x in list(renamelist):
                    renamedlist.insert(END, os.path.basename(X))
                renamelist.clear()

            if checkboxvar.get() == 3 and lrddchoice.get() == "right":
                removedright = []
                removedrightpath = []
                for x in list(filenames):
                    start = 0 - int(entryremove.get())
                    print(start)
                    y = x[start:0:-1]
                    removedright.append(y[::-1])
                dict1right = dict(zip(removedright, extensions))
                for x, y in dict1right.items():
                    removedrightpath.append(x + '.' + y)
                dict2right = dict(zip(pathlist, removedrightpath))
                for x, y in dict2right.items():
                    renamelist.append(os.path.join(os.path.dirname(x), y))
                finaldictright = dict(zip(pathlist, renamelist))
                for x, y in finaldictright.items():
                    os.rename(x, y)
                pathlist.clear()
                filenames.clear()
                extensions.clear()
                sourcelist.delete(0, END)
                for x in list(renamelist):
                    renamedlist.insert(END, os.path.basename(X))
                renamelist.clear()

        def case():
            if checkboxvar.get() == 5:
                cased = []
                casedfiles = []
                if casechoice.get() == "First Letter Upper":
                    for x in list(filenames):
                        cased.append(x.capitalize())
                    dict1 = dict(zip(cased, extensions))
                    for x, y in dict1.items():
                        casedfiles.append(x + '.' + y)
                    dict2 = dict(zip(pathlist, casedfiles))
                    for x, y in dict2.items():
                        renamelist.append(os.path.join(os.path.dirname(x), y))
                    finaldict = dict(zip(pathlist, renamelist))
                    for x, y in finaldict.items():
                        os.rename(x, y)
                    pathlist.clear()
                    filenames.clear()
                    extensions.clear()
                    for x in list(renamelist):
                        renamedlist.insert(END, os.path.basename(X))
                    sourcelist.delete(0, END)
                    renamelist.clear()

                if casechoice.get() == "lower":
                    for x in list(filenames):
                        cased.append(x.lower())
                    dict1 = dict(zip(cased, extensions))
                    for x, y in dict1.items():
                        casedfiles.append(x + '.' + y)
                    dict2 = dict(zip(pathlist, casedfiles))
                    for x, y in dict2.items():
                        renamelist.append(os.path.join(os.path.dirname(x), y))
                    finaldict = dict(zip(pathlist, renamelist))
                    for x, y in finaldict.items():
                        os.rename(x, y)
                    pathlist.clear()
                    filenames.clear()
                    extensions.clear()
                    for x in list(renamelist):
                        renamedlist.insert(END, os.path.basename(X))
                    sourcelist.delete(0, END)
                    renamelist.clear()

                if casechoice.get() == "UPPER":
                    for x in list(filenames):
                        cased.append(x.upper())
                    dict1 = dict(zip(cased, extensions))
                    for x, y in dict1.items():
                        casedfiles.append(x + '.' + y)
                    dict2 = dict(zip(pathlist, casedfiles))
                    for x, y in dict2.items():
                        renamelist.append(os.path.join(os.path.dirname(x), y))
                    finaldict = dict(zip(pathlist, renamelist))
                    for x, y in finaldict.items():
                        os.rename(x, y)
                    pathlist.clear()
                    filenames.clear()
                    extensions.clear()
                    for x in list(renamelist):
                        renamedlist.insert(END, os.path.basename(X))
                    sourcelist.delete(0, END)
                    renamelist.clear()

        def pos():
            if poschoice.get() == 7 and entrytext.get() == "start":
                added = []
                addedfiles = []
                for x in list(filenames):
                    added.append(str(entrytext.get())+str(x))
                dict1 = dict(zip(added, extensions))
                for x,y in dict1.items():
                    addedfiles.append(x+'.'+y)
                dict2 = dict(zip(pathlist, addedfiles))
                for x,y in dict2.items():
                    renamelist.append(os.path.join(os.path.dirname(x), y))
                finaldict = dict(zip(pathlist, renamelist))
                for x,y in finaldict.items():
                    os.rename(x,y)
                pathlist.clear()
                filenames.clear()
                extensions.clear()
                sourcelist.delete(0, END)
                for x in list(renamelist):
                    renamedlist.insert(END, os.path.basename(X))
                renamelist.clear()

            if poschoice.get() == 7 and entrytext.get() == "end":
                added = []
                addedfiles = []
                for x in list(filenames):
                    added.append(str(x) + str(entrytext.get()))
                dict1 = dict(zip(added, extensions))
                for x,y in dict1.items():
                    addedfiles.append(x+'.'+y)
                dict2 = dict(zip(pathlist, addedfiles))
                for x,y in dict2.items():
                    renamelist.append(os.path.join(os.path.dirname(x), y))
                finaldict = dict(zip(pathlist, renamelist))
                for x,y in finaldict.items():
                    os.rename(x,y)
                pathlist.clear()
                filenames.clear()
                extensions.clear()
                sourcelist.delete(0, END)
                for x in list(renamelist):
                    renamedlist.insert(END, os.path.basename(X))
                renamelist.clear()



        replace()
        remove()
        case()


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
rename = Button(firstframe, text="Rename", bg="yellow", fg="#00008b", padx=2, bd=2, width=10, command=Rename().rename)

# ----------------------SECONDFRAME--------------------------
secondframe = Frame(window, bg="blue", padx=10, pady=10)
scrollone = Scrollbar(secondframe)
sourcelist = Listbox(secondframe, bg="#00008b", fg="white", selectmode=MULTIPLE)
sourcelist.config(yscrollcommand=scrollone.set, width=114)
scrollone.config(command=sourcelist.yview)

# ----------------------THIRDFRAME---------------------------
thirdframe = Frame(window, bg="blue", padx=10, pady=10)
modified = Label(thirdframe, text="Renamed Files", fg="white", bg="blue", font=("Arial", 12))

# ----------------------FOURTHFRAME-------------------------

fourthframe = Frame(window, bg="blue", padx=10, pady=10)
scrolltwo = Scrollbar(fourthframe)
renamedlist = Listbox(fourthframe, bg="#00008b", fg="white")
renamedlist.config(yscrollcommand=scrolltwo.set, width=114)
scrolltwo.config(command=renamedlist.yview)

# -----------------------FIFTHFRAME-------------------------
fifthframe = Frame(window, bg="blue", padx=10, pady=10)
# FIFTHSUBONE

fifthsubone = Frame(fifthframe, bg="blue", padx=10, pady=10)
checkboxvar = IntVar()
checkboxreplace = Checkbutton(fifthsubone,
                              text="Replace",
                              variable=checkboxvar,
                              onvalue=1,
                              offvalue=2,
                              bg="blue",
                              fg="black",
                              activeforeground="black",
                              activebackground="blue",
                              font=("Arial", 12)
                              )
entryreplace = Entry(fifthsubone, bg="white", fg="black", font=("Arial", 12), width=16)
labelwith = Label(fifthsubone, bg="blue", fg="white", font=("Arial", 12), text="with")
entryreplacewith = Entry(fifthsubone, bg="white", fg="black", font=("Arial", 12), width=16)

# FIFTHSUBTWO
leftorrightdd = ['left', 'right']
lrddchoice = StringVar()
lrddchoice.set("left")
fifthsubtwo = Frame(fifthframe, bg="blue", padx=10, pady=10)
checkboxremove = Checkbutton(fifthsubtwo,
                             text="Remove",
                             onvalue=3,
                             offvalue=4,
                             variable=checkboxvar,
                             bg="blue",
                             fg="black",
                             activeforeground="black",
                             activebackground="blue",
                             font=("Arial", 12)
                             )
entryremove = Entry(fifthsubtwo, bg="white", fg="black", font=("Arial", 12), width=7)
labelstarting = Label(fifthsubtwo, bg="blue", fg="white", font=("Arial", 12), text="characters")
labelfromthe = Label(fifthsubtwo, bg="blue", fg="white", font=("Arial", 12), text="from the")
leftorright = OptionMenu(fifthsubtwo, lrddchoice, *leftorrightdd)

# FIFTHSUBTHREE
caselist = ['First Letter Upper', 'UPPER', 'lower']
casechoice = StringVar()
casechoice.set('First Letter Upper')
fifthsubthree = Frame(fifthframe, bg="blue", padx=10, pady=10)
checkboxcase = Checkbutton(fifthsubthree,
                           text="Change case to",
                           onvalue=5,
                           offvalue=6,
                           variable=checkboxvar,
                           bg="blue",
                           fg="black",
                           activeforeground="black",
                           activebackground="blue",
                           font=("Arial", 12)
                           )
case = OptionMenu(fifthsubthree, casechoice, *caselist)

# FIFTHSUBFOUR
poslist = ['start', 'end']
poschoice = StringVar()
poschoice.set('start')
fifthsubfour = Frame(fifthframe, bg="blue", padx=10, pady=10)
checkboxadd = Checkbutton(fifthsubfour,
                          text="Add text,",
                          variable=checkboxvar,
                          onvalue=7,
                          offvalue=8,
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
####################END###################################
Label(window, text="Sree Teja Dusi", font=("Comic Sans", 13), fg="white", bg="blue").pack(side=BOTTOM)

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
rename.grid(row=1, column=13, padx=10)
# SECONDFRAME
sourcelist.pack(side=LEFT)
scrollone.pack(side=RIGHT, fill=BOTH)

# THIRDFRAME
modified.pack(side=LEFT)

# FOURTHFRAME
renamedlist.pack(side=LEFT)
scrolltwo.pack(side=RIGHT, fill=BOTH)

# FIFTHFRAME
# FIFTHSUBONE
checkboxreplace.pack(side=LEFT)
entryreplace.pack(side=LEFT, padx=10)
labelwith.pack(side=LEFT)
entryreplacewith.pack(side=LEFT, padx=10)

# FIFTHSUBTWO
checkboxremove.pack(side=LEFT)
entryremove.pack(side=LEFT)
labelstarting.pack(side=LEFT)
labelfromthe.pack(side=LEFT)
leftorright.pack(side=LEFT, padx=5)
# FIFTHSUBTHREE
checkboxcase.pack(side=LEFT)
case.pack(side=LEFT)

# FIFTHSUBFOUR
checkboxadd.pack(side=LEFT)
entrytext.pack(side=LEFT)
labeltext.pack(side=LEFT)
position.pack(side=LEFT, padx=5)
labeltexttwo.pack(side=LEFT)

window.mainloop()