<template>
  <div>
    <h1>메인 페이지</h1>
    <div v-if="productIsEmpty" class="product-list"> 
      <div v-for="product in products" :key="product.id" class="product-card">
        <!-- 데이터 검색하는데 활용 -->
        <!-- {{ product }} -->
        <img :src="product.image" alt="">
        <strong> {{ product.title }} </strong>
        <p>가격 : ${{ product.price }} </p>
        <button @click="goDetail(product)" >상세페이지로 이동</button>
        <button @click="addCart(product)" >장바구니에 추가</button>
      </div>
    </div>
    <div v-else>
      <strong> 로딩 중이거나, 상품 정보가 없습니다. </strong>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import {useRouter} from 'vue-router'
import axios from 'axios'

const products = ref([])
const storeURL = 'https://fakestoreapi.com/products'


axios.get(storeURL)
  .then((response) =>{
    // console.log(response.data)
    products.value = response.data
  }).catch((error) => {
    console.error(error)
  })

const productIsEmpty = computed(() => {
  return products.value.length > 0 ? true : false
})

const router = useRouter()

// 클릭하면 각 상품의 상세페이지로 이동
// 각 상품의 상세페이지의 id도 같이 넘겨줘야 각 상품의 상세 페이지로 이동 가능  => 인자로 추가 
const goDetail = function (product) {
  console.log(product)
  // 해당 url 주소로 이동
  router.push(`/${product.id}`)
}

// 장바구니 추가(임시데이터 저장으로)
const addCart = function (product) {
  
  // 하나의 데이터만 저장하기
  // 데이터 저장(JSON -> 문자열로 바꿔서 저장 )
  localStorage.setItem('cart',JSON.stringify(product))


  // 여러 데이터 저장하기
  // 중복 체크(데이터 가져오기, 객체로 변환)
  // 현재 localStorage에 저장된 데이터 가져오기
  // 만약 없다면 비어있는 리스트로 초기화
  const existingCart = JSON.parse(localStorage.getItem('cart')) || []
  
  // 중복된 제품이 있는지 확인
  const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.id === product.id)
  
  // 중복이 아니라면 추가
  if (isDuplicate) {
    alert('장바구니에 추가합니다')
    existingCart.push(product)
  } else {
    alert('이미 있는 상품입니다. 장바구니로 이동합니다.')
  }

  // 수정된 카트 데이터를 localStorage에 저장
  localStorage.setItem('cart', JSON.stringify(existingCart))

  router.push('/cart')

}

</script>


<style>
/* global CSS */
.product-list {
  display: flex;
  /* flex-item 요소들이 강제로 한줄에 배치되게 할 것인지(nowrap), 가능한 영역 내에서 벗어나지 않고 여러행으로 나누어 표현(wrap) */
  flex-wrap: wrap;
  gap: 10px;
}

</style>


<style scoped>
/* local CSS */
.product-card {
  border: 1px solid black;
  width: 210px;
}

.product-card img {
  width: 200px;
  height: 200px;
  /*  */
  object-fit: fill;
}

</style>