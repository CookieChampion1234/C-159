from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("600x400")

list_name = ["MIckey Mouse", "Elsa", "Anna", "Donald Duck"]
dict_student = {"name" : "Shinchan",
                "age" : "5"}

try:
    print(list_name[5])
    
    print(dict_student["mom"])
    
except IndexError:
    messagebox.showinfo("Error", "This Index does not exist")
except KeyError:
    messagebox.showinfor("Error", "This Key does not exist")
    
root.mainloop