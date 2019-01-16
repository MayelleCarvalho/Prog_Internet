from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Account
from rest_framework import status, serializers
from accounts.serializers import AccountSerializer


@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        accounts_serializer = AccountSerializer(accounts, many=True)
        return Response(accounts_serializer.data)
    elif request.method == 'POST':
        account_serializer = AccountSerializer(data=request.data)
        if account_serializer.validate_balance() and account_serializer.is_valid() and account_serializer.validate_data():
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)
        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def account_detail(request, id):
    try:
        account = Account.objects.get(pk=id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        account_serializer = AccountSerializer(account)
        return Response(account_serializer.data)

    elif request.method == 'PUT':
        account_serializer = AccountSerializer(account, data = request.data)
        if account_serializer.validate_balance() and account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data)
        return Response (account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        account_serializer = AccountSerializer(account, data=request.data, partial=True)

        if account_serializer.is_valid():
            if account_serializer.validated_data:
                saldo = account.__getattribute__('balance') - account_serializer.data.__getattribute__('balance')
                print(saldo)
                print(account.__getattribute__('balance'))
                print(request.data__getitem__('balance'))
                if saldo > 0:
                    account_serializer.data.__setattr__('balance', saldo)
                    account_serializer.save()
                    print('entrou')
                    return Response(status=status.HTTP_202_ACCEPTED)
                elif saldo == 0:
                    raise serializers.ValidationError("O Saldo não pode ser zerado")
                elif saldo < 0 :
                    raise serializers.ValidationError("Saldo insuficiente")


#
# @api_view(['PATCH'])
# def account_edit_balance(request, id):
#
#     try:
#         account = Account.objects.get(pk=id)
#     except Account.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PATCH':
#         account_serializer = AccountSerializer(account, many=True, partial=True)
#         saldo = account.balance - value
#         if saldo > 0:
#             account_serializer.__setattr__('balance', saldo)
#             if account_serializer.is_valid():
#                 account_serializer.save()
#                 return Response(status=status.HTTP_202_ACCEPTED)
#         elif saldo == 0:
#             raise serializers.ValidationError("O Saldo não pode ser zerado")
#         elif saldo < 0 :
#             raise serializers.ValidationError("Saldo insuficiente")
#         return Response(status=status.HTTP_400_BAD_REQUEST)
