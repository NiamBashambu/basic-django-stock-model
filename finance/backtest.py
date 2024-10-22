from finance.models import StockData
import pandas as pd

def backtest(symbol, initial_investment, short_window=50, long_window=200):
    # Fetch historical data for backtesting
    data = StockData.objects.filter(symbol=symbol).order_by('date')
    df = pd.DataFrame(list(data.values()))

    df['short_mavg'] = df['close_price'].rolling(window=short_window).mean()
    df['long_mavg'] = df['close_price'].rolling(window=long_window).mean()

    # Define signals
    df['signal'] = 0
    df['signal'][short_window:] = np.where(df['short_mavg'][short_window:] > df['long_mavg'][short_window:], 1, 0)
    df['positions'] = df['signal'].diff()

    # Calculate returns
    df['daily_return'] = df['close_price'].pct_change()
    df['strategy_return'] = df['daily_return'] * df['signal'].shift(1)
    total_return = (1 + df['strategy_return']).prod() - 1
    num_trades = df['positions'].sum()
    max_drawdown = (df['close_price'].cummax() - df['close_price']).max() / df['close_price'].cummax()

    return {
        'total_return': total_return,
        'num_trades': num_trades,
        'max_drawdown': max_drawdown
    }