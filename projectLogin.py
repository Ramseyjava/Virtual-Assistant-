from tkinter import *
...
#mport tkinter.label

root = Tk()

def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')
def getvals():
    print("Accepted")

#Heading
label = Label(root, text="python registration from", font="ar 15 bold").grid(row=0, column=3)

#field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
Emergence = Label(root, text="Emergence")
payment = Label(root, text="payment mode")

#packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
Emergence.grid(row=4, column=2)
payment.grid(row=5, column=2)


#variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencevalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar


#creating entry field
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
emergenceentry = Entry(root, textvariable = emergencevalue)
paymententry = Entry(root, textvariable = paymentvalue)


#packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergenceentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

#creating checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6,column=3)

#submit button
Button(text="submit", voice_data=getvals).grid(row=7, column=3)




root.mainloop()
