from django.http import JsonResponse
from rest_framework.decorators import api_view
import random

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

import pandas as pd
csv_path = 'test_app/data/test_data_has_null.csv'

def savedata(request):
    df = pd.read_csv('test_app/data/test_data.csv', encoding='cp949')
    data = df.to_dict('records')
    return JsonResponse({'dat':data})

def savenulldata(request):
    df = pd.read_csv(csv_path, encoding='cp949')
    df.fillna("NULL", inplace=True)
    data = df.to_dict('records')
    return JsonResponse({'dat':data})


def avg_age(request):
    
    df = pd.read_csv(csv_path, encoding='cp949')
    df.fillna(0, inplace=True)
    data = df.to_dict('records')
    total = 0
    cnt = 0
    for i in data:
        if i['나이']:
            total += i['나이']
            cnt += 1
            
    avg = total/cnt # 46.2
    df['diff'] = abs(avg-df['나이'])
    data = sorted(df.to_dict('records'), key=lambda x:x['diff'])[:10]
    
    return JsonResponse({'dat':data})
