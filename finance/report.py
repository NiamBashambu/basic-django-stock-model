import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
from django.core.files.base import ContentFile

from finance.models import StockData

def generate_report(symbol):
    data = StockData.objects.filter(symbol=symbol).order_by('date')
    df = pd.DataFrame(list(data.values()))

    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['close_price'], label='Actual Prices', color='blue')
    plt.title(f'Stock Prices for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation=45)

    # Save to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return ContentFile(buffer.read(), name=f'report_{symbol}.png')