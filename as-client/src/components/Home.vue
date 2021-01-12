<template>
  <div class="flex flex-col">
    <InfoBubble v-if="infoPopped" @closeBubble="popInfo"></InfoBubble>
    <div id="categories" class="flex flex-col mx-auto mt-2 p-4 w-full z-0">
      <p class="mx-auto text-2xl">
        Tu veux quoi
        <span
          class="border border-gray-800 rounded-full bg-gray-800 text-white cursor-pointer text-base px-2 py-1"
          title="Informations sur les produits affichés"
          @click="popInfo"
        >?</span>
      </p>
      <FilterSelection v-bind:categories="categories" @preselects="savePreselectChoices"></FilterSelection>
      <input
        type="text"
        v-model="userSearch"
        placeholder="Recherche personalisée"
        class="border border-solid border-black rounded placeholder-black px-2 py-1 my-4 md:w-1/3 md:mx-auto bg-transparent"
      />
      <div id="discountList" class="mx-auto md:w-2/3">
        <div v-for="(shop, name) in filteredDiscounts" :key="name">
          <div v-for="(product, itemName, index) in shop" :key="index">
            <DiscountDisplay v-bind:product="product" v-bind:shop="name"></DiscountDisplay>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DiscountDisplay from "./DiscountDisplay";
import FilterSelection from "./FilterSelection";
import InfoBubble from "./InfoBubble";

export default {
  name: "home",
  components: { DiscountDisplay, FilterSelection, InfoBubble },
  data() {
    return {
      //utility functions
      utils: require("../utils"),
      //user chosen categories
      types: [],
      //available categories
      categories: {},
      //all discounts this week
      weekDiscounts: [],
      //discounts filtered by search
      filteredDiscounts: {},
      //the users search
      userSearch: "",
      //determining if the info button has been pressesd
      infoPopped: false
    };
  },
  computed: {},
  created() {
    this.getWeekDiscounts();
    this.getCategories();
  },
  mounted() {},
  watch: {
    userSearch: function() {
      this.search();
    }
  },
  methods: {
    popInfo: function() {
      this.infoPopped = !this.infoPopped;
      if (this.infoPopped) {
        document.querySelector("body").style.overflow = "hidden";
      } else {
        document.querySelector("body").style.overflow = "visible";
      }
    },

    savePreselectChoices: function(passedPreselects) {
      this.types = passedPreselects;
      this.search();
    },

    addPreselections: function() {
      var keywords = "";
      for (let i = 0; i < this.types.length; i++) {
        this.categories[this.types[i]].forEach(keyword => {
          keywords += keyword + " ";
        });
      }

      return keywords;
    },

    search: function() {
      var preselects = this.addPreselections();
      //check if search is not empty
      if (this.userSearch !== "" || preselects !== "") {
        //build regex
        var searchReg = this.utils.buildRegex(
          this.userSearch + " " + this.addPreselections()
        );
        console.log(searchReg);

        //loop through stores discounts
        for (let i = 0; i < Object.keys(this.weekDiscounts).length; i++) {
          var shop = Object.keys(this.weekDiscounts)[i];
          //add property of corresponding shop e.g. 'mig' 'coop' or 'denn'
          this.filteredDiscounts[shop] = [];
          var shopDiscounts = this.weekDiscounts[shop];

          //match regex with all items
          shopDiscounts.forEach(discount => {
            var matches = discount.Title.match(searchReg);
            if (matches !== null) {
              this.filteredDiscounts[shop].push(discount);
            }
          });
        }
        console.log(this.filteredDiscounts);
        this.$forceUpdate();
      } else {
        this.filteredDiscounts = {};
        this.$forceUpdate();
      }
    },

    getCategories: function() {
      axios
        .get("https://as-api.herokuapp.com/v1/products/categories")
        .then(response => {
          if (response.status == 200) {
            this.categories = response.data;
          }
        })
        .catch(function(error) {
          alert("couldn't get categories: " + error.message);
        });
    },

    getWeekDiscounts: function() {
      axios
        .get("https://as-api.herokuapp.com/v1/discounts/current")
        .then(response => {
          if (response.status == 200) {
            this.weekDiscounts = response.data;
            //console.log("data: " + response.data);
          }
        })
        .catch(function(error) {
          alert("couldn't get all discounts: " + error.message);
        });
    }
  }
};
</script>
