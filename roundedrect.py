import tkinter as tk

def rounded_rectangle(canvas, x1, y1, x2, y2, radius=50, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    canvas.create_polygon(points, **kwargs, smooth=True)

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=100, bg='white')
canvas.pack()

rounded_rectangle(canvas, 10, 10, 190, 90, radius=60, fill='lightblue', outline='black')
button_text = canvas.create_text(100, 50, text='Click me!', font=('Arial', 12))

root.mainloop()
