##import test_backend
##meters = StringVar()
##meters.set(test_backend.my_function())
##ttk.Label(mainframe, textvariable=meters).grid(column=3, row=3, sticky=W)

#here
import backend
from tkinter import *
from tkinter import ttk

def refresh(*args):
    try:
        print("yeah")
    except ValueError:
        pass

root = Tk()
root.title("Snakescan")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#here
value = StringVar()
value.set(backend.get_cpu_stats()[0])
ttk.Label(mainframe, text="Physical Cores").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, textvariable=value).grid(column=3, row=1, sticky=W)


value2 = StringVar()
value2.set(backend.get_cpu_stats()[1])
ttk.Label(mainframe, text="Logical Cores").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, textvariable=value2).grid(column=3, row=2, sticky=W)


value3 = StringVar()
value3.set(backend.get_cpu_stats()[2])
ttk.Label(mainframe, text="CPU Freq.").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, textvariable=value3).grid(column=3, row=3, sticky=W)

value4 = StringVar()
#value4.set(backend.get_cpu_stats()[3])
ttk.Label(mainframe, text="CPU").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, textvariable=value).grid(column=3, row=4, sticky=W)




#ttk.Label(mainframe, textvariable=str()backend.get_cpu_stats()[0]).grid(column=3, row=1, sticky=W)




ttk.Button(mainframe, text="Refresh", command=refresh).grid(column=2, row=5, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", refresh)

root.mainloop()