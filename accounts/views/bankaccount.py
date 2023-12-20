from accounts.models.users import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView,CreateAPIView
from accounts.models.bankaccount import BankAccount, Bank, Ifsc
from accounts.serializers.bankaccount import BankSerializer, IfscSerializer, BankAccountSerializer
from rest_framework.permissions import IsAuthenticated


class GetBankAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class GetIfscAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ifsc.objects.all()
    serializer_class = IfscSerializer

class GetBankAccountAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class CreateBankAccountAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        ifsc = request.data.get('ifsc')
        account_holder_name = request.data.get('account_holder_name')
        account_number = request.data.get('account_number')
        confirm_account_number = request.data.get('confirm_account_number')
        account_type = request.data.get('account_type')

        try:
            ifsc_instance = Ifsc.objects.get(name=ifsc)
        except Ifsc.DoesNotExist:
            return Response({"message": "Ifsc code not found"})

        try:
            user = request.user
            if ifsc_instance and account_holder_name and account_number and confirm_account_number and account_type:
                bank_account = BankAccount.objects.create(user = user, ifsc = ifsc_instance, account_holder_name = account_holder_name, account_number = account_number, confirm_account_number = confirm_account_number, 
                                                          account_type = account_type)
                
                instance = BankAccountSerializer(bank_account)
                return Response(instance.data)
            
            else:
                return Response({"message":"Enter all bank accounts deatils"})
            
        except BankAccount.DoesNotExist:
            return Response({"message":"Bank account not found"})
            
class UpdateBankAccountAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        ifsc = request.data.get('ifsc')
        account_holder_name = request.data.get('account_holder_name')
        account_number = request.data.get('account_number')
        confirm_account_number = request.data.get('confirm_account_number')
        account_type = request.data.get('account_type')

        try:
            ifsc_instance = Ifsc.objects.get(name=ifsc)
        except Ifsc.DoesNotExist:
            return Response({"message": "Ifsc code not found"})
        
        user = request.user
        if ifsc_instance and account_holder_name and account_number and confirm_account_number and account_type:
            bank = BankAccount.objects.get(id = id, user=user)
            bank.account_number = account_number
            bank.account_type = account_type
            bank.account_holder_name = account_holder_name
            bank.confirm_account_number = confirm_account_number
            bank.save()

            instance = BankAccountSerializer(bank) 
            return Response(instance.data)
        else:
            return Response({"message":"Please enter your Full details of the user account"})
        