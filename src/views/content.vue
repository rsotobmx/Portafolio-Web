<template>
    <div >
        <content>
             <div class="container mt-50">
       <div class="columns">
           <div class="column is-6 is-offset-3">
               
               <h3 class="title is-3">Elegir foto de Perfil</h3><hr/>
                    <Imagen/> 
                      <br/>
               <h3 class="title is-3">Editar Usuario</h3><hr/>
             
            
               
                <form action="#" @submit.prevent="update">

                   
                   <div class="field">
                        <label class="label">Usuario</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="e.g Alex Smith" v-model="nombre">
                        </div>
                    </div>

                   

                        <div class="field">
                            <label class="label">Email</label>
                            <div class="control">
                                <input class="input" type="email" placeholder="e.g. alexsmith@gmail.com" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Contraseña actual</label>
                            <div class="control">
                                <input class="input" pattern="(?=.*\d).*" title="al menos un digito" type="password" v-model="pass1" >
                            </div>
                        </div>

                        <div class="field">
                            <label class="label"> Nueva Contraseña</label>
                            <div class="control">
                                <input class="input" pattern="(?=.*\d).*" title="al menos un digito" type="password" v-model="pass2" >
                            </div>
                        </div>

                        <button type=submit class="button is-primary"> Guardar Datos </button>

        



                </form>
                
                <div class="notification is-danger mt-10" v-if="error">
                    
                    {{error}}
                </div>

                  
                    <h3 class="title is-3">Presentacion</h3><hr/>
                     <button @click.prevent="mostrarPresentacion"  class="button is-secondary"> ver Presentacion </button>

                    <div class="notification  mt-10" v-if="print">
                    
                        {{print}}
                    </div>

                    <p>

                        

                    </p>



           </div>

       </div>
   </div>
   <br/>
                  <br/>
                   <br/>
                    <br/>
        </content>

    </div>
</template>

<script>

import '@/firebase/init'
import firebase from 'firebase'
import imagen from '../components/layout/imagen'

export default {
    components:{
        'Imagen': imagen
        
    },

    data(){
        return{
            nombre:'',
            email: '',
           
            pass1:'',
            pass2:'',
            error:'',
            print:''
            
        }
    },
    name: 'update',
    methods:{
        
       mostrarPresentacion(){
           var user = firebase.auth().currentUser;
            var db=firebase.firestore();

             db.collection("usuarios").doc(user.photoURL)
             .get().then(result =>{
                 
                 this.print=result.data().presentacion
                 

             }) 
                            
                                
                                
                            


        },

        
        update(){

            
               var user = firebase.auth().currentUser;        


            if(this.nombre && this.email && this.pass1 && this.pass2 ){

                if(user){

                    var credential = firebase.auth.EmailAuthProvider.credential(
                            user.email, 
                            this.pass1
                        
                        )

                     user.reauthenticateWithCredential(credential).then((u)=>{
                                    console.log(u)
                                    console.log("Reathentificado correctamente")
                            }).catch((err)=> {
                                this.error=err.message
                                this.error="Error en constraseña actual"
                            })
                   
                    
                        console.log(user.photoURL)
                        var db=firebase.firestore();
                            db.collection("usuarios").doc(user.photoURL)

                            .update({
                                    nombre:this.nombre,
                                    pass: this.pass2,
                            
                                    correo:this.email,

                            }).then(result=>{
                                    console.log("Guardo correctamente")
                                    console.log(result)
                                    
                            })
                            .catch(error=>{
                                console.log("No se guardo correctamente en la bases de datos")
                                console.log(error)
                                this.error="No se guardo correctamente en la bases de datos"
                            }) 


                    


                    //actualizando Usuario
                    user.updateProfile({
                        
                    displayName: this.nombre,
                  

                    }).then((u)=> {
                        this.nombre=''
                        
                        this.phone=''
                        console.log(u)
                        console.log("Cambio nombre")

                    // Update successful.
                    }).catch((err)=> {
                        this.error=err.message
                    }); 

                     //Actualizando Correo
                     
               
                    user.updateEmail(this.email).then((u)=> {
                        
                        this.email=''
                        
                        console.log(u)
                        console.log("cambio correo")
                        
                    // Update successful.
                    }).catch((err)=> {
                        this.error=err.message
                    }); 

                    //actualizamos constraseña
                    if(this.pass2.length>=6){
                        
                         credential = firebase.auth.EmailAuthProvider.credential(
                            user.email, 
                            this.pass1
                        
                        )
                            // Now you can use that to reauthenticate
                            user.reauthenticateWithCredential(credential).then((u)=>{
                                    console.log(u)
                                    user.updatePassword(this.pass2).then((us)=> {

                                        this.pass2=''
                                        this.pass1=''
                                        console.log(us)
                                        console.log("cambio constraseña")
                                // Update successful.
                                }).catch((err)=> {
                                    this.error=err.message
                                    this.error="Constraseña no actualizada"
                                }); 
                            }).catch((err)=> {
                                this.error=err.message
                                this.error="Error en constraseña actual"
                            });

                            
                        
                       
                        
                        

                    }
                    
                    
                   

      

                }
            }else{
                this.error="Todos los campos son obligatorios"
            }

        }
    }

}
</script>

<style>




</style>