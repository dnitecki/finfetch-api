from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_api_key.permissions import HasAPIKey
from pandas_datareader import data as pdr
import yfinance as yf

class GetStocks(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        if request.method =='GET':
            ticker = request.GET.get('ticker', "")
            start = request.GET.get('startDate', "")
            end = request.GET.get('endDate', "")
            
            if ticker =="":
                return Response("Missing Required Parameters", status=status.HTTP_400_BAD_REQUEST)
            elif start =="":
                return Response("Missing Required Parameters", status=status.HTTP_400_BAD_REQUEST)
            elif end =="":
                return Response("Missing Required Parameters", status=status.HTTP_400_BAD_REQUEST)
            stock=pdr.get_data_yahoo(ticker, start=start, end=end)
            return Response({'data':stock}, status=status.HTTP_200_OK)

class GetStockInfo(APIView):
    def get(self,request):
        if request.method =='GET':
            ticker = request.GET.get('ticker',"")
            if ticker == "":
                return Response("Missing Required Parameters", status=status.HTTP_400_BAD_REQUEST)
            stock = yf.Ticker(ticker)
            stockInfo = stock.info
            return Response({'data':stockInfo}, status=status.HTTP_200_OK)

class GetStockNews(APIView):
    def get(self,request):
        if request.method =="GET":
            ticker = request.GET.get('ticker',"")
            if ticker =="":
                return Response("Missing Required Parameters", status=status.HTTP_400_BAD_REQUEST)
            stock = yf.Ticker(ticker)
            stockNews = stock.news
            return Response({'data':stockNews}, status=status.HTTP_200_OK)