import tkinter

class Application(tkinter.Frame):
    def __init__(self,root=None):
        super().__init__(root, width=380, height=280,
                         borderwidth=1,relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')
    
    def create_widgets(self):
        self.text_box = tkinter.Entry(self)

root = tkinter.Tk()
root.title('TO-DO アプリ')
root.geometry('400x650+400+100')
root.resizable
app.mainloop()

