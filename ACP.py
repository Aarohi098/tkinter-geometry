from tkinter import *

window = Tk()
window.title('Number Pad')
window.geometry('250x350')

nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]
hidden_text = ""

def update_display(value):
    global hidden_text
    hidden_text += str(value)
    display_label.config(text="*" * len(hidden_text))

for i in range(4):
    window.columnconfigure(i, weight=1, minsize=50)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        number = nums[i][j]
        btn = Button(window, text=number, bg="#a28de1", command=lambda v=number: update_display(v))
        btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)

display_label = Label(window, text="", )
display_label.grid(row=4, column=0, columnspan=3, pady=10)

btn1 = Button(window, text="Save password")
btn1.grid(row=5, column=0, columnspan=3, pady=5)
        
window.mainloop()


