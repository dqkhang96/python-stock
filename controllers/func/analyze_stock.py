from models.stock import Stock
from models.analyze_stock import AnalyzeStock


class FAnalyzeStockController:
    def __init__(self,session=None):
        self.session=session
    
    def get_analyze_stocks_data(self,startDate,endDate):
        ## Tương đương với SELECT * from Analyze_Stock WHERE date >= startDate AND date <= endDate
        stocks=self.session.query(Stock).filter(Stock.date >= startDate,Stock.date <= endDate).all()

        stocks.sort(key=lambda stock:stock.code)
        analyzeStocks=[]

        t = -1
        for stock in stocks:
            if(len(analyzeStocks)>0)and(analyzeStocks[t].code==stock.code):
                if(analyzeStocks[t].closedPriceMin>stock.closedPrice):
                    analyzeStocks[t].closedPriceMin=stock.closedPrice
                if(analyzeStocks[t].closedPriceMax<stock.closedPrice):
                    analyzeStocks[t].closedPriceMax=stock.closedPrice
            else:
                analyzeStocks.append(AnalyzeStock(stock.code,stock.closedPrice,stock.closedPrice))
                t+=1
                
        return analyzeStocks
        