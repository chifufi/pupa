import tkinter as tk

def show_text_window():
    text = "pupa pupa pupa"
    
    # Создание нового окна
    window = tk.Toplevel(root)
    window.title("Вывод текста")
    
    # Создание метки для вывода текста
    label = tk.Label(window, text=text)
    label.pack(padx=20, pady=20)

# Создание основного окна
root = tk.Tk()
root.title("Главное окно")

# Создание кнопки
button = tk.Button(root, text="Показать текст", command=show_text_window)
button.pack(padx=50, pady=20)

root.mainloop()