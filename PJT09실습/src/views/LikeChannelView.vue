<template>
  <div>
    <h1>좋아하는 채널</h1>
    <div v-if="channelData.length" class="container d-flex flex-wrap">
      <ChannelLike v-for="channel in channelData" :channel="channel"/>
    </div>
    <p v-else>등록된 채널 없음</p>
  </div>
</template>

<script setup>
import ChannelLike from '@/Components/ChannelLike.vue'


const channelData = JSON.parse(localStorage.getItem('channel'))
</script>

<style scoped>
.container {
    display: inline-block;
    gap: 20px;

}
</style>