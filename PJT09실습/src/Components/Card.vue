<template>
    <div class="card" @click="goDetail(result)">
        <img :src="result.snippet.thumbnails.high.url" alt="이미지">
        <div>
            {{ result.snippet.title }}
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue'
import DetailView from '@/views/DetailView.vue';


const router = useRouter()


defineProps({
    result: Object,
})


const goDetail = function (result) {
    // router.push({ name:'Detail', params: { videoId: result.id.videoId, title: result.snippet.title, date: result.snippet.publishTime, description: result.snippet.description }})
    router.push({ name:'Detail', params: { videoId: result.id.videoId }})
    console.log(result)
}

</script>

<style scoped>
.card {
    width: 30%;
    border: 1px solid black;
    object-fit: fill;
    display: flex;
}


img {
    width: 100%;
    height: 100%;
}

</style>