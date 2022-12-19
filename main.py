from stock import Stock


stock = Stock()
variation = stock.get_variation()

if abs(variation) >= 4:
    from news import News

    stock_news = News(company=stock.company_name, sto=stock.stock, day=stock.days[0], variation=variation)
    stock_news.get_data(2)
    stock_news.send_news()
