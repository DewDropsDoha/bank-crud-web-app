from django.shortcuts import get_object_or_404, render
from .models import Account
from .forms import AccountModelForm
from datetime import datetime,date

# Split fetched data from DB
def split(s):
    str = s
    arr = str.split()
    return arr
# Split to get dict(amount,date,time)
def arr_split(s):
    str = s
    amount_date_time = str.split('-')
    return amount_date_time

# Getting current Date
def get_date():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    temp = "-" + current_date + "-" + current_time
    return temp

# Home page
def home_view(request):
    obj = get_object_or_404(Account,id=1)
    balance = obj.balance
    template_name = "home.html"
    context = {"balance":balance}
    return render(request, template_name, context)

# Deposit Page
def deposit_view(request):
    obj = get_object_or_404(Account,id=1)
    balance = obj.balance
    form = AccountModelForm(request.POST or None, instance=obj)
    deposit_amount = int(request.POST.get('balance',0))
    context = {"form":AccountModelForm()}
    if form.is_valid():
        obj.balance = balance + deposit_amount
        current_time = get_date()
        obj.deposit = obj.deposit + " " + str(deposit_amount) + current_time
        obj.save()
        form = AccountModelForm()
        #msg = "Insufficient Balance!"
        context = {"form":AccountModelForm(), "msg":"1"}
        
    template_name = "deposit.html"
    print(AccountModelForm())
    return render(request, template_name, context)

# Withdraw Page
def withdraw_view(request):
    obj = get_object_or_404(Account,id=1)
    balance = obj.balance
    form = AccountModelForm(request.POST or None, instance=obj)
    withdraw_amount = int(request.POST.get('balance',0))

    context = {"form":AccountModelForm()}
    if form.is_valid() and withdraw_amount<=balance:
        obj.balance = balance - withdraw_amount
        current_time = get_date()
        obj.withdraw = obj.withdraw + " " + str(withdraw_amount) + current_time
        obj.save()
        form = AccountModelForm()
        context = {"form":AccountModelForm()}
    elif withdraw_amount==0:
        context = {"form":AccountModelForm()}
    else:
        msg = "Insufficient Balance!"
        context = {"form":AccountModelForm(), "msg":msg}

    template_name = "withdraw.html"
    return render(request, template_name, context)

# Transaction Page
# Fetch all data, then split, then render
def transaction_view(request):
    obj = get_object_or_404(Account,id=1)
    deposit_list = split(obj.deposit)
    count=0
    for i in deposit_list:
        deposit_list[count]=arr_split(deposit_list[count])
        count+=1
    count=0
    withdraw_list = split(obj.withdraw)
    for i in withdraw_list:
        withdraw_list[count]=arr_split(withdraw_list[count])
        count+=1
    
    template_name = "transaction.html"
    context = {"deposit_list":deposit_list, "withdraw_list":withdraw_list,"title":"All Transactions"}
    return render(request, template_name, context)