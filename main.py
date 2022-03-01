# 2022 Baltazarus

import sys
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog

class Application:
    def __init__(self, master, width = 500, height = 500, *args, **kwargs):
        self.master = master
        self.width = width
        self.height = height
        self.widget_main_text = None
        self.widget_menubar = None
        self.window_about = None
        self.current_path = ""
        self.ffilters = (("Text File", "*.txt"), ("All Files", "*.*"))
        self.b_save_as = False

        self.InitUI()

    def InitUI(self):
        self.master.geometry(str(self.width) + 'x' + str(self.height))
        self.master.title("TkNotepad32 v1.0")
        self.InitMenubar()
        
        self.widget_main_text = tk.Text(self.master)
        self.widget_main_text.grid(row=0, column=0, columnspan=4, sticky=tk.N+tk.S+tk.W+tk.E)

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

    def InitMenubar(self):
        self.widget_menubar = tk.Menu(self.master)
        file_menu = tk.Menu(self.widget_menubar, tearoff = 0)
        file_menu.add_command(label = "New", command = self.New)
        file_menu.add_command(label = "Open", command = self.Open)
        file_menu.add_command(label = "Save", command = self.Save)
        file_menu.add_separator()
        file_menu.add_command(label = "Save As", command = self.SaveAs)
        file_menu.add_separator()
        file_menu.add_command(label = "Quit", command = self.Exit)
        self.widget_menubar.add_cascade(label = "File", menu = file_menu)

        edit_menu = tk.Menu(self.widget_menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.Cut)
        edit_menu.add_command(label="Copy", command=self.Copy)
        edit_menu.add_command(label="Paste", command=self.Paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.SelectAll)
        self.widget_menubar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(self.widget_menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.About)
        self.widget_menubar.add_cascade(label="Help", menu=help_menu)
        
        self.master.config(menu = self.widget_menubar)

    def Exit(self):
        confirm = tk.messagebox.askyesno(title = "Quit?", message="Do you wish to quit?")
        if confirm:
            exit(0)

    def About(self):
        self.window_about = tk.Tk()
        self.window_about.resizable(False, False)
        self.window_about.geometry("210x70")
        self.window_about.title("About")

        label_about = tk.Label(
            self.window_about, 
            text="Created 2022 Baltazarus\nThis is Python version of Notepad32",
            width=170, height=20
        ).pack()

    def New(self):
        self.widget_main_text.delete("1.0", tk.END)
        self.current_path = ""

    def Open(self):
        self.current_path = filedialog.askopenfilename(filetypes=self.ffilters)
        f = open(self.current_path, "r")
        text_content = f.read()
        self.widget_main_text.delete("1.0", tk.END)
        self.widget_main_text.insert("1.0", text_content, tk.END)
        f.close()
    
    def Save(self):
        if len(self.current_path) < 1 or self.b_save_as:
            self.current_path = filedialog.asksaveasfilename(filetypes=self.ffilters)
            self.b_save_as = False
        f = open(self.current_path, "w")
        f.write(self.widget_main_text.get("1.0", tk.END))
        f.close()

    def SaveAs(self):
        self.b_save_as = True
        self.Save()

    def Cut(self):
        self.widget_main_text.event_generate("<<Cut>>")
    
    def Copy(self):
        self.widget_main_text.event_generate("<<Copy>>")

    def Paste(self):
        self.widget_main_text.event_generate("<<Paste>>")

    def SelectAll(self):
        self.widget_main_text.event_generate("<<SelectAll>>")

def Main(args):
    root = tk.Tk()
    # Manage command line arguments.
    if len(args) > 1:
        for i in range(len(args)):
            if args[i] == "-maximized":
                root.state("zoomed")
            if args[i] == "-minimized":
                root.state("normal")
    
    __main = Application(root, 500, 500)
    root.mainloop()

if __name__ == '__main__':
    Main(sys.argv)
