<template>
  <div id="discountItem" class="mx-auto">
    <img :src='"@/assets/" + this.shop + ".png"' :alt="shop" class="w-32 h-8" />
    <div id="product" class="flex">
      <div id="description" class="w-2/3 text-left">
        <p>{{product.Title}}</p>
        <div id="insteadof" v-if="product.DiscountPrice !== null && product.RegularPrice !== null">
          <span>{{parseFloat(product.DiscountPrice).toFixed(2)}} au lieu de {{parseFloat(product.RegularPrice).toFixed(2)}}</span>
        </div>
        <div id="discountPrice" v-else-if="product.DiscountPrice !== null">
          <span>{{product.DiscountPrice}}</span>
        </div>
        <span v-if="product.Discount !== '' && product.Discount !== null">Rabais: <span class="font-bold">{{product.Discount}}</span></span>
      </div>
      <div id="image" class="w-1/3">
          <img :src="product.imageLink" class="mx-auto">
      </div>
    </div>
    <hr class="rounded border-gray-700 m-4" />
  </div>
</template>

<script>
export default {
  props: {
    product: Object,
    shop: String
  },
};
</script>