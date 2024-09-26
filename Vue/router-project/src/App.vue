<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/video">Video</RouterLink>
    <RouterLink to="/photo">Photo</RouterLink>
    <RouterLink to="/prompt">Prompt</RouterLink>
  </nav>

  <RouterView></RouterView>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
export default {

}
</script>

<style>

</style>