# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import User
import json

register_code = 0


def user_login_view(request):
	print "user_login_view"
	return render(request,'reg.html')


@csrf_exempt
def record(request):
    strr = 'fadfaf'

    # for x in a:
    #     strr += x + ':' + a[x]+ "'\n'
    if request.method == 'POST':
        a = request.POST
        json_data = json.loads(request.body)
        a = json_data
    print a.get('name')
#    user, if_success = User.objects.get_or_create(name = a.get('name'), sex = a['sex'], phone = a['phone'], mail = a['email'], invoice = a['invoice'],tax_id = a['tax_id'], address = a['address'], user_id = a['id'], paper_id = a['paper_id'],stay = a['stay'], type = a['type'])

    user, if_success = User.objects.get_or_create(name = a['name'], phone = a['phone'], mail = a['email'])
    if if_success == True:
        if a['stay'] == 'no':
            user.enter_date = None
            user.out_date = None
            user.m_room = None
        if a['stay'] == 'single':
            user.enter_date = a['in_date']
            user.out_date = a['out_date']
            user.m_room = None
        if a['stay'] == 'multi':
            user.enter_date = a['in_date']
            user.out_date = a['out_date']
            user.m_room = a['m_name']
        user.save()
    else:
        strr = "create user failed because identical object exists"

    return HttpResponse(strr)


# Create your views here.
