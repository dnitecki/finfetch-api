from django.urls import path
from stocks import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'stocks'

urlpatterns = [
    path('stock', views.GetStocks.as_view() ),
    path('stock/info', views.getStockInfo),
    path('stock/news', views.getStockNews),
]


urlpatterns = format_suffix_patterns(urlpatterns)