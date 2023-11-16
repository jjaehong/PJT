<template>
  <div>
    <h1>나중에 볼 동영상</h1>
    <div v-if="videoData.length" class="container d-flex flex-wrap">
      <CardLater v-for="video in videoData" :video="video"/>
    </div>
    <p v-else>등록된 비디오 없음</p>
  </div>
</template>

<script setup>
import CardLater from '@/Components/CardLater.vue'


const videoData = JSON.parse(localStorage.getItem('video'))
</script>

<style scoped>
.container {
    display: inline-block;
    gap: 20px;

}
</style>