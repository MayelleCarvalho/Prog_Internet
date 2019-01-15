from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.decorators import api_view

from accounts.models import Account


@api_view(['GET', 'POST'])
def account_list(request):
    return redirect('accounts/')

@api_view(['GET', 'PUT', 'DELETE' ])
def account_detail(request, id):
    return redirect('accounts/1')