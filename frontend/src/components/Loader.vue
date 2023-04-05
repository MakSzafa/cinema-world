<template>
    <div class="loader">
    </div>
</template>

<script>
export default {
    name: "Loader",
}
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";

.loader {
    margin-left: auto;
    margin-right: auto;
    margin-top: 10rem;
    animation-duration: 1s !important;
    border-width: 5px !important;
    border-color: $primary !important;
    border-right-color: transparent !important;
    border-top-color: transparent !important;
    height: 10rem !important;
    width: 10rem !important;

    @include mobile {
        margin-top: 5rem;
        height: 7rem !important;
        width: 7rem !important;
    }
}
</style>