from tkinter import Frame,Entry,Button,LEFT,RIGHT

class CrawlerScreen(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.input_frame=Frame(self)

        self.stock_code_input=Entry(self.input_frame)
        self.stock_code_input.pack(side=LEFT)

        self.stock_submit=Button(self.input_frame)
        self.stock_submit["text"]="Crawl"
        self.stock_submit["command"]= lambda: print(self.stock_code_input.get())
        self.stock_submit.pack(side=RIGHT)
        
        self.input_frame.pack()







    