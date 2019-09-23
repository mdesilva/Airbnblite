<template>
<div>
    <div class="property">
        <h1> {{ property.name }} </h1>
        <h3> {{ property.type }} </h3>
        <h6> {{ property.price }} </h6>
    </div>
</div>
</template>
<script>
export default {
    name: "Property",
    props: ["property"]
}
</script>

<style scoped>

</style>