import pickle
import numpy as np
from finance.models import StockData

def predict_next_days(symbol, days=30):
    # Load the pre-trained model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Fetch the last available stock data
    last_data = StockData.objects.filter(symbol=symbol).order_by('-date')[:60]
    X = np.array([data.close_price for data in last_data]).reshape(-1, 1)

    # Prepare input for prediction (last 60 days)
    predictions = model.predict(X[-60:].reshape(-1, 1))

    return predictions[-days:]