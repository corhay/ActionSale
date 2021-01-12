<template>
  <div id="container">
    <div
      id="maskingDiv"
      class="bg-black w-full absolute top-0 z-20 opacity-75 masking-div"
    ></div>
    <transition name="slide">
      <div
        id="info bubble"
        v-if="opened"
        class="rounded-lg border-black border bg-black z-30 absolute text-white flex flex-col mx-2 px-2 opacity-75 mt-12 md:w-1/3 bubble"
      >
        <div class="flex">
          <p class="text-justify p-4 text-gray-200">
            Les produits affichés sont tirés des sites web des supermarchés
            mentionnés. Les données sont mises à jour chaque mardi.
          </p>
          <div id="close button" class="flex justify-end">
            <span
              @click="$emit('closeBubble')"
              class="m-4 cursor-pointer h-1 hover:text-red-denner text-3xl"
              >X</span
            >
          </div>
        </div>
        <p class="text-left px-4 py-2">
          <img src="@/assets/mig.png" alt="Migros:" class="w-1/4" />
          <a
            href="https://produits.migros.ch/offres/actions?region=gmvd"
            class="underline text-blue-700"
            >Actions du canton de Vaud</a
          >
        </p>
        <p class="text-left px-4 py-2">
          <img src="@/assets/coop.png" alt="Coop:" class="w-1/4" />
          <a
            href="https://www.coop.ch/fr/enseignes/supermarche/actions.html"
            class="underline text-blue-700"
            >Actions du supermarché de Chexbres</a
          >
        </p>
        <p class="text-left px-4 py-2">
          <img src="@/assets/denn.png" alt="Denner:" class="w-1/4" />
          <a
            href="https://www.denner.ch/fr/actions/list/of/actions-actuelles/"
            class="underline text-blue-700"
            >Actions en Suisse</a
          >
        </p>
        <p class="text-sm text-gray-800 p-2">Créé par Cor</p>
      </div>
    </transition>
  </div>
</template>
<script>
export default {
    data(){
        return{
            opened: false,
        }
    },
    created(){
        window.setTimeout(() => {
            this.opened = true;
        }, 100)
    },
}
</script>
<style>

@media (min-width: 768px) {
    .bubble {
        left: 33%;
        right: 33%;
    }
}

.masking-div {
  height: 9999px;
}

.slide-enter-active {
  transition-property: all;
  transition-duration: 0.3s;
}

.slide-enter,
.slide-leave-to {
  transform: translateY(-50px);
  opacity: 0;
}
</style>