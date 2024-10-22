from django.urls import path
from .views import backtest_view



from .views import predict_view



from .views import report_view

urlpatterns = [
    path('backtest/', backtest_view, name='backtest'),
    path('predict/', predict_view, name='predict'),
    path('report/', report_view, name='report'),
]