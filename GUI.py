from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
      Label(text = "Welcome to Blackjack!",fg = "green").grid(row = 0,column = 1,sticky = N)
root = Tk()
root.title("BlackJack")
app = Application(root)
root.mainloop()
