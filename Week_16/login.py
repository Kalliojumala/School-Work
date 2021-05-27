

#Tkinter commands/Notes

#Parts of GUI are activated by using 'pack()- method'

#Fill, fills the gui 
#Default : NONE 
#Args: x , y or BOTH 

#Expand
#Default : NO 
#if given value YES fills empty space with parent object attributes/params/size

#Side
#Default : TOP
#Args: BOTTOM, LEFT, RIGHT

from tkinter import *

#Test function for TkInter!
def button_press():
    #User inputs 
    user_name = input_username.get()
    user_password = input_password.get()

    #Generate a welcome message
    message = Label(text=f"Welcome {user_name}!", fg='red', bg='black', width=30, height=5)
    message.place(x=5, y=150)
    
    #Delete temp inputs
    v_user_name.delete(0, END)
    v_user_password.delete(0, END)
    


#Create window
window = Tk()

#Title for the window
window.title('Login TkInter practice')

#Window resolution
window.geometry('500x500')

#Label 1
username = Label(text='Username', fg='red', bg='black')
username.place(x=5, y=10)

#Label 2
password = Label(text='Password',fg='red',bg='black')
password.place(x=5, y=50)

#Button with size, colour ja width
press_me = Button(text='Log in',fg='red', bg='black', command=button_press)
press_me.place(x=5, y=90)

#Add input windows for username and password
input_username = StringVar()
v_user_name = Entry(textvariable=input_username)

input_password = StringVar()
v_user_password = Entry(textvariable=input_password)

v_user_name.place(x= 5, y=30)
v_user_password.place(x=5, y=70)


#Main loop
window.mainloop()
