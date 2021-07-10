from classes import *


class PaintApp(Attributes):

    def __init__(self, master):
        super().__init__(master)
        self.x_pos, self.y_pos = None, None
        self.x_start, self.y_start, self.x_end, self.y_end = None, None, None, None
        self.btn_press = False
        self.canvas.bind("<Motion>", self.track_motion)
        self.canvas.bind("<ButtonPress-1>", self.btn_onclick)
        self.canvas.bind("<ButtonRelease-1>", self.btn_onrelease)

    tool_id = -1
    color_fill = "grey"
    color_line = "black"
    size_line = 1
    input_text = "Paint"

    def track_motion(self, event=None):
        if self.btn_press ==  True:
            if self.tool_id == 0:
                self.pencil(event)
            # print(event.x, event.y)
        pass

    def btn_onclick(self, event=None):
        self.btn_press = True
        self.x_start = event.x
        self.y_start = event.y
        # print("Start: ", self.x_start, self.y_start)

    def btn_onrelease(self, event=None):
        self.btn_press = False
        self.x_pos = None
        self.y_pos = None
        self.x_end = event.x
        self.y_end = event.y
        self.paint()
        # print("End: ", self.x_end, self.y_end)

    def size(self, th):
        size_dialog.destroy()
        global size_line
        self.size_line = th
        self.size_lbl.config(text=th)

    def line_size(self):
        global size_dialog
        size_dialog = Toplevel(self.master)
        size_dialog.title("Outline Size")
        size_dialog.geometry("300x150")
        label = Label(size_dialog, text="Choose Size")
        label.grid(row=0, column=0)
        button1 = Button(size_dialog, text="0", width=4, command=lambda th=0: self.size(th))
        button1.grid(row=1, column=1)
        button2 = Button(size_dialog, text="1", width=4, command=lambda th=1: self.size(th))
        button2.grid(row=1, column=2)
        button2 = Button(size_dialog, text="2", width=4, command=lambda th=2: self.size(th))
        button2.grid(row=1, column=3)
        button2 = Button(size_dialog, text="5", width=4, command=lambda th=5: self.size(th))
        button2.grid(row=1, column=4)
        button2 = Button(size_dialog, text="10", width=4, command=lambda th=10: self.size(th))
        button2.grid(row=2, column=1)
        button2 = Button(size_dialog, text="15", width=4, command=lambda th=15: self.size(th))
        button2.grid(row=2, column=2)
        button2 = Button(size_dialog, text="18", width=4, command=lambda th=18: self.size(th))
        button2.grid(row=2, column=3)
        button2 = Button(size_dialog, text="20", width=4, command=lambda th=20: self.size(th))
        button2.grid(row=2, column=4)

    def color_pick(self, ch):
        global color_fill
        color = tkinter.colorchooser.Chooser(self.master).show()
        if ch == 1:
            self.color_fill = color[1]
            self.color_fill_lbl.config(bg=color[1])
        elif ch == 2:
            self.color_line = color[1]
            self.color_line_lbl.config(bg=color[1])
        else:
            pass

    def color_change(self, event):
        obj = self.canvas.find_closest(event.x, event.y)
        self.canvas.itemconfig(obj, fill="black")

    def line_tool(self):
        self.canvas_obj.append(self.canvas.create_line([self.x_start, self.y_start, self.x_end, self.y_end], width=self.size_line,  fill=self.color_fill))
        self.draw.line([self.x_start, self.y_start, self.x_end, self.y_end], width=self.size_line,  fill=self.color_fill)

    def rect_tool(self):
        self.canvas_obj.append(self.canvas.create_rectangle([self.x_start, self.y_start, self.x_end, self.y_end], width=self.size_line, outline=self.color_line, fill=self.color_fill) )
        self.draw.rectangle([self.x_start, self.y_start, self.x_end, self.y_end], width=self.size_line, outline=self.color_line, fill=self.color_fill)

    def cir_tool(self):
        self.canvas_obj.append(self.canvas.create_oval([self.x_start, self.y_start, self.x_end, self.y_end], width=self.size_line,outline=self.color_line, fill=self.color_fill))
        self.draw.ellipse([self.x_start, self.y_start, self.x_end, self.y_end], width=self.size_line,outline=self.color_line, fill=self.color_fill)

    def pencil(self, event=None):
        if self.x_pos is not None and self.y_pos is not None:
            self.canvas_obj.append(self.canvas.create_line([self.x_pos, self.y_pos, event.x, event.y], width=self.size_line, fill=self.color_fill, smooth=True))
            self.draw.line([self.x_pos, self.y_pos, event.x, event.y], width=self.size_line, fill=self.color_fill)
        self.x_pos = event.x
        self.y_pos = event.y

    def paint(self):
        if self.tool_id == 0:
            self.track_motion
        elif self.tool_id == 1:
            self.line_tool()
        elif self.tool_id == 2:
            self.rect_tool()
        elif self.tool_id == 3:
            self.cir_tool()
        else:
            pass

    def tool(self, id):
        global tool_id
        self.tool_id = id


if __name__ == '__main__':
    root = Tk()
    PaintApp(root)
    root.title('Paint App')
    root.geometry('1250x720')
    root.mainloop()
