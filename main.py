from tkinter import *
import random


window = Tk()

window.geometry("800x400")
window.title("Камень - Ножницы - Бумага")
window.resizable(width=False, height=False)

frame = Frame(window)
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

name = Label(frame, text="Rock - Paper - Scissors", font="100")
name.place(x=300, y=20)

label1 = Label(frame, text="Player", font="normal 15")
label2 = Label(frame, text="VS", font="normal 15")
label3 = Label(frame, text="Computer", font="normal 15")

label1.place(x=80, y=50, width=100)
label2.place(x=350, y=50, width=100)
label3.place(x=600, y=50, width=100)

scissors_png = PhotoImage(file="scissors.png")
paper_png = PhotoImage(file="paper.png")
rock_png = PhotoImage(file="rock.png")

user_image = Label(frame, image="")
user_image.place(x=80, y=100)

comp_image = Label(frame, image="")
comp_image.place(x=600, y=100)


label4 = Label(frame, text="", font="normal 20", width=15, borderwidth=2, relief="solid")
label4.place(x=275, y=250)


def Rock():
    user = "Rock"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=rock_png)
    if user == computer:
        label4.config(text="Ничья")
        comp_image.config(image=rock_png)
    elif computer == "Paper":
        label4.config(text="Ты проиграл!")
        comp_image.config(image=paper_png)
    else:
        label4.config(text="Ты выиграл!")
        comp_image.config(image=scissors_png)


b1 = Button(frame, text="Камень", font=10, width=20, command=Rock)
b1.place(x=46, y=300)

def Paper():
    user = "Paper"
    user_image.config(image=paper_png)
    computer = random.choice(["Rock", "Paper", "Scissors"])
    if user == computer:
        label4.config(text="Ничья")
        comp_image.config(image=paper_png)
    elif computer == "Scissors":
        label4.config(text="Ты проиграл!")
        comp_image.config(image=scissors_png)
    else:
        label4.config(text="Ты выиграл!")
        comp_image.config(image=rock_png)


b2 = Button(frame, text="Бумага", font=10, width=20, command=Paper)
b2.place(x=283, y=300)
def Scissors():
    user = "Scissors"
    user_image.config(image=scissors_png)
    computer = random.choice(["Rock", "Paper", "Scissors"])
    if user == computer:
        label4.config(text="Ничья")
        comp_image.config(image=scissors_png)
    elif computer == "Rock":
        label4.config(text="Ты проиграл!")
        comp_image.config(image=rock_png)
    else:
        label4.config(text="Ты выиграл!")
        comp_image.config(image=paper_png)


b3 = Button(frame, text="Ножницы", font=10, width=20, command=Scissors)
b3.place(x=520, y=300)

window.mainloop()