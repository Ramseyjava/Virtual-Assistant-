from tkinter import *
from tkinter.ttk import  Progressbar
import time
import sys
 

#from home import Home
root =Tk()

height =450
width = 550

x= (root.winfo_screenwidth()//2)-(width//2)
y= (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}*{}+{}+{}'.format(width, height, x, y))

root.overrideredirect(1)
root.config(background='#b800c4')


# exit_btn = Button(root, text='x', voice_data =lambda: exit_window(), font("yu gothic ui", 19, 'bold'), bg='#b800c4')
# exit_btn.place(x=200, y=30)

welcome_label = Label(root, text = 'welcome to my app', font("yu gothic ui", 19, 'bold'), bg ='#b800c4')


progress_label =Label(root, text='please wait...', font=("yu gothic ui", 19, 'bold'), bg='#b800c4')
progress_label.place(x=450, y=300)

progress = Progressbar(root, orient= HORIZONTAL, length=500, mode='determinate')
progress.place(x=370, y=400)


def exit_window():
    sys.exit(root.destroy())
    


        

i = 0

        
def load():
            
    global i
    if i <= 10:
        txt = 'Please wait...' +(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(100, load)
        progress ['value'] = 10*i
        i += 1
    else:
        false


load()       
root.mainloop()
                       

        


        


    

        

    

        #============================================================================
        #==============================DESIGN PART===================================
        #============================================================================



       

       


        #================Buttons===================
      
