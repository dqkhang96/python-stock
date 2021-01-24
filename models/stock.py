from sqlalchemy import Column, Integer, String, Date,Float
from models.base import Base

class Stock(Base):
    __tablename__="Analyze_Stock"

    date=Column('Date',Date,primary_key=True)
    code=Column('Mã',String,primary_key=True)
    closedPrice=Column('Giá đóng cửa',Float)
    changePercen=Column('Thay đổi (+/-%)',String)
    referencePrice=Column('Giá tham chiếu',Float)
    openPrice=Column('Giá mở cửa',Float)
    maxPrice=Column('Giá cao nhất',Float)
    minPrice=Column('Giá thấp nhất',Float)
    volumnMatching=Column('KLGD khớp lệnh',Float)
    valueMatching=Column('GTGD khớp lệnh',Float)
    volumnAgreement=Column('KLGD thỏa thuận',Float)
    valueAgreement=Column('GTGD thỏa thuận',Float)
    dif=Column('Dif',Float)
    rate=Column('Rate_Dif/Tc',Float)

    def __init__(self,date):
        self.date=date