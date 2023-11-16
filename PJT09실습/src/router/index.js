import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DetailView from '@/views/DetailView.vue'
import LaterView from '@/views/LaterView.vue'
import LikeChannelView from '@/views/LikeChannelView.vue'
import SearchView from '@/views/SearchView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/:videoId',
      // path: '/:videoId/:title/:date/:description',
      name: 'Detail',
      component: DetailView
    },
    {
      path: '/Later',
      name: 'Later',
      component: LaterView
    },
    {
      path: '/LikeChannel',
      name: 'LikeChannel',
      component: LikeChannelView
    },
    {
      path: '/Search',
      name: 'Search',
      component: SearchView
    }
  ]
})

export default router
