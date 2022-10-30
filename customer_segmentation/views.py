from django.http.response import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from math import ceil
from .models import Accounts1, Accounts2
from django.contrib import messages
import json
import datetime
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import csv
from django.forms.models import model_to_dict
from django.core import serializers
from .serializers import DataSerializers


# Create your views here.

def index(request):
    messages = ''
    if request.method == "POST":
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        print("email", email)
        print("password", password)
        user=authenticate(username= email, password= password)
        if user is not None:
            print("in if user")
            login(request, user)
            return redirect("updateaccount/4")
        else:
            messages = "Invalid credentials! Please try again"
            print("in else user")
    return render(request, 'Login.html', {"messages": messages})
@login_required
def signout(request):
    logout(request)
    return render(request, 'Login.html', {"messages": ''})
@login_required
def home1(request):
    print("request.user", request.user)
    return render(request, 'index.html')
@login_required
def update_account(request, id):
    messages = ''
    if request.method == "POST":
        a_number = request.POST.get('anumber',None)
        unsegmented = request.POST.get('unsegmented',None)
        entity_url = request.POST.get('entity_url',None)
        check = request.POST.get('check', None)
        buy = request.POST.get('buy', None)
        print(unsegmented, entity_url, buy)
        account = Accounts1.objects.filter(a_number=a_number).first()
        if check:
            check = "unavailable"
        else:
            check = "available"
        if account:
            if unsegmented or entity_url or buy:
                if check == "available":
                    if buy:
                        orgtypes = buy.split(",")
                        while("" in orgtypes):
                            orgtypes.remove("")
                        length = len(orgtypes)
                        if length >= 5:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                            account.org_type_4 = orgtypes[3]
                            account.org_type_5 = orgtypes[4]
                        if length > 0 and length == 4:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                            account.org_type_4 = orgtypes[3]
                        if length > 0 and length == 3:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                        if length > 0 and length == 2:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                        if length > 0 and length == 1:
                            account.org_type_1 = orgtypes[0]
                account.segment_source = unsegmented
                account.last_updated = request.user
                account.unavailable = check
                account.entity_url = entity_url
                account.save()
                messages = "Data updated successfully."
            else:
                messages = "Please fill atleast one field."

    if id == 1:
        data = Accounts1.objects.filter(entity_url__isnull=True, segment_source__isnull=True, ultimate_parent__icontains = "yes").first()
        serializer = DataSerializers(data)
        count_record = Accounts1.objects.filter(entity_url__isnull=True, segment_source__isnull=True, ultimate_parent__icontains = "yes").count()
    if id == 2:
        data = Accounts1.objects.filter(entity_url__isnull=True, segment_source__isnull=True, exit_rate_usd__gte = 1).first()
        serializer = DataSerializers(data)
        count_record = Accounts1.objects.filter(entity_url__isnull=True, segment_source__isnull=True, exit_rate_usd__gte = 1).count()
    if id == 3:
        data = Accounts1.objects.filter(entity_url__isnull=True, segment_source__isnull=True, oppertunity_type__gte = 1).first()
        serializer = DataSerializers(data)
        count_record = Accounts1.objects.filter(entity_url__isnull=True, segment_source__isnull=True, oppertunity_type__gte = 1).count()
    if id == 4:
        data = Accounts1.objects.filter(entity_url__isnull=True, segment_source__isnull=True).first()
        serializer = DataSerializers(data)
        count_record = Accounts1.objects.filter(entity_url__isnull=True, segment_source__isnull=True).count()
    count_record = count_record if count_record else None
    dataJson = serializer.data
    return render(request, 'UpdateAccount.html',  {"data" : dataJson, "count_record": count_record, "id": id, "messages": messages })

@login_required
def update_unsegmented(request):
    messages = ''
    if request.method == "POST":
        a_number = request.POST.get('anumber','')
        unsegmented = request.POST.get('unsegmented','')
        check = request.POST.get('check', '')
        buy = request.POST.get('buy','')
        account = Accounts1.objects.filter(a_number=a_number).first()
        if check:
            check = "unavailable"
        else:
            check = "available"
        if account:
            if unsegmented or buy:
                if check == "available":
                    if buy:
                        orgtypes = buy.split(",")
                        while("" in orgtypes):
                            orgtypes.remove("")
                        length = len(orgtypes)
                        if length >= 5:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                            account.org_type_4 = orgtypes[3]
                            account.org_type_5 = orgtypes[4]
                        if length > 0 and length == 4:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                            account.org_type_4 = orgtypes[3]
                        if length > 0 and length == 3:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                        if length > 0 and length == 2:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                        if length > 0 and length == 1:
                            account.org_type_1 = orgtypes[0]
                account.last_updated = request.user
                account.unavailable = check
                account.segment_source = unsegmented
                account.save()
                messages = "Data updated successfully."
            else:
                messages = "Please fill atleast one field."
    data = Accounts1.objects.filter(segment_source__isnull=True).exclude(entity_url__isnull=True).first()
    serializer = DataSerializers(data)
    dataJson = serializer.data
    return render(request, 'UpdateUnsegmented.html', {"data" : dataJson, "messages": messages })


@login_required
def update_url(request):
    messages = ''
    if request.method == "POST":
        a_number = request.POST.get('anumber','')
        entity_url = request.POST.get('entity_url','')
        check = request.POST.get('check', '')
        buy = request.POST.get('buy','')
        account = Accounts1.objects.filter(a_number=a_number).first()
        if check:
            check = "unavailable"
        else:
            check = "available"
        if account:
            if entity_url or buy:
                if check == "available":
                    if buy:
                        orgtypes = buy.split(",")
                        while("" in orgtypes):
                            orgtypes.remove("")
                        length = len(orgtypes)
                        if length >= 5:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                            account.org_type_4 = orgtypes[3]
                            account.org_type_5 = orgtypes[4]
                        if length > 0 and length == 4:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                            account.org_type_4 = orgtypes[3]
                        if length > 0 and length == 3:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                            account.org_type_3 = orgtypes[2]
                        if length > 0 and length == 2:
                            account.org_type_1 = orgtypes[0]
                            account.org_type_2 = orgtypes[1]
                        if length > 0 and length == 1:
                            account.org_type_1 = orgtypes[0]
                account.last_updated = request.user
                account.unavailable = check
                account.entity_url = entity_url
                account.save()
                messages = "Data updated successfully."
            else:
                messages = "Please fill atleast one field."
    data = Accounts1.objects.filter(entity_url__isnull=True).exclude(segment_source__isnull=True).first()
    serializer = DataSerializers(data)
    dataJson = serializer.data
    return render(request, 'UpdateUrl.html', {"data" : dataJson, "messages":messages })

@login_required
def search_existing(request):
    dataJson = {}
    if request.method == "POST":
        a_number = request.POST.get('anumber','')
        account = Accounts1.objects.filter(a_number=a_number).first()
        serializer = DataSerializers(account)
        dataJson = serializer.data
    print("datajson", dataJson)
    print("request.user", request.user)
    return render(request, 'SearchExistingAccounts.html', {"data" : dataJson })


@login_required
def loadFile(request):
    messages = ''
    if request.method == "POST":
        file_data = request.FILES["file1"]
        decoded_file = file_data.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        data = {}
        try:
            for row in reader:
                print("row", row)
                for key, value in row.items():
                    data[key.replace(' ', '')] = value
                    print("data", data)
                a_number = data['ANumber']
                account_name = data['AccountName']
                org_type_1 = data['Org_Type_1']
                org_type_2 = data['Org_Type_2']
                org_type_3 = data['Org_Type_3']
                org_type_4 = data['Org_Type_4']
                org_type_5 = data['Org_Type_5']
                entity_url = data['EntityURL']
                segment_source = data['Website']
                account = Accounts1.objects.filter(a_number=a_number).first()
                if account:
                    account.account_name = account_name 
                    account.segment_source = segment_source
                    account.entity_url = entity_url
                    account.org_type_1 = org_type_1
                    account.org_type_2 = org_type_2
                    account.org_type_3 = org_type_3
                    account.org_type_4 = org_type_4
                    account.org_type_5 = org_type_5
                    account.last_updated = request.user
                    account.save()
                    messages = "File uploaded successfully."
                    print("done")
        except:
            messages = "There's an issue uploading your file."
    print("request.user", request.user)
    return render(request, 'LoadFile.html', {"messages":messages})