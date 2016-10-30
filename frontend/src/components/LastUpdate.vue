<template>
</template>

<script>
import HeaderComponent from './components/header.vue'
import OtherComponent from './components/other.vue'
export default{
    data(){
        return{
            msg:'hello vue'
        }
    },
    components:{
        'other-component':OtherComponent,
        HeaderComponent,
    }
}
</script>
