from tkinter import *
import time

root = Tk()
root.title("Clock By Nitin")
root.geometry('1300x450+0+0')
root.config(bg='#081923')


def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))

    # configuration to display it AM or PM
    if int(h) > 12 and int(m) > 0:
        day.config(text='PM')
    # to convert 24hrs clock to 12hrs
    if int(h) > 12:
        h = str((int(h) - 12))

    hr.config(text=h)
    min.config(text=m)
    sec.config(text=s)

    # to change every 200 sec
    hr.after(200, clock)


# ----------------Hour----------------------------
hr = Label(root, text='Digital Clock By Nitin', font=('NOW', 50, 'bold'), bg='#00B5EB', fg='white')
hr.place(x=350, y=50)

# ----------------Hour----------------------------
hr = Label(root, text='12', font=('DS-Digital', 70, 'bold'), bg='#00B5EB', fg='white')
hr.place(x=350, y=200, width=150, height=150)

hr2 = Label(root, text='Hour', font=('Now', 20, 'bold'), bg='#00B5EB', fg='white')
hr2.place(x=350, y=360, width=150, height=50)

# ----------------Minute----------------------------
min = Label(root, text='60', font=('DS-Digital', 70, 'bold'), bg='#00B5EB', fg='white')
min.place(x=520, y=200, width=150, height=150)

min2 = Label(root, text='Minute', font=('Now', 20, 'bold'), bg='#00B5EB', fg='white')
min2.place(x=520, y=360, width=150, height=50)

# ----------------Second----------------------------
sec = Label(root, text='60', font=('DS-Digital', 70, 'bold'), bg='#00B5EB', fg='white')
sec.place(x=690, y=200, width=150, height=150)

sec2 = Label(root, text='Second', font=('NOW', 20, 'bold'), bg='#00B5EB', fg='white')
sec2.place(x=690, y=360, width=150, height=50)

# ----------------AM/PM----------------------------
day = Label(root, text='AM', font=('NOW', 60, 'bold'), bg='#FF2D00', fg='white')
day.place(x=860, y=200, width=150, height=150)

day2 = Label(root, text='Time', font=('NOW', 20, 'bold'), bg='#FF2D00', fg='white')
day2.place(x=860, y=360, width=150, height=50)

clock()
root.mainloop()
