import requests
from django.core.management.base import BaseCommand
from finance.models import StockData
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Fetch stock data from Alpha Vantage'

    def handle(self, *args, **kwargs):
        api_key = '4PFNZNTEBJB6LTRV'
        symbol = 'AAPL'
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&outputsize=full'

        response = requests.get(url)
        data = response.json()

        time_series = data.get('Time Series (Daily)', {})
        for date_str, daily_data in time_series.items():
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            stock_data = StockData(
                symbol=symbol,
                date=date,
                open_price=float(daily_data['1. open']),
                close_price=float(daily_data['4. close']),
                high_price=float(daily_data['2. high']),
                low_price=float(daily_data['3. low']),
                volume=int(daily_data['6. volume']),
            )
            stock_data.save()
        self.stdout.write(self.style.SUCCESS('Stock data fetched successfully.'))
