<template>
  <div id="app">
    <div id="nav">
      <Header/>
      <router-link to="/">Home</router-link> |
      <router-link to="/allProperties">All Properties </router-link> |
      <router-link to="/admin"> Admin </router-link>
    </div>
    <router-view/>
  </div>

</template>

<script>
import Header from './components/Header.vue'

export default {
  name: "App",
  components: {
    Header
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

