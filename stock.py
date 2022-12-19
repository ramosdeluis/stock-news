import os


class Stock:
    def __init__(self, sto='TSLA', company='Tesla Inc'):
        self.variation = None
        self.days = None
        self.past_day = None
        self.current_day = None
        self.current_price: float
        self.past_price: float
        self.start_url = 'https://www.alphavantage.co/query?'
        self.stock = sto
        self.company_name = company
        self.parms = {
            'function': 'TIME_SERIES_DAILY_ADJUSTED',
            'symbol': self.stock,
            # 'interval': '5min',
            'datatype': 'json',
            'apikey': os.environ.get('ALPHA_KEY')
        }

    def get_data(self) -> None:
        import requests
        response = requests.get(url=self.start_url, params=self.parms)
        data = response.json()
        self.days = [list(data['Time Series (Daily)'])[0], list(data['Time Series (Daily)'])[1]]
        self.current_day = {
            list(data['Time Series (Daily)'])[0]: data['Time Series (Daily)'][list(data['Time Series (Daily)'])[0]]}
        self.past_day = {
            list(data['Time Series (Daily)'])[1]: data['Time Series (Daily)'][list(data['Time Series (Daily)'])[1]]}

    def get_variation(self) -> float:
        self.get_data()
        day_close_price = float(self.current_day[self.days[0]]['4. close'])
        yesterday_close_price = float(self.past_day[self.days[1]]['4. close'])
        self.variation = ((day_close_price-yesterday_close_price)/yesterday_close_price)*100
        return self.variation


if __name__ == '__main__':
    stock = Stock()
    stock.get_variation()
