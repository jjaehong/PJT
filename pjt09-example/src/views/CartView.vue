<template>
    <div>
        <h1>장바구니</h1>
        <div v-if="cartitems">
            {{ cartitems }}
            <div v-if="productIsEmpty" class="product-list">
                <div v-for="product in products" :key="product.id" class="product-card">
                    <!-- 데이터 검색하는데 활용 -->
                    <!-- {{ product }} -->
                    <img :src="product.image" alt="">
                    <strong> {{ product.title }} </strong>
                    <p>가격 : ${{ product.price }} </p>
                    <button @click="goDetail(product)">상세페이지로 이동</button>
                    <button @click="addCart(product)">장바구니에 추가</button>
                </div>


            </div>

            <div v-else>
                <strong>장바구니에 담긴 상품이 없습니다.</strong>
            </div>
        </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const cartitems = ref(null)
const router = useRouter()

cartitems.value = JSON.parse(localStorage.getItem('cart')) || []

const goDetail = function (product) {
  // 해당 url 주소로 이동
  router.push(`/${product.id}`)
}

const removeCart = (product) => {
    // localStorage 에서 삭제
    // 현재 cartItems.value에서 삭제
    // 1. 현재 localStorage에 저장된 데이터를 가져오기
    const existingCart = JSON.parse(localStorage.getItem('cart'))

    // 2. 삭제할 아이템 index 검색
    const itemIdx = existingCart.findindex((item) => item.id ===product.id)

    // 3. 데이터 삭제
    existingCart.splice(itemIdx,1)

    // 4. 삭제된 데이터를 기준으로 데이터를 반영
    localStorage.setItem('cart',JSON.stringify(existingCart))
    cartitems.value = existingCart
 
}


</script>

<style scoped></style>