<template>
   <div class="container mt-50">
       <div class="columns">
           <div class="column is-6 is-offset-3">
               <h3 class="title is-3">Iniciar Sesion</h3><hr/>
               <form action="#" @submit.prevent="login">

                   
                   

                        <div class="field">
                            <label class="label">Email</label>
                            <div class="control">
                                <input class="input" type="email" placeholder="e.g. alexsmith@gmail.com" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Contraseña</label>
                            <div class="control">
                                <input class="input" pattern="(?=.*\d).*" title="al menos un digito" type="password" v-model="pass1" >
                            </div>
                        </div>

                        

                        <button type=submit class="button is-primary"> Iniciar</button>
                        <br/>
                        <br/>
                        <button   @click.prevent="loginGoogle"  class="button is-tertiary"> Login Con Google </button>
                         
        
                        <br/>
                        <br/>
                       <button  @click.prevent="loginfacebook"  class="button is-secondary"> login Con facebook </button>
                         <br/>
                        <br/>
                        <button  @click.prevent="logingithub" class="button is-secondary"> Iniciar Con Git-Hub</button>


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
           
           email: '',
           pass1: '',
           
           error: ''
    
        }
    },
    name: 'login',
        methods:{
            logingithub(){
                
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
            loginGoogle(){
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

             loginfacebook(){
                
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
            login(){
                this.error=""
                if( this.email && this.pass1 ){
                    
                    
                        
                        if(this.pass1.length>=6 ){

                            
                            firebase.auth().signInWithEmailAndPassword(this.email,this.pass1)
                            .then(user=> {
                                this.$router.push({name:'dashboard'})
                                console.log(user)



                            }).catch(err =>{
                                this.error= err.message
                            })

                        
                        

                    }
                        

                }else{
                    this.error='Todos los campos Son Obligatorios'

            }
        }
    }
}
</script>