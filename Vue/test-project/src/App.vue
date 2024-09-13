<!-- App.vue -->
<template>
  <!-- 3. 보여준다. -->
  <NavBar></NavBar>
  <div class="container mt-3">
    <Header></Header>
    <hr>
    <VideoPlayer></VideoPlayer>
    <hr>
    <NewsSection></NewsSection>
  </div>
</template>

<script>
// 1. import 꺼낸다.
import NavBar from './components/NavBar.vue'
import Header from './components/Header.vue'
import VideoPlayer from './components/VideoPlayer.vue'
import NewsSection from './components/NewsSection.vue'

export default {
  // 2. 등록한다.
  components: { NavBar, Header, VideoPlayer, NewsSection, }
}
</script>

<style></style>