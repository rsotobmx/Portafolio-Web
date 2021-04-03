<template>
  <div >
    
    <div >
      <Header/>
      
    </div>
    <div >
      <Content/>
     
        

     
    </div>

    <div >
      <Footer/>
    </div>


    
  </div>
</template>


<script>
  import header from './header'
  import content from './content'
  import footer from './footer'
  

  
  export default {
    
    components: {
      'Header': header,
      'Content':content,
      'Footer':footer,
      
      
        
    },
    data(){
      return{
        

      }
    }
  }

</script>

<style >
  
</style>