<template>
    <button
    :value="value"
    @click="toggle()"
    :class="[isToggled ? toggledClasses : 'border-black']"
    class="border border-solid rounded p-2 m-2 lg:hover:bg-red-denner lg:hover:text-white lg:hover:border-transparent">
    {{ value }}</button>
</template>

<script>
export default {
    props: {
        value: String,
    },

    data(){
        return {
            isToggled: false,
            toggledClasses: 'text-white border-transparent bg-red-denner',
        }
    },

    methods: {
        toggle: function(){
            this.isToggled = !this.isToggled;
        }
    }
}
</script>