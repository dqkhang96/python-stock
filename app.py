import tkinter as tk
from tkinter import ttk
from views.crawler_screen import CrawlerScreen
from views.analyze_stock import AnalyzeStockScreen
from models.base import Session

class Application(tk.Frame):
   
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.session=Session()
        self.create_widgets() 

   
    
    def create_widgets(self):
        self.tab_control = ttk.Notebook(root,width=1000)
        self.tab_control.add(AnalyzeStockScreen(self.tab_control,self.session), text='Analyze Stock')
        self.tab_control.add(CrawlerScreen(self.tab_control), text='Crawler')
        self.tab_control.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()