<template>
<div   class="container mt-50">
       <div class="columns">
           <div class="column is-10 is-offset-1">
           
                     
                  <h3 class="title is-3">Tabla De transacciónes</h3><hr/>
                  
                      <hr/>
                  <table class=" table is-hoverable  is-fullwidth">
                        <thead>
                            <tr>
                            
                            <th scope="col">id</th>
                            <th scope="col">transacción</th>
                            <th scope="col">ganancia obtenida</th>
                            
                            <th scope="col">Precio de cierre del Bitcoin</th>
                            <!--
                            <th scope="col">eliminar</th>
                            <th scope="col">Marcar como leido</th>
                            -->
                            </tr>
                        </thead>
                        <tbody >
                            <tr v-for="mensaje in datospaginados" :key="mensaje.id" >
                               
                                <td>{{ mensaje.id }}</td>
                                <td>{{ mensaje.telefono}}$</td>
                                <td>{{ mensaje.correo }}$</td>
                                
                                <td>{{ mensaje.nombre }}</td>
                                
                               <!--
                                <td><button class="button is-danger" @click.prevent="borrar(mensajes,mensaje.id)" >Eliminar</button></td>
                                <td><button class="button is-warning" @click.prevent="leido(mensajes,mensaje.id,mensaje.nombre,mensaje.url)">Leido</button></td>
                                -->
                            </tr>
                            
                          
                        
                        </tbody>
                    </table>
                    <nav class="pagination is-centered" role="navigation" aria-label="pagination">
 
                    <ul class="pagination-list">
                        <li v-for="pagina in totalpaginas()"  :key="pagina.id" v-on:click="getdatapagina(pagina)"><a class="pagination-link" aria-label="Goto page 1">{{pagina}}</a></li>
                        
                    </ul>
                </nav>

                <div>
                    <button @click.prevent="getResponse" class="button is-warning">{{msg}}</button>
                </div>
        
              


                  
           </div>
        </div>

</div>


</template>
<script>
import '@/firebase/init'
import firebase from 'firebase'
import axios from 'axios'
export default {
    data(){
        return{
            msg:"play",
            page:1,
           pages:1,
           error:"",
            datospaginados:[],
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
    mounted(){
        this.getdatapagina(1);
        this.mostrarPresentacion();
    },
    
    methods:{
        getResponse(){
            console.log("entro en trading")
            this.msg="trabajando"
            const path = 'http://127.0.0.1:5000/mensaje';
            axios.get(path)
            
            .then((res)=>{
                console.log(res.data())
                this.msg=res.data()
                console.log("entro en trading")
            })
            .catch((err)=>{
                console.error(err)
            })
        },

        

        getdatapagina(nopagina){
            this.datospaginados=[]
            let ini =(nopagina*5) - 5
            let fin = (nopagina * 5 )
            
            this.datospaginados= this.mensajes.slice(ini,fin)
            
        },

        totalpaginas(){
            return Math.ceil( this.pages / 5)
        },

         leerdatos(){
           
            var db=firebase.firestore();
            

             db.collection("usuarios").where("mensajes",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                   
                    
                    
                    this.total=doc.data().mensajes.length
                    console.log( this.total)
                    this.paginas = Math.ceil((this.total / this.porPagina)) // Redondea hacia arriba
                    console.log("entro aqui leerdatos")

                    
                });

            });

         



        },

            mostrarPresentacion(){

             console.log("entro aqui")
             
            //var user = firebase.auth().currentUser;
            var db=firebase.firestore();
            

             db.collection("usuarios")
             
             
             .where("cantM",'>',1)
            
             
            .onSnapshot((querySnapshot)=> {
                
                
             
                querySnapshot.forEach((doc)=> {
                    
                    
                    
                    this.mensajes=doc.data().mensajes
                    
                    this.pages=doc.data().mensajes.length
                    console.log(this.pages,"entro aquii")
                    
                   
                    
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