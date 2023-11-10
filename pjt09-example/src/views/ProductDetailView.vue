<template>
    <div>
        <h1>상세 페이지</h1>
        <div v-if="product" class="product-card">
            <!-- 데이터 검색하는데 활용 -->
            <!-- {{ product }} -->
            <img :src="product.image" alt="">
            <strong> {{ product.title }} </strong>
            <p>가격 : ${{ product.price }} </p>
        </div>
        <div v-else>
            <strong> 로딩 중... </strong>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'
const storeURL = `https://fakestoreapi.com/products/${productId}`
const route = useRoute()
const product = ref('')

// 파라미터에 있는 변수값을 가져와서 저장
const productId = route.params.productId
console.log(productId)


axios.get(storeURL)
    .then((response) => {
        // console.log(response.data)
        product.value = response.data
    }).catch((error) => {
        console.error(error)
    })



</script>

<style scoped>
.product-card {
  border: 1px solid black;
  width: 210px;
}

</style>