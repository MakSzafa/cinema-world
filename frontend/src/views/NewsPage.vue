<template>
  <div class="body">
    <h1 class="title">Nowości</h1>
    <p>Póki co chyba nowości nie ma, więc można ukryć zakładkę</p>
  </div>
</template>

<script>
export default {
  name: "NewsPage",
  mounted() {
    document.title = "Filmarket | Nowości";
  },
};
</script>

<style scoped lang="scss"></style>
