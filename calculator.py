from tkinter import *                                                   # importing the tkinter module

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
    
def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnEquals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
cal = Tk()
cal.title("Calculator by Omid Jabbarian")
# icon = PhotoImage(file='image.png') # icon image change
operator=""
text_Input= StringVar()

#==========================================================================================================================================================
# graphic part for my calculator


txtDisplay = Entry(cal, font=('arial', 20,"bold"), textvariable=text_Input, bd=30, insertwidth=4,bg="orange", justify="right").grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="7", command=lambda:btnClick(7), bg="orange").grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="8", command=lambda:btnClick(8),bg="orange").grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9),bg="orange").grid(row=1,column=2)
btn_add=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+"),bg="orange").grid(row=1,column=3)

btn4=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4),bg="orange").grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5),bg="orange").grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6),bg="orange").grid(row=2,column=2)
btn_times=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*"),bg="orange").grid(row=2,column=3)

btn1=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1),bg="orange").grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2),bg="orange").grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3),bg="orange").grid(row=3,column=2)
btn_minus=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick("-"),bg="orange").grid(row=3,column=3)

btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick(0),bg="orange").grid(row=4,column=0)
btn_clear=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="C",bg="orange",command=btnClear).grid(row=4,column=1)
btn_equals=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="=",bg="orange",command=btnEquals).grid(row=4,column=2)
btn_div=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/"),bg="orange").grid(row=4,column=3)

#===========================================================================================================================================================
cal.mainloop()