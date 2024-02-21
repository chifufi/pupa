import tkinter as tk

def show_text_window():
    text = "pupa pupa pupa"
    
    # Создание нового окна
    window = tk.Toplevel(root)
    window.title("Вывод текста")
    
    # Установка размера нового окна
    window.geometry("300x100")
    
    # Создание метки для вывода текста
    label = tk.Label(window, text=text)
    label.pack(padx=20, pady=20)

# Создание основного окна
root = tk.Tk()
root.title("Главное окно")
root.geometry("200x100")
# Создание кнопки
button = tk.Button(root, text="Показать текст", command=show_text_window)
button.pack(padx=50, pady=20)

root.mainloop()