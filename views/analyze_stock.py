from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT,BOTTOM,DISABLED,NORMAL
from tkinter.ttk import Frame, Label, Entry, Button
from tksheet import Sheet
import xlsxwriter
import time
from models.stock import Stock
from models.analyze_stock import AnalyzeStock
from models.base import Session
from controllers.func.analyze_stock import FAnalyzeStockController
from datetime import datetime, timedelta

class AnalyzeStockScreen(Frame):
    def __init__(self, master=None,session=None):
        super().__init__(master)
        self.master = master
        self.session=session
        self.analyze_controller=FAnalyzeStockController(session)
        self.pack(padx=20,pady=20)
        self.create_widgets()

    
    def create_widgets(self):
        # Khởi tạo tab phân tích chứng khoán 

        ## Phần nhập ngày bắt đầu
        self.start_date_frame=Frame(self)
        self.start_date_frame.pack(fill=X)
        self.start_date_label = Label(self.start_date_frame, text="Start date", width=10)
        self.start_date_label.pack(side=LEFT, padx=5, pady=5)
        self.start_date_input=Entry(self.start_date_frame)
        self.start_date_input.pack(fill=X, padx=5, expand=True)

        ## Phần nhập ngày kết thúc 
        self.end_date_frame=Frame(self)
        self.end_date_frame.pack(fill=X)
        self.end_date_label = Label(self.end_date_frame, text="End date", width=10)
        self.end_date_label.pack(side=LEFT, padx=5, pady=5)
        self.end_date_input=Entry(self.end_date_frame)
        self.end_date_input.pack(fill=X, padx=5, expand=True)

        ## Phần nút bấm
        self.stock_submit_frame=Frame(self)
        self.stock_submit_frame.pack(fill=X,padx=10)

        ## Phần button phân tích
        self.stock_submit=Button(self.stock_submit_frame)
        self.stock_submit["text"]="Tính"
        self.stock_submit["command"]= lambda: self.start_calc()
        self.stock_submit.pack(side=RIGHT)

        # Phầns button export excel
        self.export_excel_button=Button(self.stock_submit_frame,state=DISABLED)
        self.export_excel_button["text"]="Export file"
        self.export_excel_button["command"]= lambda: self.export_file_excel()
        self.export_excel_button.pack(side=RIGHT,padx=20)

        ## Phần bản tính
        self.tabel_frame=Frame(self)
        self.tabel_frame.pack(fill=X,pady=10)
        self.sheet = Sheet(self.tabel_frame)
        self.sheet.pack(fill=X)

        self.header=("Mã","Giá đóng nhỏ nhất","Giá đóng lớn nhất")
        self.sheet.headers(self.header)

        ### Cấu hình cho tkinter sheet
        self.sheet.enable_bindings(("single_select",
                       "row_select",
                       "column_width_resize",
                       "arrowkeys",
                       "right_click_popup_menu",
                       "rc_select",
                       "rc_insert_row",
                       "rc_delete_row",
                       "copy",
                       "cut",
                       "paste",
                       "delete",
                       "undo",
                       "edit_cell"))

    def start_calc(self):
        ## Disable trang export file button
        self.export_excel_button["state"]=DISABLED
     
        datetime_format="%d/%m/%Y"
        startDate= datetime.strptime(self.start_date_input.get().strip(),datetime_format)
        endDate = datetime.strptime(self.end_date_input.get(),datetime_format)

        self.analyzeStocks=self.analyze_controller.get_analyze_stocks_data(startDate,endDate)

        ## Tạo data cho tkinter sheet
        self.data_sheet=[]

        for anaStock in self.analyzeStocks:
            self.data_sheet.append([anaStock.code,anaStock.closedPriceMin,anaStock.closedPriceMax])
        
        ## Thêm vào tkinter sheet 
        self.sheet.set_sheet_data(self.data_sheet)

        self.export_excel_button["state"]=NORMAL
    
    def export_file_excel(self):

        ## Tạo bảnh tính excel với tên file là file_excel_<Thời gian tính theo giây>
        workbook = xlsxwriter.Workbook('file_excel_{}.xlsx'.format(time.time()))
        worksheet = workbook.add_worksheet()

        ## Tạo kiểu kiểu chữ
        bold = workbook.add_format({'bold': True})

        ## Phần header cho trang tính excel
        worksheet.write('A1', 'Mã', bold)
        worksheet.write('B1', 'Giá đóng nhỏ nhất', bold)
        worksheet.write('C1', 'Giá đóng lớn nhất', bold)

        ## Thêm dòng vào bảng tính
        row = 1
        for record in self.analyzeStocks:
            worksheet.write(row, 0, record.code)
            worksheet.write(row, 1, record.closedPriceMin)
            worksheet.write(row, 2, record.closedPriceMax)
            row+=1

        ## Lưu file và đóng bảng tính
        workbook.close()









    