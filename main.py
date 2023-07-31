# Импортируем библиотеку tkinter для создания графического интерфейса
from tkinter import *

# Импортируем модуль random для генерации случайных ходов компьютера
import random

# Создаём главное окно
window = Tk()

# Задаём размер и заголовок окна
window.geometry("800x400")
window.title("Камень - Ножницы - Бумага")
window.resizable(width=False, height=False)

# Создаём фрейм для размещения элементов игры
frame = Frame(window)
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

# Создаём метку для отображения заголовка игры
name = Label(frame, text="Камень - Ножницы - Бумага", font="100")
name.place(x=275, y=20)

# Создаём метки для отображения "Игрок" и "Компьютер"
label1 = Label(frame, text="Игрок", font="normal 15")
label2 = Label(frame, text="VS", font="normal 15")
label3 = Label(frame, text="Компьютер", font="normal 15")

label1.place(x=80, y=50, width=100)
label2.place(x=350, y=50, width=100)
label3.place(x=600, y=50, width=110)

# Загружаем изображения для ножниц, бумаги и камня
scissors_png = PhotoImage(file="scissors.png")
paper_png = PhotoImage(file="paper.png")
rock_png = PhotoImage(file="rock.png")

# Создаём метки для отображения выбранных изображений игрока и компьютера
user_image = Label(frame, image="")
user_image.place(x=80, y=100)

comp_image = Label(frame, image="")
comp_image.place(x=600, y=100)

# Создаём метку для отображения результата игры
label4 = Label(frame, text="", font="normal 20", width=15, borderwidth=2, relief="solid")
label4.place(x=275, y=250)

# Функция для обработки нажатия кнопки "Камень"
def Rock():
    user = "Камень"
    computer = random.choice(["Камень", "Бумага", "Ножницы"])
    user_image.config(image=rock_png)
    if user == computer:
        label4.config(text="Ничья")
        comp_image.config(image=rock_png)
    elif computer == "Бумага":
        label4.config(text="Ты проиграл!")
        comp_image.config(image=paper_png)
    else:
        label4.config(text="Ты выиграл!")
        comp_image.config(image=scissors_png)

# Создаём кнопку для хода "Камень"
b1 = Button(frame, text="Камень", font=10, width=20, command=Rock)
b1.place(x=46, y=300)

# Функция для обработки нажатия кнопки "Бумага"
def Paper():
    user = "Бумага"
    user_image.config(image=paper_png)
    computer = random.choice(["Камень", "Бумага", "Ножницы"])
    if user == computer:
        label4.config(text="Ничья")
        comp_image.config(image=paper_png)
    elif computer == "Ножницы":
        label4.config(text="Ты проиграл!")
        comp_image.config(image=scissors_png)
    else:
        label4.config(text="Ты выиграл!")
        comp_image.config(image=rock_png)

# Создаём кнопку для хода "Бумага"
b2 = Button(frame, text="Бумага", font=10, width=20, command=Paper)
b2.place(x=283, y=300)

# Функция для обработки нажатия кнопки "Ножницы"
def Scissors():
    user = "Ножницы"
    user_image.config(image=scissors_png)
    computer = random.choice(["Камень", "Бумага", "Ножницы"])
    if user == computer:
        label4.config(text="Ничья")
        comp_image.config(image=scissors_png)
    elif computer == "Камень":
        label4.config(text="Ты проиграл!")
        comp_image.config(image=rock_png)
    else:
        label4.config(text="Ты выиграл!")
        comp_image.config(image=paper_png)

# Создаём кнопку для хода "Ножницы"
b3 = Button(frame, text="Ножницы", font=10, width=20, command=Scissors)
b3.place(x=520, y=300)

# Запускаем главный цикл событий для отображения окна и обработки действий пользователя.
window.mainloop()
