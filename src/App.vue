<template>
  <div  id="app">
    
      
    
      <navegation />
    
      <sidebar/>
      
      <router-view/>
      
        
      
      
    
    
   
   

    
  </div>
</template>


<script>
  import sidebar from '@/components/layout/sidebar'
  import navegation from '@/components/layout/navegation'


  
  export default {
    
    components: {
      
      navegation,
      sidebar
        
        
    },
    data(){
      return{
        

      }
    }
  }

</script>

<style lang="scss">
  @import './scss/App.scss';


</style>