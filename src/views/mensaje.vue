<template>
<div   class="container mt-50">
       <div class="columns">
           <div class="column is-10 is-offset-1">
           
                     
                  <h3 class="title is-3">Tabla De Mensajes</h3><hr/>
                  <button @click.prevent="mostrarPresentacion"  class="button is-secondary"> ver lista de mensajes </button>
              
                  <table class=" table is-hoverable  is-fullwidth">
                        <thead>
                            <tr>
                            
                            <th scope="col">Nombre</th>
                            <th scope="col">telefono</th>
                            <th scope="col">correo</th>
                            <th scope="col">mensaje</th>
                            <th scope="col">Leido</th>
                            <th scope="col">eliminar</th>
                            <th scope="col">Marcar como leido</th>
                            </tr>
                        </thead>
                        <tbody >
                            <tr v-for="mensaje in mensajes" :key="mensaje.id" >
                               
                                <td>{{ mensaje.nombre }}</td>
                                <td>{{ mensaje.telefono}}</td>
                                <td>{{ mensaje.correo }}</td>
                                <td>{{ mensaje.mensaje }}</td>
                                <td>{{ mensaje.leido }}</td>
                               
                                <td><button class="button is-danger" @click.prevent="borrar(mensajes,mensaje.id)" >Eliminar</button></td>
                                <td><button class="button is-warning" @click.prevent="leido(mensajes,mensaje.id,mensaje.nombre,mensaje.url)">Leido</button></td>
                                
                            </tr>
                            
                          
                        
                        </tbody>
                    </table>
           </div>
        </div>

</div>


</template>
<script>
import '@/firebase/init'
import firebase from 'firebase'
export default {
    data(){
        return{
             mensajes:[],
            mensaje: {
                id:'',
                nombre:'',
                categoria:'',
                subcategoria:'',
                desarrollo:'',
                url: '' 
             },
        }

    },
    methods:{
         mostrarPresentacion(){
            //var user = firebase.auth().currentUser;
            var db=firebase.firestore();
            

             db.collection("usuarios").where("mensajes",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                    
                    
                    this.mensajes=doc.data().mensajes
                    console.log(this.mensajes)
                    
                    
                    //tabla.innerHTML =' <tr> <th scope="row">'+ doc.data().array_id +'</th> <td> <br>'+ doc.data().array_nombrevideo+'</td><br> <td><br>'+ doc.data().array_categoria +'</td><br>  <td><br>'+ doc.data().array_subcategoria +'</td><br> <td><br>'+ doc.data().array_enlace +'</td><br>  </tr'
                    

                    
                });

            });
                


            },
            leido(array,pos){ 
            var user = firebase.auth().currentUser;
            var db=firebase.firestore();
            console.log(array[pos-1])
            var aux=array

            aux[pos-1].leido=true

        
                    db.collection("usuarios").doc(user.photoURL)


                    
                    .update({
                        mensajes: aux
                        
                    })
                    .then(() => {
                        console.log("se guardo correctamente");
                           
                                  

                    })
                    .catch((error) => {
                        // The document probably doesn't exist.
                        console.error("Error : ", error);
                    });

                   


             
           
            
            

            
        },
        borrar(video,valor){
           var user = firebase.auth().currentUser;
            var db=firebase.firestore();

           console.log(video.length)
             
                
                    video.shift()
                    console.log(valor) 
                    db.collection("usuarios").doc(user.photoURL)
                                    
                                    .update({
                                        
                                    mensajes: video

                                    }).then(result=>{
                                            console.log("Guardo correctamente")
                                            console.log(result)

                                    })



        },
            

    }


}

</script>
<style scoped>

.table{
    background: white;
}

</style>