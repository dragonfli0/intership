import sys
import time
import tkinter as tk
import webbrowser
from tkinter import ttk
from PIL import Image, ImageTk

# создание окна
root = tk.Tk()
root.title('Мое окно')
root.geometry('1000x1000')
root.configure(bg='#a3b18a')

# создание вкладок
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

tab1 = tk.Frame(notebook)
notebook.add(tab1, text='Вкладка 1')
tab1['bg'] = '#dad7cd'

tab2 = tk.Frame(notebook)
notebook.add(tab2, text='Вкладка 2')
tab2['bg'] = '#dad7cd'

tab3 = tk.Frame(notebook)
notebook.add(tab3, text='Вкладка 3')
tab3['bg'] = '#dad7cd'

tab4 = tk.Frame(notebook)
notebook.add(tab4, text='Вкладка 4')
tab4['bg'] = '#dad7cd'

# картинки для вкладок
# Список изображений для первой вкладки
image_files = ["sua1.jpg", "mizi1.jpg", "suamizi.jpg", "ms.jpg"]
current_image_index = 0


def change_image():
    global current_image_index, bg_photo
    # Загружаем следующее изображение
    bg_image = Image.open(image_files[current_image_index])
    bg_image = bg_image.resize((1000, 1000), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Обновляем изображение в label
    bg_label.config(image=bg_photo)

    # Переходим к следующему изображению
    current_image_index = (current_image_index + 1) % len(image_files)

    # Планируем следующую смену через 3 секунды
    root.after(3000, change_image)


# Загружаем первое изображение
bg_image = Image.open(image_files[0])
bg_image = bg_image.resize((1000, 1000), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(tab1, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Запускаем смену изображений
root.after(3000, change_image)

bg_image2 = Image.open("luka.jpg")
bg_image2 = bg_image2.resize((1000, 1000), Image.Resampling.LANCZOS)
bg_photo2 = ImageTk.PhotoImage(bg_image2)
bg_label2 = tk.Label(tab2, image=bg_photo2)
bg_label2.place(x=0, y=0, relwidth=1, relheight=1)

# Для третьей вкладки
tab3_images = ["ivan.jpg", "ivanAA.jpg"]  # [0] - обычное состояние, [1] - при нажатии
current_tab3_image = 0  # 0 - обычное, 1 - нажатое


def update_tab3_image():
    global bg_photo3
    # Загружаем текущее изображение
    bg_image3 = Image.open(tab3_images[current_tab3_image])
    bg_image3 = bg_image3.resize((1000, 1000), Image.Resampling.LANCZOS)
    bg_photo3 = ImageTk.PhotoImage(bg_image3)
    # Обновляем изображение
    bg_label3.config(image=bg_photo3)
    bg_label3.image = bg_photo3  # Сохраняем ссылку


def on_button_press(event):
    global current_tab3_image
    # Показываем изображение для нажатого состояния
    current_tab3_image = 1
    update_tab3_image()


def on_button_release(event):
    global current_tab3_image
    # Возвращаем изображение для обычного состояния
    current_tab3_image = 0
    update_tab3_image()


# Загружаем первое изображение для 3-й вкладки (обычное состояние)
bg_image3 = Image.open(tab3_images[0])
bg_image3 = bg_image3.resize((1000, 1000), Image.Resampling.LANCZOS)
bg_photo3 = ImageTk.PhotoImage(bg_image3)
bg_label3 = tk.Label(tab3, image=bg_photo3)
bg_label3.place(x=0, y=0, relwidth=1, relheight=1)

bg_image4 = Image.open("till.webp")
bg_image4 = bg_image4.resize((1000, 1000), Image.Resampling.LANCZOS)
bg_photo4 = ImageTk.PhotoImage(bg_image4)
bg_label4 = tk.Label(tab4, image=bg_photo4)
bg_label4.place(x=0, y=0, relwidth=1, relheight=1)

# создание кнопок
button1 = tk.Button(tab1, relief="flat", bg="#ffd6ff")
button1.place(x=100, y=100, width=50, height=50)

button2 = tk.Button(tab2, relief="flat", bg="#ffc300")
button2.place(x=100, y=100, width=50, height=50)

button3 = tk.Button(tab3, relief="flat", bg="#000814")
button3.place(x=100, y=100, width=50, height=50)
# Привязываем события к кнопке
button3.bind("<ButtonPress-1>", on_button_press)  # Нажатие кнопки мыши
button3.bind("<ButtonRelease-1>", on_button_release)  # Отпускание кнопки мыши

button4 = tk.Button(tab4, relief="flat", bg="#62b6cb")
button4.place(x=100, y=100, width=50, height=50)

root.mainloop()