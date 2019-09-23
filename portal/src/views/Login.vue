<template>
<div>
    <div id="loginForm">
        <form @submit.prevent="loginUser"> 
            <input type="text" v-model="username" placeholder="Username">
            <input type="password"  v-model="password" placeholder="Password">
            <button type="submit"> Login </button>
        </form>
    </div>
</div>
</template>

<script>

import axios from 'axios'

export default {
    name: "Login",
    data() {
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        loginUser() {
            axios.post("http://localhost:4000/user/login", {
                username: this.username,
                password: this.password
            })
            .then(res => console.log(`The response to login the user was ${res}`))
        }
    }
}
</script>

<style scoped>
</style>