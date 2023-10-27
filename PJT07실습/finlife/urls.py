from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('save-deposit-products/', views.save_deposit_products),    # 정기예금 상품 목록 DB에 저장
    path('deposit-products/', views.deposit_products),              # 전체 정기예금 상품 목록 출력 & 데이터 삽입
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options),  # 특정 삼품의 옵션 리스트 출력
    path('deposit-products/top_rate/', views.top_rate),                                 # 가입 기간에 상관없이 최고금리가 가장 높은 금융상품과 해당 상품의 옵션리스트 출력
]
