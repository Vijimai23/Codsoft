from tkinter import *
root=Tk()
root.geometry("500x500")
root.title('Task1-Basic Calculator')

#function 
operator=''
def Buttonclick(number):
    global operator
    operator=operator+number
    text_field.delete(0,END)
    text_field.insert(END,operator)
 
def clear():
    global operator
    text_field.delete(0,END)
    operator=''

def answer():
    global operator
    result=str(eval(operator))
    text_field.delete(0,END)
    text_field.insert(0,result)

#creating main frame
main_frame=Frame(root,bg='dark blue',highlightthickness=5,highlightbackground='black',width=300,height=410)
main_frame.place(x=85,y=10)

# creating text field
label_name=Label(main_frame,bg='white',text='CALCULATOR',font=('bold',20))
label_name.place(x=50,y=10)
text_field=Entry(main_frame,bg='white',highlightthickness=3,highlightbackground='black',bd=5,font=('bold',20),width=13)
text_field.place(x=5,y=70)

#creating buttons
button_clear=Button(main_frame,bg='red',text='c',font=('bold',20),width=3,command=clear)
button_clear.place(x=225,y=65)

#row 1  
button7=Button(main_frame,text='7',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("7"))
button7.place(x=10,y=130)
button8=Button(main_frame,text='8',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("8"))
button8.place(x=85,y=130)
button9=Button(main_frame,text='9',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("9"))
button9.place(x=150,y=130)
button_div=Button(main_frame,text='/',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("/"))
button_div.place(x=225,y=130)

#row 2
button4=Button(main_frame,text='4',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("4"))
button4.place(x=10,y=200)
button5=Button(main_frame,text='5',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("5"))
button5.place(x=85,y=200)
button6=Button(main_frame,text='6',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("6"))
button6.place(x=150,y=200)
button_mul=Button(main_frame,text='x',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("*"))
button_mul.place(x=225,y=200)

#row 3
button1=Button(main_frame,text='1',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("1"))
button1.place(x=10,y=270)
button2=Button(main_frame,text='2',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("2"))
button2.place(x=85,y=270)
button3=Button(main_frame,text='3',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("3"))
button3.place(x=150,y=270)
button_sub=Button(main_frame,text='-',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("-"))
button_sub.place(x=225,y=270)

#row4
button_dot=Button(main_frame,text='.',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("."))
button_dot.place(x=10,y=340)
button0=Button(main_frame,text='0',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("0"))
button0.place(x=85,y=340)
button_equal=Button(main_frame,text='=',bg='white',font=('bold',20),width=3,command=answer)
button_equal.place(x=150,y=340)
button_add=Button(main_frame,text='+',bg='white',font=('bold',20),width=3,command=lambda:Buttonclick("+"))
button_add.place(x=225,y=340)

root.mainloop()