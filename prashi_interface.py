from daredive import kek
from tkinter import *   
 
canvas_bg = "#b2d4fa"

root = Tk()             
root.title('gawkgawk3000')

root.geometry('600x600')
 
label=Label(root,text='swapnil fucks surat fast and hard').place(x=200,y=20) 

def submitFunction() :
    print('Submit button is clicked.')

btn = Button(root, text = 'rope', bd = '5',height=5,width=30, command = lambda: kek())
btn.place(x=200,y=40)
btn = Button(root, text = 'whip', bd = '5',height=5,width=30)
btn.place(x=200,y=140)  
btn = Button(root, text = 'handcuffs', bd = '5',height=5,width=30)
btn.place(x=200,y=240)                                                                        
btn = Button(root, text = 'dildo', bd = '5',height=5,width=30)
btn.place(x=200,y=340)
btn = Button(root, text = 'limit reached', bd = '5',height=5,width=30)
btn.place(x=200,y=440)

root.mainloop()