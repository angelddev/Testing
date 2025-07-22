import tkinter as tk
import re


root = tk.Tk()

root.title("Calculator yepaaaaaa")
root.geometry("500x500")

# FRONT END 

# Data entry placement
entry = tk.Entry(width=100, borderwidth=1.5, font=("Arial", 30))
entry.grid(row=0, columnspan=5, padx=5, ipady=10)


# Grid implementation and space assignation
for n in range (0,5):
    root.grid_rowconfigure(n, weight=1)
    root.grid_columnconfigure(n, weight=1)


# First a dictionary for every button in the calculator with (shown value, read value) (except for C and =, since does will be implemented apart)
buttons = [
    ("1", 1), ("2", 2), ("3", 3), ("+", "+"),  
    ("4", 4), ("5", 5), ("8", 6), ("-", "-"), 
    ("7", 7), ("8", 8), ("9", 9), ("x", "*"),
    (".", "."), ("0", 0), ("/", "/"), ("DEL", "DEL")
]
button_objects = {}

# Button function assignment
ncol = 0
nrow = 1

for label, value in buttons:
    if(ncol>3):
        ncol=0
        nrow+=1
    button_objects[label] = tk.Button(root, font=("Arial", 15), text=label, padx=40, pady=50, command=lambda val=value: button_func(val))
    button_objects[label].grid(row=nrow, column=ncol, padx=5, pady=5)
    ncol+=1
  
for n in range (1, 1000):
    print (n)


button_objects["C"] = tk.Button(root, font=("Arial", 15), text="C", padx=40, pady=100, command=lambda: button_func("C"))
button_objects["="] = tk.Button(root, font=("Arial", 15), text="=", padx=40, pady=100, command=lambda: button_func("="))
button_objects["C"].grid(row=1, rowspan=2, column=4, padx=5, pady=5)
button_objects["="].grid(row=3, rowspan=2, column=4, padx=5, pady=5)

#  BACK END


#   Button logic and functions 

expression=""
last_expression=""
def button_func(action):
    global expression
    global last_expression

    if isinstance(action, int):
       if last_expression=="=":
          expression=""
          last_expression=""
       expression = expression + str(action)
       entry.delete(0, tk.END)
       entry.insert(0, expression)

    elif action in "+-*/": 
        if (len(expression)>0 and expression[-1] in "+-/*.") or (len(expression)==0 and action in "/x"):
            return
        expression = expression + str(action)
        entry.delete(0, tk.END)
        entry.insert(0, expression)
        last_expression=""

    elif action == ".":
        if last_expression=="=":
          expression=""
          last_expression=""
        current_number = re.split(r'[+\-*/]', expression)[-1]
        if "." in current_number:
            return
        if (len(expression)>0 and expression[-1] in ".") or (len(expression)==0 and action in "/x"):
            return
        expression = expression + str(action)
        entry.delete(0, tk.END)
        entry.insert(0, expression)
        last_expression=""
 
    elif action == "=":
        try:
            result = round(eval(expression), 2)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
            expression = str(result)
            last_expression="="
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
            expression = ""
    elif action =="C":
        entry.delete (0, tk.END)
        expression=""
    elif action =="DEL":
        if expression:
            expression = expression[:-1]
            entry.delete(0, tk.END)
            entry.insert(0, expression)

    
root.mainloop()