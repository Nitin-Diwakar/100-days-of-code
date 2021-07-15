from tkinter import *

import random
from tkinter import messagebox


win = Tk()
win.title("Hand Game")
win.iconbitmap('yellowrockon_116074.ico')
# width = 650
# height = 600
win.maxsize(width=650, height=600)
win.minsize(width=650, height=600)
win.config(bg="#99ff99")

# ================================IMAGE BACKGROUND========================================
bgImage = PhotoImage(file=r"images/background.png")
Label(win, image=bgImage).place(relwidth=1, relheight=1)

# ================================ ALL IMAGES========================================
blank_img = PhotoImage(file="images/blank.png")
player_rock = PhotoImage(file="images/rock.png")
sm_player_rock = player_rock.subsample(3, 3)
player_paper = PhotoImage(file="images/paper.png")
sm_player_paper = player_paper.subsample(3, 3)
player_scissor = PhotoImage(file="images/scissor.png")
sm_player_scissor = player_scissor.subsample(3, 3)
com_rock = PhotoImage(file="images/com_rock.png")
com_paper = PhotoImage(file="images/com_paper.png")
com_scissor = PhotoImage(file="images/com_scissor.png")
s = PhotoImage(file="images/s.png")
r = PhotoImage(file="images/r.png")
p = PhotoImage(file="images/p.png")

# ================================USER IMAGES========================================
ls = PhotoImage(file="images/lscissor.png")
lr = PhotoImage(file="images/lrock.png")
lp = PhotoImage(file="images/lpaper.png")

# ================================COMPUTER IMAGES========================================
rr = PhotoImage(file="images/rrock.png")
rp = PhotoImage(file="images/rpaper.png")
rs = PhotoImage(file="images/rscissor.png")
# ===============================METHODS=============================================
score_com = IntVar()
score_you = IntVar()

# ===============================FUNCTIONS=============================================


def Rock():
    # global player_choice
    # player_choice = 1
    # player_img.configure(image=player_rock)
    # MatchProcess()
    global player_choice
    player_choice = 1

    player_img.configure(image=lr)
    MatchProcess()


def Paper():
    global player_choice
    player_choice = 2

    player_img.configure(image=lp)
    # player_img.configure(image=player_paper)
    MatchProcess()


def Scissor():
    global player_choice
    player_choice = 3

    player_img.configure(image=ls)
    # player_img.configure(image=player_scissor)
    MatchProcess()


def MatchProcess():
    com_choice = random.randint(1, 3)
    if com_choice == 1:
        comp_img.configure(image=rr)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=rp)
        ComputerPaper()

    elif com_choice == 3:
        comp_img.configure(image=rs)
        CompututerScissor()


def ComputerRock():
    if player_choice == 1:
        lbl_status.config(text="Game Tie")
    elif player_choice == 2:
        lbl_status.config(text="Player Win")
        score_you.set(score_you.get() + 1)
    elif player_choice == 3:
        lbl_status.config(text="Computer Win")
        score_com.set(score_com.get() + 1)


def ComputerPaper():
    if player_choice == 1:
        lbl_status.config(text="Computer Win")
        score_com.set(score_com.get() + 1)
    elif player_choice == 2:
        lbl_status.config(text="Game Tie")
    elif player_choice == 3:
        lbl_status.config(text="Player Win")
        score_you.set(score_you.get() + 1)


def CompututerScissor():
    if player_choice == 1:
        lbl_status.config(text="Player Win")
        score_you.set(score_you.get() + 1)
    elif player_choice == 2:
        lbl_status.config(text="Computer Win")
        score_com.set(score_com.get() + 1)
    elif player_choice == 3:
        lbl_status.config(text="Game Tie")


def ExitApp():
    win.destroy()
    exit()


def about():
    messagebox.showinfo("About", """Rock paper scissors is a hand game usually played between two people,in which each player simultaneously forms one of three shapes with an outstretched hand.These shapes are 'rock', 'paper', and 'scissors'\n\nRules:\n\nA player who decides to play rock will beat another player who has chosen scissors ('rock crushes scissors' or sometimes 'blunts scissors'), but will lose to one who has played paper ('paper covers rock'); a play of paper will lose to a play of scissors ('scissors cuts paper')\n\n\nDesign By: Nitin Diwakar""")


# ===============================LABEL WIDGET=========================================
player_img = Label(win, image=blank_img)
comp_img = Label(win, image=blank_img)
lbl_player = Label(win, text="YOU")
lbl_player.grid(row=1, column=1)
lbl_player.config(bg="#ffffff")
lbl_computer = Label(win, text="COMPUTER")
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="#ffffff")
lbl_status = Label(win, text="", font=('arial', 15))
lbl_status.config(bg="#ffffff")
player_img.grid(row=2, column=1, padx=30, pady=20)
comp_img.grid(row=2, column=3, pady=10)  # padx not fixing the problem
lbl_status.grid(row=3, column=2)

# ===============================BUTTON WIDGET===================================
rock = Button(win, image=sm_player_rock, command=Rock)
paper = Button(win, image=sm_player_paper, command=Paper)
scissor = Button(win, image=sm_player_scissor, command=Scissor)
btn_quit = Button(win, text="Quit", command=ExitApp, bg='red', fg='white')
rock.grid(row=4, column=1, pady=30)
paper.grid(row=4, column=2, pady=30)
scissor.grid(row=4, column=3, pady=30)
btn_quit.grid(row=5, column=2)

ent2 = Entry(win, textvariable=score_you, width=2,
             font=('Ubuntu', 24), relief=GROOVE)
# ent2.place(x=50,y=50, anchor=CENTER) #relx=0.3, rely=0.85
ent2.grid(row=3, column=1)
ent3 = Entry(win, textvariable=score_com, width=2,
             font=('Ubuntu', 24), relief=GROOVE)
ent3.grid(row=3, column=3)

btn = Button(win, text="About", command=about)
btn.grid(row=6, column=2, pady=5)
# ========================================INITIALIZATION===================================
win.mainloop()
