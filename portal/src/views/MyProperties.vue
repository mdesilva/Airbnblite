<template>
<div>
    <div v-bind:key="property.id" v-for="property in userProperties">
        <Property v-bind:property="property"/>
    </div>
</div>
</template>

<script>


import Property from "../components/Property.vue";
import axios from 'axios';

export default {
    name: "MyProperties",
    components: {
        Property
    },
    data() {
        return {
            userProperties = []
        }
    },
    created(): {
        axios.get("").then(res => userProperties = res.data)   
    }
}
</script>