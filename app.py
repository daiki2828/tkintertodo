
import tkinter

class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280,
                         borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        # 閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')
        #top bar
        top_image = tkinter.Label(self)
        top_image["image"] = tkinPhotoImage(file="image/topbar.png")
        top_image.pack()



root = tkinter.Tk()
root.title('サプー アプリ')
root.geometry('400x300')
app = Application(root=root)
app.mainloop()
