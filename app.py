import tkinter as tk

def draw_shapes(canvas):
    # Rectangle
    canvas.create_rectangle(50, 50, 150, 100, fill="blue")

    # Oval (Ellipse)
    canvas.create_oval(200, 50, 300, 150, fill="green")

    # Line
    canvas.create_line(350, 50, 450, 100, fill="red")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Graphic Model with Tkinter")

    # Create a canvas widget to draw on
    canvas = tk.Canvas(root, width=500, height=200)
    canvas.pack()

    # Call the function to draw shapes
    draw_shapes(canvas)

    # Start the main event loop
    root.mainloop()