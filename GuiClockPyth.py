from tkinter import *
import time
root=Tk()
root.title("GUI Clock")
root.geometry('400x400')
root.config(bg='white')
def clock():
    hr=time.strftime('%I')
    mi=time.strftime('%M')
    sc=time.strftime('%S')
    day=time.strftime('%A')
    am_pm=time.strftime('%p')
    zn=time.strftime('%Z')
    L1.config(text=hr+':'+mi+':'+sc+" "+am_pm)
    L1.after(1000,clock)
    L2.config(text='Day: '+day)
    L3.config(text='Time Zone: '+zn)
L1= Label(root, text='', font= ('Arial', 28, 'bold'), fg= 'white', bg= 'black')
L1.pack(pady= 100)
L2= Label(root, text= '', font= ('Arial', 14), fg='white', bg= 'black')
L2.pack(pady= 5)
L3= Label(root, text="", font= ('Arial', 14), fg= 'white', bg= 'black')
L3.pack(pady= 5)
clock()
root.mainloop()


