from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.core import management
from django.utils import timezone
import datetime

import sys
import os
import json

from project.models import log_list


# log_api用
def api_log(request):

    # url から値の読取
    datetime_str = request.GET.get("datetime")
    serial_no_str = request.GET.get("serial_no")
    voltage_str = request.GET.get("voltage")
    temp_str = request.GET.get("temp")
    humidity_str = request.GET.get("humidity")
    atmospheric_pressure_str = request.GET.get("atmospheric_pressure")
    moisture_content_str = request.GET.get("moisture_content")
    
    # もし時間が無かったら現在時間を入れる
    if datetime_str == None:
        datetime_str = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S.%f')

    data_list = [] # 計算を格納するリストを作成する(1次元配列)
    data_list.clear() # 一旦リストを空にする

    # リストに格納する
    data_list.append(log_list(datetime = datetime_str,\
                              serial_no = serial_no_str,\
                              voltage = voltage_str,\
                              temp = temp_str,\
                              humidity = humidity_str,\
                              atmospheric_pressure = atmospheric_pressure_str,\
                              moisture_content = moisture_content_str))

    log_list.objects.bulk_create(data_list) # 作成したリストをDBに書き込む
    
    return HttpResponse("Success!")

def api_now(request):

    now = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S.%f')

    ret = {"now":now}

    return JsonResponse(ret)
        
