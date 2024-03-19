from rest_framework.views import APIView
from rest_framework.response import Response
from .parser.main import get_info
from .models import CryptoCurrency
from .serializers import CryptoCurrencySerizliser

class CryptocurrencyAPIview(APIView):
    

    def get(self,request):
        
        get_info()

        cryptocurrencies =  CryptoCurrency.objects.all()
        data = [{'name': crypto.name, 'price': crypto.price,'change': crypto.change} for crypto in cryptocurrencies]
        return Response({'result': data})


