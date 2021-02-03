from tkinter import Tk, Canvas, BOTH


class Main:

    root = None
    canvas = None

    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x500+300+300")
        self.root.title("Mouse Tracker")
        self.canvas = Canvas()
        self.canvas.pack()
        self.root.bind('<Motion>', self.motion)

        self.root.mainloop()

    def motion(self, event):
        x, y = event.x, event.y
        self.canvas.delete("all")
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.create_line(0, y, 700, y)
        self.canvas.create_line(x, 0, x, 500)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.create_text(25, 10, fill="black", text="x= {}".format(x))
        self.canvas.create_text(25, 25, fill="black", text="y= {}".format(y))

        return


if __name__ == '__main__':
    Main()
