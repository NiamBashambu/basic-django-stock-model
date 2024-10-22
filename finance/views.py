

from django.http import JsonResponse
from .backtest import backtest

def backtest_view(request):
    symbol = request.GET.get('symbol', 'AAPL')
    initial_investment = float(request.GET.get('initial_investment', 10000))
    results = backtest(symbol, initial_investment)

    return JsonResponse(results)

from django.http import JsonResponse
from .predict import predict_next_days

def predict_view(request):
    symbol = request.GET.get('symbol', 'AAPL')
    predictions = predict_next_days(symbol)

    return JsonResponse({'predictions': predictions.tolist()})



from django.http import HttpResponse
from .report import generate_report

def report_view(request):
    symbol = request.GET.get('symbol', 'AAPL')
    report_image = generate_report(symbol)

    response = HttpResponse(report_image, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="report_{symbol}.png"'
    return response