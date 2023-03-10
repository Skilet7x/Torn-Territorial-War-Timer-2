from tkinter import *

root = Tk()
root.title("Torn Territorial War Timer")
root.iconbitmap('torn.ico')

def calculate():
    top = Toplevel()
    top.title("Torn Territorial War Timer")
    top.iconbitmap('torn.ico')
    total = e1.get()
    taken = e2.get()
    points = int(total) - int(taken)
    slots = e3.get()
    counter = 0
    while True:
        counter = counter + 1
        if int(counter) > int(slots):
            break
        else:
            pass
        days = int(points)/(int(counter)*86400)
        hours = (days % 1)*24
        minutes = (hours % 1)*60
        seconds = (minutes % 1)*60
        if counter < 10 and counter > 0:
            ans = Label(top, text=" {} მოთამაშე      ...   {} დღე {} საათი {} წუთი და {} წამი.".format(int(counter), int(days // 1), int(hours // 1), int(minutes // 1), int(seconds // 1)))
            ans.grid(row = counter - 1, column = 0, sticky=W)
            continue
        elif counter >= 10:
            ans = Label(top, text=" {} მოთამაშე    ...   {} დღე {} საათი {} წუთი და {} წამი.".format(int(counter), int(days // 1), int(hours // 1), int(minutes // 1), int(seconds // 1)))
            ans.grid(row = counter - 1, column = 0, sticky=W)
            continue

l1 = Label(root, text="ტერიტორიის მთლიანი ქულების რაოდენობა (Points):")
e1 = Entry(root)
l2 = Label(root, text="ტერიტორიის დაპყრობილი ქულების რაოდენობა:")
e2 = Entry(root)
l3 = Label(root, text="ტერიტორიის ზომა (Slots):")
e3 = Entry(root)
submit = Button(root, text="Submit", padx = 16, command=calculate)

l1.grid(row = 0, column = 0, sticky=W)
e1.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0, sticky=W)
e2.grid(row = 1, column = 1)
l3.grid(row = 2, column = 0, sticky=W)
e3.grid(row = 2, column = 1)
submit.grid(row = 3, column = 1, sticky=E)

root.mainloop()