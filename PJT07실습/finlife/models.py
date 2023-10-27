from django.db import models

# Create your models here.


class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)     # 금융 상품 코드
    kor_co_nm = models.TextField(default=-1, blank=True, null=True)                  # 금융 회사명
    fin_prdt_nm = models.TextField(default=-1, blank=True, null=True)                # 금융 상품명
    etc_note = models.TextField(default=-1, blank=True, null=True)                   # 금융 상품 설명
    join_deny  = models.IntegerField(default=-1, blank=True, null=True)              # 가입제한(1:제한없움, 2: 서민전용, 3:일부제한)
    join_member = models.TextField(default=-1, blank=True, null=True)                # 가입 대상
    join_way = models.TextField(default=-1, blank=True, null=True)                   # 가입 방법
    spcl_cnd = models.TextField(default=-1, blank=True, null=True)                   # 우대 조건


	
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)       # 외래 키(DepositProducts 클래스참조)
    fin_prdt_cd = models.TextField(default=-1, blank=True, null=True)    # 금융 상품 코드
    intr_rate_type_nm = models.CharField(default=-1, blank=True, null=True,max_length=100) #저축 금리 유형명
    intr_rate = models.FloatField(default=-1, blank=True, null=True)     # 저축 금리
    intr_rate2 = models.FloatField(default=-1, blank=True, null=True)    # 최고우대금리
    save_trm = models.IntegerField(default=-1, blank=True, null=True)    # 저축기간 (단위 : 개월)
