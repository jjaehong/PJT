<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref } from 'vue'


const API_KEY = import.meta.env.VITE_API_KEY
const router = useRouter()
</script>


<template>
  <div class="container">
    <header>
      <nav class="navbar navbar-dark bg-dark navbar-expand-md fixed-top">
        <div class="container-fluid">
          <RouterLink :to="{ name: 'Home' }" class="navbar-brand">MyTube</RouterLink>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink :to="{ name: 'Home' }" class="nav-link">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'Search' }" class="nav-link">Search</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'Later' }" class="nav-link">Later</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'LikeChannel' }" class="nav-link">Channel</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    
  </header>
  <br><br><br>
  <h5 @click="$router.go(-1)">← 뒤로가기</h5>
  <RouterView />
</div>
</template>

<style scoped>

.container {
  width: 90%;
  margin: 0 auto;
}

</style>
