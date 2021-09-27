<template>
   <div class="container mt-50">
       <div class="columns">
           <div class="column is-6 is-offset-3">
               <h3 class="title is-3">Crear cuenta</h3><hr/>
               <form action="#" @submit.prevent="register">

                   

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
                            <label class="label">Numero De telefono</label>
                            <div class="control">
                                <input class="input" type="text" pattern="(?=.*\d).*" placeholder="+58 4127449249" v-model="phone">
                            </div>
                        </div>
                        
                        <div class="field">
                            <label class="label">Presentacion</label>
                            <div class="control">
                                <input class="input" type="text"  placeholder="Estudiante de
Ingeniería en Computación de la UJAP con conocimientos de Java, Python," v-model="presentacion">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Contraseña</label>
                            <div class="control">
                                <input class="input" pattern="(?=.*\d).*" title="al menos un digito" type="password" v-model="pass1" >
                            </div>
                        </div>

                        <div class="field">
                            <label class="label"> Repetir Contraseña</label>
                            <div class="control">
                                <input class="input" type="password" v-model="pass2">
                            </div>
                        </div>

                        <button type=submit class="button is-primary"> Registrarme</button>
                        <br/>
                         
                        <button  @click.prevent="Registrofacebook"  class="button is-secondary"> Registrar Con facebook </button>
                        <br/>
                         
                        
                        <button   @click.prevent="RegistroGoogle"  class="button is-tertiary"> Registrar Con Google </button>
                          <br/>
                           
                        <button @click.prevent="Registrogithub" class="button is-secondary"> Registrar Con Git-Hub </button>


               </form>
                <div class="notification is-danger mt-10" v-if="error">
                    
                    {{error}}
                </div>
               

           </div>

       </div>
   </div>
</template>


<script>
import '@/firebase/init'
 
import firebase from 'firebase'

export default {
    
  
    data (){
        return{
           nombre: '',
           email: '',
           phone:'',
           pass1: '',
           pass2: '',
           presentacion:'',
           error: ''
    
        }
    },
    name: 'register',
        methods:{
            Registrogithub(){
                
                const provider = new firebase.auth.GithubAuthProvider();
                 firebase.auth()
                .signInWithPopup(provider)
                .then(result =>{
                    console.log(result)
                    console.log("github sign in")
                    this.$router.push({ name: 'dashboard'})
                    
                })
                .catch(err=>{
                    console.log(err)
                })

            },

            Registrofacebook(){
                
                const provider = new firebase.auth.FacebookAuthProvider();
                 firebase.auth()
                .signInWithPopup(provider)
                .then(result =>{
                    console.log(result)
                    console.log("facebook sign in")
                    this.$router.push({ name: 'dashboard'})
                    
                })
                .catch(err=>{
                    console.log(err)
                })

            },
            RegistroGoogle(){
                const provider = new firebase.auth.GoogleAuthProvider();
                firebase.auth()
                .signInWithPopup(provider)
                .then(result =>{
                    console.log('google sig in')
                    console.log(result)
                    this.$router.push({ name: 'dashboard'})
                })
                .catch(e =>{
                    console.log('error')
                    console.log(e)
                })
                
            },

            register(){
                if(this.nombre && this.email && this.pass1 && this.pass2 && this.phone && this.presentacion){
                   
                 if(this.pass1 ==this.pass2){
                        
                            if(this.pass1.length>=6  && this.phone.length==11){  
                            
                                    
                                            
                                            //bases de datos
                                            var db=firebase.firestore();
                                                db.collection('usuarios').add({
                                                    nombre:this.nombre,
                                                    pass: this.pass1,
                                                    cel:this.phone,
                                                    correo:this.email,
                                                    presentacion:this.presentacion,
                                                   
                                                     

                                                })
                                                .then(result=>{
                                                    console.log("Guardo correctamente",)
                                                    console.log(result.id)
                                                })
                                                .catch(err=>{
                                                    console.log("No se guardo correctamente en la bases de datos")
                                                    console.log(err)
                                                })       
                                        
                                    




                                    
                                    firebase.auth().createUserWithEmailAndPassword(this.email,this.pass1)
                                    // enviamos Formulario
                                    .then(user=>{   

                                            

                                    //actualizar el usuario
                                    if(user){
                                        user.user.updateProfile({
                                            displayName: this.nombre,
                                            photoURL: this.nombre,
                                            


                                        }).then((u)=> {
                                            


                                                //find e bases de datos
                                            this.nombre=''
                                            this.phone=''
                                            this.email= ''
                                            this.pass1= ''
                                            this.pass2= ''
                                            this.presentacion=''
                                            this.$router.push({ name: 'dashboard'})
                                            //console.log(user)
                                            console.log(u)

                                            

                                        }).cath((err)=> {
                                            this.error=err.message
                                        })
                                    }
                                    

                                }).catch(err => {
                                    this.error =err.message
                                })

                            }else{
                                this.error="constraseña debe de ser mayor a 6 digitos o numero de telefeno erroneo"
                            }

                            }else{
                                this.error='Las constraseñas son distintas'
                             }

                }else{
                    this.error='Todos los campos Son Obligatorios'

            }

                                    
        }
    }
}

</script>