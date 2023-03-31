<template>
  <v-app>
    <v-main>
      <v-botttom-navigation>
        <v-btn :to="{name: 'home'}" prepend-icon="mdi-home">Home</v-btn>
        <v-btn :to="{name: 'about'}" prepend-icon="mdi-information-outline">About</v-btn>
        <v-btn :to="{name: 'helloworld'}" prepend-icon="mdi-new-box">Hello World</v-btn>
      </v-botttom-navigation>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App',

  setup() {

  }
})
</script>
