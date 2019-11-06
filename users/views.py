from rest_framework.viewsets import ViewSet
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response

class CustomerViewSet(ViewSet):
    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request, pk=None):
        queryset = Customer.objects.filter(register_date=pk)
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)