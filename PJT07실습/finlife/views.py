from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status
import requests
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from .models import DepositProducts, DepositOptions


# Create your views here.

@api_view(['GET'])
def index(request):
    API_KEY = settings.API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    return Response(response)


@api_view(['GET'])
def save_deposit_products(request):

    # api 불러와야할때 사용하세요.
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    
    # 이 아래는 삭제해도됩니다.
    response = requests.get(url).json()
    
    for li in response.get("result").get('baseList'):
        data_baseList={
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm'),           
            'fin_prdt_nm' : li.get('fin_prdt_nm'),         
            'etc_note' : li.get('etc_note'),     
            'join_deny'  : li.get('join_deny'),     
            'join_member' : li.get('join_member'),         
            'join_way' : li.get('join_way'),             
            'spcl_cnd' : li.get('spcl_cnd'),   
        }
        serializer_baseList = DepositProductsSerializer(data=data_baseList)
        if serializer_baseList.is_valid(raise_exception=True):
            serializer_baseList.save()
        
    for li in response.get("result").get('optionList'):
        print(li)
        products = DepositProducts.objects.get(fin_prdt_cd=li["fin_prdt_cd"])
    
        # data_optionList={
        #     'fin_prdt_cd' : li.get('fin_prdt_cd'),
        #     'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
        #     'intr_rate' : li.get('intr_rate'),
        #     'intr_rate2' : li.get('intr_rate2'),
        #     'save_trm' : li.get('save_trm'),
        # }
        serializer_optionList = DepositOptionsSerializer(data=li)
        if serializer_optionList.is_valid(raise_exception=True):
            serializer_optionList.save(product=products)
            

    return JsonResponse({ 'message': 'okay' })



# 전체 정기예금 상품 목록 출력 & 데이터 삽입
@api_view(['GET','POST'])
def deposit_products(request):
    API_KEY = settings.API_KEY    
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.data)



# 특정 삼품의 옵션 리스트 출력
@api_view(['GET'])
def deposit_product_options(request,fin_prdt_cd):
    
    if request.method == 'GET':
        options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializer(options, many = True)
        return Response(serializer.data)

# 가장 높은 금리 옵션 찾기 => 해당 옵션의 외래키로 설정된 금융상품 찾기
@api_view(['GET'])
def top_rate(request):
    
    # 가장 높은 금리 옵션 찾기
    highest_option = DepositOptions.objects.order_by('-intr_rate2').first()
    serializer1 = DepositOptionsSerializer(highest_option)

    # 해당 옵션의 외래키로 설정된 금융상품 찾기
    if highest_option:

        highest_product = highest_option.product
        serializer2 = DepositProductsSerializer(highest_product)
        
        data = {
            'deposit_product':serializer1.data,
            'options':serializer2.data,
        }
        return Response(data)
    