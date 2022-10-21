from tkinter import *
window=Tk()


window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightgreen')

def calculate_SI () :
    principal = int(principal_e.get())
    rate=int(rate_e.get())
    time=int(time_e.get())
    i = ((principal*rate*time)/100)
    i = round(i,2)
    output_msg = Label(result_frame,text='Interest on Rs. '+ str(principal) + ' at the rate of interest '+ str(rate) +' % for '+str(time) +' years is Rs. '+ str(i),bg='lightcyan',font=('Calibri',12),bd=1,width=65)    
    output_msg.place(x=20,y=40)
    output_msg.pack()


app_label=Label(window, text="Simple Interest Calculator", fg = "black", bg = "lightgreen", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principal_label=Label(window, text="Enter Principal", fg = "black", bg = "lightgreen", font=("Calibri", 12),bd=1)
principal_label.place(x=20, y=90)

principal_e=Entry(window, text="", bd=2, width=15)
principal_e.place(x=150, y=92)

rate_label=Label(window,text='Enter Rate',fg='black',bg='lightgreen',font=('Calibri',12),bd=1)
rate_label.place(x=20,y=140)

rate_e = Entry(window,text='',bd=2,width=15)
rate_e.place(x=150,y=142)

time_label=Label(window,text='Enter Time',fg='black',bg='lightgreen',font=('Calibri',12),bd=1)
time_label.place(x=20,y=185)

time_e = Entry(window,text='',bd=2,width=15)
time_e.place(x=150,y=187)


result_frame = LabelFrame(window,text="Result", bg = "lightgreen", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightgreen", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

calculate_button = Button(window,text="Calculate",fg='black',bg='white',bd=4,command=calculate_SI)
calculate_button.place(x=20,y=250)

window.mainloop()