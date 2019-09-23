<template>
    <div>
        <Properties v-bind:properties="properties" />
    </div>
</template>

<script>
import Properties from "../components/Properties"
import axios from 'axios'

export default {
    name: "AllProperties",
    components: {
        Properties
    },
    data() {
        return {
            properties: []
        }
    },
    created() {
        axios.get("http://localhost:4000/properties")
        .then(res => this.properties = res.data)
    }
}
</script>

<style scoped>

</style>