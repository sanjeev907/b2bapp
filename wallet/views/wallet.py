from accounts.models.users import User
from utils.views import CustomPageNumberPagination
from wallet.models.wallet import Wallet, Wallettype
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView,CreateAPIView , GenericAPIView
from rest_framework.permissions import IsAuthenticated
from wallet.serializers.wallet import WalletSerializer
from rest_framework import status

class GetWalletList(ListAPIView):
    pagination_class = CustomPageNumberPagination
    queryset = Wallet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = WalletSerializer

class GetWalletByid(ListAPIView):
    pagination_class = CustomPageNumberPagination
    def get(self, request,id, *args, **kwargs):
        id = request.data.get('id')
        try:
            if id:
                user = Wallet.objects.get(id=id)
                instance = WalletSerializer(user)
                return Response(instance.data,{'messge':'success'},status=status.HTTP_200_OK) # type: ignore
        except Wallet.DoesNotExist:
            return Response({'messge':'User Wallet not Found'},status =status.HTTP_404_NOT_FOUND)
        


