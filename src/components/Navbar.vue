<template>
  <div id="header">
    <nav
      class="flex items-center justify-between flex-wrap bg-red-denner px-6 pt-3"
      :class="navDrop ? 'pb-1' : 'pb-3'"
    >
      <div class="flex items-center flex-shrink-0 text-white mr-6">
        <a href="/">
          <img src="@/assets/logo2.png" alt="ActionSale" class="w-24 h-16" />
        </a>
      </div>
      <div class="block md:hidden">
        <button
          v-on:click="toggleNav"
          class="flex items-center px-3 py-2 border rounded text-white border-white menu-button"
        >
          <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <title>Menu</title>
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
          </svg>
          <transition name="fade">
            <img v-if="newNotification" src="@/assets/alert.svg" alt="NOUVEAU" class="menu-badge" />
          </transition>
        </button>
      </div>
      <div class="hidden w-full block flex-grow md:flex md:items-center md:w-auto md:visible">
        <div class="text-sm">
          <a
            href="/"
            class="block mt-4 md:inline-block md:mt-0 text-teal-200 hover:text-white mr-4"
          >Accueil</a>
        </div>
        <transition name="fade">
          <div id="install" v-if="pwaInstallable">
            <span
              @click="promptInstall"
              class="block mt-4 md:inline-block md:mt-0 text-teal-200 hover:text-white mr-4 cursor-pointer"
            >Installer</span>
          </div>
        </transition>
      </div>
    </nav>
    <!-- Mobile nav section -->
    <div id="mobile menu" class="flex flex-col bg-red-denner px-6 pb-3 items-end" v-if="navDrop">
      <div class="flex justify-center">
        <a
          href="/"
          class="block mt-4 md:inline-block md:mt-0 text-teal-200 hover:text-white mr-4"
        >Accueil</a>
        <transition name="fade">
          <div id="install" v-if="pwaInstallable" class="menu-button">
            <span
              @click="promptInstall"
              class="block mt-4 md:inline-block md:mt-0 text-teal-200 hover:text-white mr-4 cursor-pointer"
            >Installer</span>
            <img src="@/assets/alert.svg" alt="NOUVEAU" class="button-badge" />
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    loggedIn: Boolean,
    username: String,
    userId: Number
  },
  data() {
    return {
      navDrop: false,
      pwaInstallable: false,
      newNotification: false,
      defferredPrompt: null
    };
  },
  mounted() {
    window.addEventListener("beforeinstallprompt", e => {
      e.preventDefault();
      //Stashing the event for later use
      this.defferredPrompt = e;
      //Add install button now that it is available
      this.pwaInstallable = true;
      this.newNotification = true;
    });
  },
  methods: {
    toggleNav: function() {
      if (this.newNotification && !this.navDrop) {
        this.newNotification = false;
      }

      this.navDrop = !this.navDrop;
    },

    logout: function() {
      axios.post("/logout").then(() => (location.href = "/home"));
    },

    //prompts user for pwa install
    promptInstall: function() {
      //show install prompt
      this.defferredPrompt.prompt();
      //wait for user choice
      this.defferredPrompt.userChoice.then(choiceResult => {
        if (choiceResult.outcome === "accepted") {
          console.log("yay install");
        } else {
          console.log("no install nono");
        }
      });
    }
  }
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.menu-button .menu-badge {
  display: inline-block;
  position: absolute;
  top: 16px;
  right: 10px;
  width: 1.5em;
}

.button-badge {
  display: inline-block;
  position: absolute;
  top: 5.5em;
  right: 1.6em;
  width: 1em;
}
</style>
