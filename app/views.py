from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from .models import Account, Transaction

def all_accounts(request):
    accounts = Account.objects.all()
    return render(request, 'app/home.html', {'accounts': accounts})

def select_account(request, account_id):
    account = Account.objects.get(pk=account_id)
    other_accounts = Account.objects.exclude(pk=account_id)
    context = {
        'source': account,
        'destinations': other_accounts
    }
    return render(request, 'app/destination.html', context)

def prepare_transfer(request):
    source = Account.objects.get(pk=int(request.POST.get('source-id', False)))
    destination = Account.objects.get(pk=int(request.POST.get('destination-id', False)))
    context = {
        'source': source,
        'destination': destination
    }
    return render(request, 'app/transfer.html', context)

def transfer_money(request):
    source = Account.objects.get(pk=int(request.POST.get('source-id', False)))
    destination = Account.objects.get(pk=int(request.POST.get('destination-id', False)))
    amount = float(request.POST.get('amount', False))
    enough_cash = source.available_cash >= amount
    if enough_cash:
        source.available_cash -= amount
        source.save()
        destination.available_cash += amount
        destination.save()
        messages.success(request, 'OK 200: Transfer successfully executed.')
    else:
        messages.error(request, f'Error 400: Tried to transfer {amount} from {source.name}, but only had {source.available_cash} available.')
    
    transaction = Transaction(description=f"Transfer from {source.name} to {destination.name}.", success=enough_cash, cash_amount=amount, source_account=source, 
    destination_account=destination)
    transaction.save()

    return redirect('overview')

def see_all_transfers(request):
    transfers = Transaction.objects.all().order_by('-executed_time')
    return render(request, 'app/allTransfers.html', {'transfers': transfers})