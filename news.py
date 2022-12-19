import os
from twilio.rest import Client


class News:

    def __init__(self, sto='TSLA', company='Tesla Inc', day='2022-12-19', variation=0):
        self.news_list = []
        self.stock = sto
        self.variation = variation
        self.url = 'https://newsapi.org/v2/everything?'
        self.news_parms = {
            'q': company,
            'from': day,
            'sortBy': 'popularity',
            'apikey': os.environ.get('NEWS_KEY')
        }
        self.sms_parms = {
            'apikey': os.environ.get('SMS_KEY')
        }
        self.sms = ''

    def get_data(self, news_quantity=3) -> None:
        import requests

        response = requests.get(url=self.url, params=self.news_parms)
        data = response.json()
        for _ in range(news_quantity):
            self.news_list.append(data['articles'][_])

    def create_sms(self):
        if self.variation > 0:
            self.sms += f"{self.stock}: {self.variation:.2f}%\n\n"
        elif self.variation == 0:
            self.sms += f"{self.stock}: {self.variation:.2f}%\n\n"
        else:
            self.sms += f"{self.stock}: {self.variation:.2f}%\n\n"
        for num, a_new in enumerate(self.news_list):
            self.sms += f"{num + 1}º New:\n"
            self.sms += f"Headline: {a_new['title']}\n"
            self.sms += f"Brief: {a_new['description']}"
            self.sms += f"\n\n"

    def send_news(self):
        self.create_sms()
        account_sid = "AC90884ead92d52bd58a6e6c564e99e9cd"
        auth_token = os.environ.get('SMS_KEY')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=self.sms,
            from_="+14245005133",
            to="PHONE_NUMBER"
        )

        print(message.sid)


if __name__ == '__main__':
    news = News(company='Tesla Inc', day='2022-12-19', sto='TSLA', variation=-2)
    news.get_data()
    news.create_sms()
    print(news.sms)
