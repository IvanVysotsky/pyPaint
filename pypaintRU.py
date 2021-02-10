# -*- coding: utf8 -*-

from tkinter import *

canvas_width = 1000
canvas_height = 500
brush_size = 3
color = "black"


def paint(event):
  global brush_size
  global color
  x1 = event.x - brush_size
  x2 = event.x + brush_size
  y1 = event.y - brush_size
  y2 = event.y + brush_size
  w.create_oval(x1, y1, x2, y2,
                fill=color, outline=color)


def brish_size_change(new_size):
  global brush_size
  brush_size = new_size


def color_change(new_color):
  global color
  color = new_color


root = Tk()
root.title("PyPaint by Ivan Vysotsky dev.")

w = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           bg="white")
w.bind("<B1-Motion>", paint)

red_btn = Button(text="Красный", width=10,
                 command=lambda: color_change("red"))
blue_btn = Button(text="Синий", width=10,
                  command=lambda: color_change("blue"))
black_btn = Button(text="Чёрный", width=10,
                   command=lambda: color_change("black"))
yellow_btn = Button(text="Жёлтый", width=10,
                    command=lambda: color_change("yellow"))
green_btn = Button(text="Зелёный", width=10,
                   command=lambda: color_change("green"))
orange_btn = Button(text="Оранжевый", width=10,
                    command=lambda: color_change("orange"))

white_btn = Button(text="Ластик", width=10,
                   command=lambda: color_change("white"))
clear_btn = Button(text="Очистить", width=10,
                   command=lambda: w.delete("all"))
pencil_btn = Button(text="Карандаш", width=10,
                    command=lambda: brish_size_change(1))

five_btn = Button(text="5", width=10,
                  command=lambda: brish_size_change(5))
standart_btn = Button(text="Стандартный", width=10,
                      command=lambda: brish_size_change(3))
ten_btn = Button(text="10", width=10,
                 command=lambda: brish_size_change(10))
fifteen_btn = Button(text="15", width=10,
                     command=lambda: brish_size_change(15))
twenty_btn = Button(text="20", width=10,
                    command=lambda: brish_size_change(20))
thirty_btn = Button(text="30", width=10,
                    command=lambda: brish_size_change(30))

size_lbl = Label(text="Размер кисти:", width=10)
color_lbl = Label(text="Цвет:", width=10)
fun_lbl = Label(text="Доп. функции:", width=11)

w.grid(row=3, column=0,
       columnspan=7, padx=5,
       pady=5, sticky=E + W + S + N)

#кисть -- brush
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

#цвета -- color
red_btn.grid(row=0, column=1)
blue_btn.grid(row=0, column=2)
black_btn.grid(row=0, column=3)
yellow_btn.grid(row=0, column=4)
green_btn.grid(row=0, column=5)
orange_btn.grid(row=0, column=6)

#размер -- size
standart_btn.grid(row=1, column=1)
five_btn.grid(row=1, column=2)
ten_btn.grid(row=1, column=3)
fifteen_btn.grid(row=1, column=4)
twenty_btn.grid(row=1, column=5)
thirty_btn.grid(row=1, column=6)

#функции -- function
white_btn.grid(row=2, column=2)
clear_btn.grid(row=2, column=3)
pencil_btn.grid(row=2, column=1)

#надписи -- Label
size_lbl.grid(row=1, column=0)
color_lbl.grid(row=0, column=0)
fun_lbl.grid(row=2, column=0)

# параметры окана -- window preferens
root.resizable(False, False)
root.mainloop()

