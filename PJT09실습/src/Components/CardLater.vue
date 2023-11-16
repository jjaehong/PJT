<template>
    <div class="card" @click="goDetail(video)">
        <img :src="thumbnail" alt="이미지">
        <div>
            {{ title }}
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue'
import axios from 'axios'


const props = defineProps({
    video: String,
})


const API_KEY = import.meta.env.VITE_API_KEY
const youtubeURL = 'https://www.googleapis.com/youtube/v3/videos'
const title = ref()
const thumbnail = ref()
const router = useRouter()


const getVideo = axios.get(youtubeURL, { params: { key: API_KEY, part: 'snippet', id: props.video } })
  .then((result) => {
    title.value = result.data.items[0].snippet.title
    thumbnail.value = result.data.items[0].snippet.thumbnails.high.url
  })
  .catch((error) => {
    console.log(error)
  })


const goDetail = function (video) {
    router.push({ name:'Detail', params: { videoId: video }})
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