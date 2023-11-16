<template>
    <div>
        <h1>비디오 검색</h1>
        <form @submit.prevent="input">
            <input type="text" class="input" value="검색어를 입력하세요.">
            <input type="submit" class="btn btn-success">
        </form>
        <div class="container d-flex flex-wrap">
            <Card v-for="result in resultList" :result="result"/>
        </div>

    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import Card from '@/components/Card.vue'


const API_KEY = import.meta.env.VITE_API_KEY
const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const resultList = ref()
const q = ref()


const input = function (event) {
    q.value = event.currentTarget[0].value
    axios.get(youtubeURL, {params: {key: API_KEY, part: 'snippet', type: 'video', q: q.value, fields: 'items', maxResults: 6}})
    .then((request) => {
    resultList.value = request.data.items
    })
    .catch((error) => {
    console.log(error)
    })
}

</script>

<style scoped>
* {
    margin-bottom: 20px;
}

form {
    display: flex;
}

form .input {
    width: 80%;
}

.container {
    display: inline-block;
    gap: 20px;

}
</style>