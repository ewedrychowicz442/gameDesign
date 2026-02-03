import tkinter as tk

is_on =  False
def say_hi():
    global is_on
    is_on = not is_on

    if is_on:
        label.config(text="You clicked the button!", bg="green")
        button.config(text = "Unclick me!", bg= "red")
    else:
        label.config(text="You unclicked the button!",bg="red")
        button.config(text = "Click me!", bg= "green")

        
#create the main window
root = tk.Tk()
root.title("My First TKinter Project!")
root.geometry("400x300")

label = tk.Label(root, text="Hello, TKinter", font=("Arial", 28))
label.pack()

button = tk.Button(root, text =  "Click Me!", font=("Arial", 28),command = say_hi)
button.pack()
#runs the program above
root.mainloop()
