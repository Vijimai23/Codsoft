from tkinter import *
from tkinter import messagebox
import random
import string

# Create the root window

root = Tk()
root.geometry('500x400')
root.title("Password Generator")

#defining function

def generate_password():
    length = int(text_field.get())

    if length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    password_var.set(password)
    text_field.delete(0,END)

#creating main_frame

main_frame = Frame(root,bg='pink',highlightbackground='black',highlightthickness=5,width=450,height=300)
main_frame.place(x=10,y=10)        


#creating label_frame

label_frame = Label(main_frame,bg='lavender',font=('bold',18), text="Enter Password Length:")
label_frame.place(x=92,y=15)

#creating text_field

text_field = Entry(main_frame,font=('bold',18))
text_field.place(x=90,y=70)

#creating Button to generate password

button = Button(main_frame, bg='lavender',font=('bold',18),text="Generate Password", command=generate_password)
button.place(x=105,y=120)

#creating a label_frame to display generated password

password_var = StringVar()
label_frame1 = Label(main_frame,bg='lavender',font=('bold',18),text="Generated Password")
label_frame1.place(x=100,y=230)

#creating text_field to display password

text_field2 = Entry(main_frame,bg='lavender',font=('bold',16), textvariable=password_var, state='readonly', width=30)
text_field2.place(x=50,y=180)

root.mainloop()