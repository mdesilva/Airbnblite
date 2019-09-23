<template>
<div>
    <div v-bind:key="property.id" v-for="property in properties">
        <Property v-bind:property="property"/>
    </div>
</div>
</template>

<script>
import Property from './Property.vue'

export default {
    name: "Properties",
    components: {
        Property
    },
    props: ["properties"]
}
</script>

<style scoped>

</style>