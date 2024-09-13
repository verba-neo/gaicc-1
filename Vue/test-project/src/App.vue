<!-- App.vue -->
<template>
  <!-- 3. 보여준다. -->
  <NavBar/>
  <div class="container mt-3 mb-5">
    <Header />
    <hr>
    <VideoPlayer />
    <hr>
    <NewsSection />
    <hr>
    <UserPrompt />
  </div>
</template>

<script>
// 1. import 꺼낸다.
import NavBar from './components/NavBar.vue'
import Header from './components/Header.vue'
import VideoPlayer from './components/VideoPlayer.vue'
import NewsSection from './components/NewsSection.vue'
import UserPrompt from './components/UserPrompt.vue'

export default {
  // 2. 등록한다.
  components: { 
    NavBar,
    Header, 
    VideoPlayer, 
    NewsSection, 
    UserPrompt,
  }
}
</script>

<style></style>