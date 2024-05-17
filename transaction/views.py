from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionView(APIView):
      def post(self,request):
        serializer=TransactionSerializer(data=request.data)
        if serializer.is_valid():
         serializer.save()
         return Response({'data':serializer.data},status=status.HTTP_200_OK)
        else:
         return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
           

class TransactionValidate(APIView):
   def post(self, request):
        try:
            userid = request.data.get('userid') 
            if userid is None:
                return Response({"message": "User ID is required."}, status=400)
            if Transaction.objects.filter(user=userid, is_payment_success=True).exists():
                return Response({"message": "You have access."})
            else:
                return Response({"message": "You do not have access."})
        except Transaction.DoesNotExist:
            return Response({"message": "User not found."})