from tkinter import*
base = Tk()  
base.geometry('500x500')  
base.title("Registration Form")
base.config(bg="light yellow")
labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20),bg= "light yellow")  
labl_0.place(x=90,y=53)  
labl_1 = Label(base,bg= "light yellow",text="FullName",width=20,font=("bold", 10))  
labl_1.place(x=70,y=130)  
entry_1 = Entry(base)  
entry_1.place(x=240,y=130)  
labl_2 = Label(base, text="Email",width=20,font=("bold", 10),bg= "light yellow")  
labl_2.place(x=68,y=180)  
entry_02 = Entry(base)  
entry_02.place(x=240,y=180)  	  
labl_3 = Label(base, text="Gender",width=20,font=("bold", 10),bg= "light yellow")  
labl_3.place(x=70,y=230)  
#varblbl = IntVarblbl()  
Radiobutton(base, text="Male",padx = 5,bg= "light yellow" ,value=1).place(x=235,y=230)  
Radiobutton(base, text="Female",padx = 20,value=2,bg= "light yellow").place(x=290,y=230)
labl_4 = Label(base, text="Age:",width=20,font=("bold", 10),bg= "light yellow")  
labl_4.place(x=70,y=280)
entry_02 = Entry(base)  
entry_02.place(x=240,y=280)    
Button(base, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)  
# it will be used for displaying the registration form onto the window  
base.mainloop()  
print("Registration form is created seccussfully...") 

