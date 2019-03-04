from tkinter import *

def ClickButton(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def ClearButton():
    global operator
    operator=""
    text_Input.set(operator)

def EqualButton():
    global operator
    operator=str(eval(operator))
    text_Input.set(operator)

cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_Input, bd= 30,
                   insertwidth = 4,bg="powder blue",
                   justify='right').grid(columnspan=4)

btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda:ClickButton(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda:ClickButton(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda:ClickButton(9)).grid(row=1,column=2)

plus=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda:ClickButton("+")).grid(row=1,column=3)

############################

btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda:ClickButton(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda:ClickButton(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",command=lambda:ClickButton(6)).grid(row=2,column=2)

minus=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda:ClickButton("-")).grid(row=2,column=3)

###################################

btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda:ClickButton(1)).grid(row=3,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda:ClickButton(2)).grid(row=3,column=1)

btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",command=lambda:ClickButton(3)).grid(row=3,column=2)

cross=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="x",bg="powder blue",command=lambda:ClickButton("*")).grid(row=3,column=3)

###############################

btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda:ClickButton(0)).grid(row=4,column=0)

clear=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="powder blue",command=ClearButton).grid(row=4,column=1)

equals=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",command=EqualButton).grid(row=4,column=2)

divide=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda:ClickButton("/")).grid(row=4,column=3)

cal.mainloop()
