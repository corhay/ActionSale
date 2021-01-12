<template>
  <div id="wrapper" class="flex flex-col justify-center">
    <hr class="rounded border-gray-700 m-4 mt-1 md:w-1/3 md:mx-auto" />
    <div id="quickfilters" class="flex justify-center items-stretch flex-wrap md:w-1/3 md:mx-auto">
    <span>
      <Loader v-if="!dataLoaded"></Loader>
    </span>
      <span id="initFilters">
        <ToggleButton
            v-for="category in initCategories"
            :key="category"
            :value="category"
            @click.native="savePreselectChoice($event)"
          ></ToggleButton>
      </span>
      <TransitionExpand>
        <span id="extraFilters" v-show="showMoreFilters">
          <ToggleButton
            v-for="category in allCategories"
            :key="category"
            :value="category"
            @click.native="savePreselectChoice($event)"
          ></ToggleButton>
        </span>
      </TransitionExpand>
    </div>
    <transition name="buttonSpin">
    <img
      id="arrow"
      src="@/assets/expand.png"
      alt="Montrer plus"
      @click="toggleFilters"
      :class="showMoreFilters ? '': ''"
      class="w-8 mx-auto mt-4 mb-1 cursor-pointer transform"
    />
    </transition>
    <hr class="border-gray-700 w-full mx-auto transform md:w-1/3" />
  </div>
</template>

<style>
.expand-enter-active,
.expand-leave-active {
  transition-property: height, opacity;
}

.expand-enter,
.expand-leave-to {
  opacity: 0;
}

#arrow{
  transition: 0.5s all 0.2s;
}

</style>

<script>
import ToggleButton from "./ToggleButton";
import TransitionExpand from "./TransitionExpand";
import Loader from './Loader';

export default {
  components: { ToggleButton, TransitionExpand, Loader },
  props: {
    categories: Object
  },
  computed: {
      initCategories: function() {
          return Object.keys(this.categories).splice(0, this.initFilterNum);
        },

      allCategories: function() {
        return Object.keys(this.categories).splice(this.initFilterNum);
      }
    },
  data() {
    return {
      //toggle how many filters are shown
      showMoreFilters: false,
      //number of filters initially shown
      initFilterNum: 3,
      //preselects passed to Home.vue
      preselects: [],
      dataLoaded: false,
    };
  },
  watch: {
    categories: function(){
      this.dataLoaded = true;
    }
  },
  methods: {
    savePreselectChoice: function(event) {
      const preselect = event.target.value;
      const index = this.preselects.indexOf(preselect);
      console.log(index);
      if (index == -1) {
        this.preselects.push(preselect);
      } else {
        this.preselects.splice(index, 1);
      }

      this.$emit("preselects", this.preselects);
    },

    toggleFilters: function() {
      this.showMoreFilters = !this.showMoreFilters;
      var rotation = 'rotateZ(360deg)';
      if(this.showMoreFilters){
        rotation = 'rotateZ(180deg)';
      }
        document.querySelector('#arrow').style.transform = rotation;
    }
  }
};
</script>