import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PhotoView from '../views/PhotoView.vue'
import PromptView from '@/views/PromptView.vue'
import VideoView from '@/views/VideoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: HomeView },
    { path: '/video', component: VideoView },
    { path: '/photo', component: PhotoView },
    { path: '/prompt', component: PromptView },
  ]
})

export default router
