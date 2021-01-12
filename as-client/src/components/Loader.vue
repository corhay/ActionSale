<template>
    <div>
        <p>A la recherche de sale{{dots}}</p>
    </div>
</template>
<script>
export default {
    data(){
        return{
            dots: ".\xa0\xa0",
        }
    },
    created(){
        this.animate();
    },
    methods:{
        animate: function(){
            setInterval(this.addDots, 300);
        },

        addDots: function(){
            if(this.dots.lastIndexOf('\xa0') > -1){
                this.dots = this.dots.replace('\xa0', '.');
            } else{
                this.dots = '.\xa0\xa0';
            }
        },
    }
}
</script>