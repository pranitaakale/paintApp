from tkinter import *
from tkinter import filedialog
import PIL
from PIL import Image, ImageDraw, ImageTk
from help_desk import help_text
import tkinter.colorchooser, tkinter.messagebox

class Attributes:
    def __init__(self, master):

        self.pencilIcon = PhotoImage(file=r"E:\MyDocuments\Images_Project\pencileIcon.png")
        self.lineIcon = PhotoImage(file=r"E:\MyDocuments\Images_Project\lineIcon.png")
        self.rectIcon = PhotoImage(file=r"E:\MyDocuments\Images_Project\rectIcon.png")
        self.ovalIcon = PhotoImage(file=r"E:\MyDocuments\Images_Project\ovalIcon.png")
        self.fillIcon = PhotoImage(file=r"E:\MyDocuments\Images_Project\fillIcon.png")
        self.outlineIcon = PhotoImage(file=r"E:\MyDocuments\Images_Project\outlineIcon.png")
        self.sizeIcon = PhotoImage(file=r"E:\MyDocuments\Images_Project\sizeIcon.png")
        self.undoIcon = PhotoImage(file=r"E:\MyDocuments\Images_Project\undoIcon.png")

        self.master = master
        self.canvas = Canvas(self.master, width=1050, height=720, bg="white")
        self.tool_frame = Frame(self.master, width=200, height=720, bg="cyan")

        self.sub_tool_frame = Frame(self.tool_frame, width=200, height=150, bg="cyan")
        self.undo_btn = Button(self.sub_tool_frame, image=self.undoIcon, command=self.undo_func)
        self.undo_btn.pack(pady=45, side=TOP)

        self.display = Frame(self.sub_tool_frame, width=200, height=150, bg="cyan")
        self.color_fill_lbl = Label(self.display, width=3, relief=RIDGE)
        self.color_line_lbl = Label(self.display, width=3, relief=RIDGE)
        self.size_lbl = Label(self.display, width=3, relief=RIDGE)

        self.image1 = PIL.Image.new('RGB', (950, 720), 'white')
        self.draw = ImageDraw.Draw(self.image1)
        self.canvas_obj = []
        self.undo = []
        self.menu()
        self.layout()

    def layout(self):
        self.tool_frame.pack(side=LEFT, padx=5, pady=5)
        self.canvas.pack(side=RIGHT, padx=5, pady=5)
        self.display.pack()
        self.sub_tool_frame.pack(pady=50)

        color_fill_btn = Button(self.sub_tool_frame, image=self.fillIcon, width=25, command=lambda: self.color_pick(1), relief=FLAT)
        color_fill_btn.pack(padx=15, pady=10, side=LEFT)
        color_line_btn = Button(self.sub_tool_frame, image=self.outlineIcon, width=25, command=lambda: self.color_pick(2), relief=FLAT)
        color_line_btn.pack(padx=15, pady=10, side=LEFT)
        size_btn = Button(self.sub_tool_frame, image=self.sizeIcon, width=25, command=self.line_size, relief=FLAT)
        size_btn.pack(padx=15, pady=10, side=LEFT)

        self.color_fill_lbl.pack(padx=15, side=LEFT)
        self.color_line_lbl.pack(padx=15, side=LEFT)
        self.size_lbl.pack(padx=15, side=LEFT)

        btn1 = Button(self.tool_frame, image=self.pencilIcon, width=25, command=lambda: self.tool(0))
        btn1.pack(padx=2, pady=30)
        btn2 = Button(self.tool_frame, image=self.lineIcon, width=25, command=lambda: self.tool(1))
        btn2.pack(padx=2, pady=30)
        btn3 = Button(self.tool_frame, image=self.rectIcon, width=25, command=lambda: self.tool(2))
        btn3.pack(padx=2, pady=30)
        btn4 = Button(self.tool_frame, image=self.ovalIcon, width=25, command=lambda: self.tool(3))
        btn4.pack(padx=2, pady=30)
        blnk = Label(self.tool_frame, bg="cyan")
        blnk.pack()

    def save_as(self):
        save_file = filedialog.asksaveasfilename(title='Save File', defaultextension=" '.png', '.jpg', 'jpeg' ")
        self.canvas.update()
        self.canvas.postscript(file=save_file, colormode='color')
        self.image1.save(save_file)

    def open_file(self):
        open_img = filedialog.askopenfilename(initialdir='E:/MyDocuments', title='Open File')
        self.img = ImageTk.PhotoImage(Image.open(open_img))
        self.canvas.create_image(0, 0, image=self.img, anchor=NW)

    def new_canvas(self):
        self.canvas.delete('all')

    def help(self):
        global help_win
        help_win = Toplevel(self.master)
        help_win.title("Outline Size")
        help_win.geometry("500x650")
        label = Label(help_win, text=help_text, justify='left')
        label.pack(fill='both')

    def menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu, tearoff=0)
        help_menu = Menu(menu, tearoff=0)

        menu.add_cascade(label="File", menu=file)
        menu.add_cascade(label="Options")
        menu.add_cascade(label="Help", menu=help_menu)

        file.add_command(label="New", command=self.new_canvas)
        file.add_command(label="Open", command=self.open_file)
        file.add_command(label="Save as", command=self.save_as)
        file.add_command(label="Close", command=self.master.quit)

        help_menu.add_command(label="Help...", command=self.help)

    def undo_func(self):
        if self.canvas_obj:
            self.undo.append(self.canvas_obj[-1])
            self.canvas.delete(self.canvas_obj[-1])
            self.canvas_obj.pop(-1)

