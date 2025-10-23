#1000*1000 поле, в каждой вкладке button 50*50, отступ 100*100, 4 вкладки фон
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
notebook.add(tab1, text = 'Вкладка 1')
tab1['bg'] = '#dad7cd'
tab2 = tk.Frame(notebook)
notebook.add(tab2, text = 'Вкладка 2')
tab2['bg'] = '#dad7cd'
tab3 = tk.Frame(notebook)
notebook.add(tab3, text = 'Вкладка 3')
tab3['bg'] = '#dad7cd'
tab4 = tk.Frame(notebook)
notebook.add(tab4, text = 'Вкладка 4')
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

bg_label = tk.Label(tab1, image = bg_photo)
bg_label.place(x = 0, y = 0, relwidth=1, relheight=1)

# Запускаем смену изображений
root.after(3000, change_image)

bg_image2 = Image.open("luka.jpg") # удалить 4 строчки если гифка
bg_image2 = bg_image2.resize((1000, 1000), Image.Resampling.LANCZOS)
bg_photo2 = ImageTk.PhotoImage(bg_image2)
bg_label2 = tk.Label(tab2, image = bg_photo2)
bg_label2.place(x = 0, y = 0, relwidth=1, relheight=1)
'''# Для анимированного GIF
def animate_gif(label, gif_path, frames):
    def update_frame(frame_index):
        if frame_index < len(frames):
            # Обновляем изображение
            photo = ImageTk.PhotoImage(frames[frame_index])
            label.config(image=photo)
            label.image = photo  # Сохраняем ссылку
            
            # Планируем следующий кадр
            root.after(100, lambda: update_frame(frame_index + 1))
        else:
            # Зацикливаем анимацию
            update_frame(0)
    
    update_frame(0)

# Загружаем GIF и извлекаем кадры
try:
    gif_image = Image.open("Luka.gif")
    gif_frames = []
    
    # Извлекаем все кадры из GIF
    for frame in range(gif_image.n_frames):
        gif_image.seek(frame)
        # Конвертируем в RGB и изменяем размер
        frame_rgb = gif_image.convert('RGB')
        frame_resized = frame_rgb.resize((1000, 1000), Image.Resampling.LANCZOS)
        gif_frames.append(frame_resized)
    
    # Создаем label для GIF
    bg_photo2 = ImageTk.PhotoImage(gif_frames[0])
    bg_label2 = tk.Label(tab2, image=bg_photo2)
    bg_label2.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Запускаем анимацию
    animate_gif(bg_label2, "Luka.gif", gif_frames)
    
except Exception as e:
    print(f"Ошибка загрузки GIF: {e}")
    # Fallback на статичное изображение
    bg_image2 = Image.open("luka.jpg")  # используем jpg как запасной вариант
    bg_image2 = bg_image2.resize((1000, 1000), Image.Resampling.LANCZOS)
    bg_photo2 = ImageTk.PhotoImage(bg_image2)
    bg_label2 = tk.Label(tab2, image=bg_photo2)
    bg_label2.place(x=0, y=0, relwidth=1, relheight=1)'''

bg_image3 = Image.open("ivan.webp") # удалить данную строку 
'''# Список изображений для 3-й вкладки
tab3_images = ["ivan.jpg", "ivanAA.jpg"]
current_tab3_index = 0

# Функция для смены изображения в 3-й вкладке
def change_tab3_image():
    global current_tab3_index, bg_photo3
    # Переходим к следующему изображению
    current_tab3_index = (current_tab3_index + 1) % len(tab3_images)
    # Загружаем новое изображение
    bg_image3 = Image.open(tab3_images[current_tab3_index])
    bg_image3 = bg_image3.resize((1000, 1000), Image.Resampling.LANCZOS)
    bg_photo3 = ImageTk.PhotoImage(bg_image3)
    # Обновляем изображение
    bg_label3.config(image=bg_photo3)
    bg_label3.image = bg_photo3  # Сохраняем ссылку
# Загружаем первое изображение для 3-й вкладки
bg_image3 = Image.open(tab3_images[0])'''
bg_image3 = bg_image3.resize((1000, 1000), Image.Resampling.LANCZOS)
bg_photo3 = ImageTk.PhotoImage(bg_image3)
bg_label3 = tk.Label(tab3, image = bg_photo3)
bg_label3.place(x = 0, y = 0, relwidth=1, relheight=1)

bg_image4 = Image.open("till.webp")
bg_image4 = bg_image4.resize((1000, 1000), Image.Resampling.LANCZOS)
bg_photo4 = ImageTk.PhotoImage(bg_image4)
bg_label4 = tk.Label(tab4, image = bg_photo4)
bg_label4.place(x = 0, y = 0, relwidth=1, relheight=1)
# создание кнопок
button = tk.Button(tab1, relief = "flat", bg= "#ffd6ff" )
button.place(x = 100, y = 100, width = 50, height = 50)
button = tk.Button(tab2, relief = "flat", bg= "#ffc300" )
button.place(x = 100, y = 100, width = 50, height = 50)
button = tk.Button(tab3, relief = "flat", bg= "#000814" ) # удалить эту и след строку для смены фоток вкладки 3
button.place(x = 100, y = 100, width = 50, height = 50) #
'''button3 = tk.Button(tab3, relief = "flat", bg= "#000814", command=change_tab3_image)
button3.place(x = 100, y = 100, width = 50, height = 50)'''
button = tk.Button(tab4, relief = "flat", bg= "#62b6cb" )
button.place(x = 100, y = 100, width = 50, height = 50)


root.mainloop()