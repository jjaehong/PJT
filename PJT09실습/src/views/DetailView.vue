<template>
  <div class="container">
    <h1> {{ title }} </h1>
    <div>업로드 날짜: {{ date }}</div>
    <iframe width="560" height="315" :src=videoUrl title="YouTube video player" frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen></iframe>
    <div>{{ description }}</div>
    <br>
    <div class="d-flex">
    <div v-if="isDuplicate">
      <button @click="remove(route.params.videoId)" class="btn btn-primary">동영상 삭제</button>
    </div>
    <div v-else>
      <button @click="addVideo(route.params.videoId)" class="btn btn-primary">동영상 저장</button>
    </div>
    <div v-if="channelDuplicate" class="mx-3">
      <button @click="removeChannel(channelId)" class="btn btn-warning">채널 삭제</button>
    </div>
    <div v-else class="mx-3">
      <button @click="addChannel(channelId)" class="btn btn-warning">채널 저장</button>
    </div>
  </div>
  </div>
</template>


<script setup>
import axios from 'axios'
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router';


const route = useRoute()
const API_KEY = import.meta.env.VITE_API_KEY
const youtubeURL = 'https://www.googleapis.com/youtube/v3/videos'
const title = ref()
const description = ref()
const date = ref()
const channelId = ref()
const videoUrl = ref(`https://www.youtube.com/embed/${route.params.videoId}`)


const check = ref()
check.value = JSON.parse(localStorage.getItem('video')) || []


const getVideo = axios.get(youtubeURL, { params: { key: API_KEY, part: 'snippet', id: route.params.videoId } })
  .then((result) => {
    channelId.value = result.data.items[0].snippet.channelId
    title.value = result.data.items[0].snippet.title
    description.value = result.data.items[0].snippet.description
    date.value = result.data.items[0].snippet.publishedAt
  })
  .catch((error) => {
    console.log(error)
  })


  const isDuplicate = computed(() => {
    return check.value.find((item) => item === route.params.videoId) ? true : false
  })


const addVideo = (videoId) => {
  const videoData = JSON.parse(localStorage.getItem('video')) || []
  videoData.push(videoId)
  localStorage.setItem('video', JSON.stringify(videoData))
  check.value = JSON.parse(localStorage.getItem('video')) || []
}


const remove = (id) => {
  const itemIdx = check.value.findIndex((item) => item === id)
  check.value.splice(itemIdx, 1)
  localStorage.setItem('video', JSON.stringify(check.value))
}


const channelCheck = ref()
channelCheck.value = JSON.parse(localStorage.getItem('channel')) || []


const channelDuplicate = computed(() => {
    return channelCheck.value.find((item) => item === channelId.value) ? true : false
})


const addChannel = (channelId) => {
  const channelData = JSON.parse(localStorage.getItem('channel')) || []
  channelData.push(channelId)
  localStorage.setItem('channel', JSON.stringify(channelData))
  channelCheck.value = JSON.parse(localStorage.getItem('channel')) || []
}


const removeChannel = (channelId) => {
  const itemIdx = channelCheck.value.findIndex((item) => item === channelId)
  channelCheck.value.splice(itemIdx, 1)
  localStorage.setItem('channel', JSON.stringify(channelCheck.value))
}

</script>


<style scoped>
.container {
  gap: 20px;
}
</style>