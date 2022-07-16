from tkinter import *
from tkinter import filedialog
import webbrowser

window = Tk()
window.geometry("800x600")
window.config(bg="blue")
window.title("Renamer by Sree Teja Dusi")

#----------------------FIRSTFRAME---------------------------
firstframe = Frame(window, bg="blue", padx=10, pady=10)
selection = Label(firstframe, text="Source Files", fg="white", bg="blue", font=("Arial", 12))
addfolder = Button(firstframe, text="Add Folder", bg="white", fg="#00008b", padx=2, bd=2 ,width=10)
addfiles = Button(firstframe, text="Add Files", bg="white", fg="#00008b", padx=2,  bd=2 ,width=10)
removesel = Button(firstframe, text="Remove Selection", bg="white", fg="#00008b", padx=2,  bd=2 ,width=10)
clear = Button(firstframe, text="Clear", bg="white", fg="#00008b", padx=2,  bd=2 ,width=10)
sort = Button(firstframe, text="Sort", bg="white", fg="#00008b", padx=2,  bd=2 ,width=10)
preview = Button(firstframe, text="Preview", bg="white", fg="#00008b", padx=2,  bd=2 ,width=10)
rename = Button(firstframe, text="Rename", bg="yellow", fg="#00008b", padx=2,  bd=2 ,width=10)

#----------------------SECONDFRAME--------------------------
secondframe = Frame(window, bg="blue", padx=10, pady=10)
scrollone = Scrollbar(secondframe)
sourcelist = Listbox(secondframe, bg="#00008b",fg="white")
sourcelist.config(yscrollcommand=scrollone.set, width=114)
scrollone.config(command=sourcelist.yview)

#----------------------THIRDFRAME---------------------------
thirdframe = Frame(window, bg="blue", padx=10, pady=10)
modified = Label(thirdframe, text="Renamed Files", fg="white", bg="blue", font=("Arial", 12))
total = Label(thirdframe, text="Total Files To Be Renamed: ",bg="blue", fg="white",font=("Arial", 12))
current = Label(thirdframe, text="Current Operation: ",bg="blue", fg="white",font=("Arial", 12))

#----------------------FOURTHFRAME-------------------------

fourthframe = Frame(window, bg="blue", padx=10, pady=10)
scrolltwo = Scrollbar(fourthframe)
renamedlist = Listbox(fourthframe, bg="#00008b",fg="white")
renamedlist.config(yscrollcommand=scrolltwo.set, width=114)
scrolltwo.config(command=renamedlist.yview)





#FRAMES
firstframe.pack()
secondframe.pack()
thirdframe.pack()
fourthframe.pack()


#Elements
#FIRST FRAME
selection.grid(row=1, column=1, padx=10)
addfolder.grid(row=1, column=3 ,padx=10)
addfiles.grid(row=1, column=5, padx=10)
clear.grid(row=1, column=7, padx=10)
sort.grid(row=1, column=9, padx=10)
preview.grid(row=1, column=11, padx=10)
rename.grid(row=1, column=13, padx=10)
#SECONDFRAME
sourcelist.pack(side=LEFT)
scrollone.pack(side=RIGHT, fill=BOTH)
for x in range(1,100):
    sourcelist.insert(END,x)
#THIRDFRAME
modified.pack(side=LEFT)
total.pack(side=LEFT, padx=10)
current.pack(side=RIGHT, padx=120)
#FOURTHFRAME
renamedlist.pack(side=LEFT)
scrolltwo.pack(side=RIGHT, fill=BOTH)
for x in range(1,100):
    renamedlist.insert(END,x)


window.mainloop()