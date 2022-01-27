<template>
  <div class="body">
    <h1 class="title">tytul jako zmienna</h1>
  </div>
</template>

<script>
export default {
  name: 'ProductPage',
  mounted() {
    document.title = 'Filmarket | :product_name' // TODO: tu bedzie przy wyciaganiu danych produktu
  }
}
</script>

<style scoped lang="scss">

</style>