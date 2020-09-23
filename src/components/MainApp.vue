<template>
    <div id="main">
        <Navbar class="fixed top-0 w-full z-10" v-bind:loggedIn="this.$store.getters.isLoggedIn" v-bind:username="this.$store.getters.currentUser" v-bind:userId="this.$store.getters.userId"></Navbar>
        <div class="content mt-32">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import Navbar from './Navbar';

    export default {
        name: 'main-app',
        components: {Navbar},
    }
</script>
