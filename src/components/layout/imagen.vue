<template >
    <div >
        
        
        <form @submit.prevent="subirImagen" enctype="multipart/form-data">
            <input  @change="clickImagen($event)" type="file"  accept="image/*">
            <input  class="button is-secondary" type="submit" value="Guardar Cambios" >

          
            
        </form>

       
           


        
    </div>
   
</template>
<script>
import {storage} from '../../firebase/init'
const ref =storage.ref()
export default {
    data(){
        return{
            imagenes:[],
            imagen:null,
            imagendesc:false,

        }
    },
    mounted(){
              
            
        },
    methods:{
        clickImagen(e){
            this.imagen=e.target.files[0]
            console.log(this.imagen)
        },
        subirImagen(){
            ///crear Referencia donde se quiere subir
            const refImag = ref.child('imagenes/' + this.imagen.name)
            const metadata = {contentType: "img/jpeg" }
            refImag.put(this.imagen, metadata)
            .then( (e) =>console.log(e));

            

            

            
        },

        
    }
    
}
</script>

<style scoped>
.imgRedonda {
    
    border-radius:160px;
    border:10px solid #666;
}
</style>