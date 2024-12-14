from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")


def store():
    global tsteps, tcals, log
    s = steps.get()
    c = cals.get()
    a = activity.get()
    tcals += c
    tsteps += s
    log.append(a)
    messagebox.showinfo(title="Success", message="Activity logged succesfully!")


def summary():
    d = ""
    for i in lists:
        if i in log:
            c = log.count(i)
            d += f"{i}:{c}\n"

    summary1 = f"- Steps:{tsteps}\n-Calories Burned:{tcals}\n-Activities:\n-{d}"
    messagebox.showinfo(title="Daily Summary", message=sum)


tsteps = 0
tcals = 0
log = []
l1 = Label(text="Fitness Tracker",
           font=("Arial", 30, "bold"),
           bg="black",
           fg="white")
l2 = Label(text="Enter Steps",
           font=("Arial", 15, "bold"),
           bg="black",
           fg="white")
steps = IntVar()
cals = IntVar()
e1 = Entry(textvariable=steps)
l3 = Label(text="Enter Calories Burned",
           font=("Arial", 15, "bold"),
           bg="black",
           fg="white")
e2 = Entry(textvariable=cals)
l4 = Label(text="Select Activity",
           font=("Arial", 15, "bold"),
           bg="black",
           fg="white")
lists = ["Walking", "Yoga", "Cycling", "Dancing", "Playing Sports"]
activity = StringVar(value=lists[0])
op1 = OptionMenu(root, activity, *lists)
b1 = Button(text="Log activity", command=store)
b2 = Button(text="Show Daliy Summary", command=summary)
l1.pack(pady=10)
l2.pack()
e1.pack()
l3.pack()
e2.pack()
l4.pack()
op1.pack()
b1.pack(pady=10)
b2.pack()
root.mainloop()
