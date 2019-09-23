import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import AllProperties from './views/AllProperties.vue'
import Login from './views/Login'
import Admin from './views/Admin'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/allProperties',
      name: 'AllProperties',
      component: AllProperties
    },
    {
      path: '/login',
      name: "login",
      component: Login
    },
    {
      path: '/admin',
      name: "admin",
      component: Admin,
      meta: {
        requiresAuth: true
      }
    }
  ]
})

let isLoggedIn = function(){
  console.log("Log in check")
  return false;
}

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (isLoggedIn()) {
      next()
    }
    else {
      next({
        path: '/login',
        query: { redirect: to.fullPath}
      })
    }
  } else {
    next()
  }
})

export default router