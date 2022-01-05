


       
<template>

    <nav  :fixed-top="true"  :transparent="true" class="navbar is-fixed-top navbar-brand is-hoverable " role="navigation" aria-label="main navigation">
        <div class="container">

                 <div  class="navbar-brand">
            <router-link class="navbar-item" to="/">
                <div class="logo">
                    <img src="https://s2.coinmarketcap.com/static/img/coins/200x200/1.png"   >
                    
                </div>

                
            </router-link>

            <a role="button" class="navbar-burger" :class="{'is-active': isOpen}" @click.prevent="toggleMenu" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            </a>
        </div>

        <div  id="navbarBasicExample " class="navbar-menu bar " :class="{'is-active': isOpen}">
            <div class="navbar-start">
            <router-link class="navbar-item is-primary" to="/" >
            
                Inicio
               
            </router-link>
            <router-link class="navbar-item is-primary" to="/mensaje">
            
                <a>Transacciones</a>
               
            </router-link>
            
            <template v-if="user">
                 <template v-if="user.displayName === 'admin'">
                    <router-link class="navbar-item is-primary " to="/contact">
                    
                        Bandeja
                    
                    </router-link>
                 </template>
            </template >
            

        
            </div>
            
            <div class="navbar-end">
            
                               
            <div class="navbar-item">
                <template v-if="user">
                    
                    <div class="navbar-item has-dropdown is-hoverable">
                      
                            
                        
                        <a class="navbar-link">
                            
                            
                            {{ user.displayName  }}

                        </a>
                        

                        <div class="navbar-dropdown">
                            <router-link class="navbar-item" to="/dashboard">
                                Editar Usuario
                            </router-link>

                           <!--
                            <a class="navbar-item" to=/mensaje>
                                Componentes Web
                            </a>
                            -->

                            <template v-if="user.displayName === 'admin'">
                                <router-link class="navbar-item" to="/contact">
                                    bandeja de mensajes<article  class="message is-success">
                                                    <div class="message-header">
                                                        <p>{{videos}}</p>
                                                    </div>
                                                </article>
                                </router-link>
                            </template>
                            
                            <router-link class="navbar-item" to="/mensaje">
                                Transacciones    <article  class="message is-success">
                                                <div class="message-header">
                                                    <p>{{mensajes}}</p>
                                                </div>
                                            </article>
                            </router-link>
                            
                        </div>
                    </div>
                    <div class="buttons">
                        <a class="button is-primary" @click.prevent="logout">
                            <strong>Salir</strong>
                        </a>
                    </div>
                    
                     
                    
                </template>
                <template v-else>
                    <div class="buttons">
                        <router-link class="button is-primary" to="/register">
                            <strong>Registrarme</strong>
                        </router-link>
                        <router-link class="button is-light" to="/login">
                            Iniciar Sesion
                        </router-link>
                    </div>

                </template>

                
            </div>
        </div>
        </div>


        </div>
       

        
        
    </nav>
    

    


</template>


<script>
import firebase from 'firebase'


export default {
    
    
    data(){
        return{
            isOpen: false,
            user: null,
            showNavbar:true,
            lastscrollpos:0,
            mensajes:'',
            videos:'',
            nombre:''
        }

    },
    mounted(){

                var db=firebase.firestore();
            

             db.collection("usuarios").where("mensajes",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                   
                    
                    
                   this.mensajes=doc.data().mensajes.length
                    
                    console.log( this.mensajes)
                    this.nombre=doc.data().nombre
                    

                    
                });

            });
            db.collection("usuarios").where("videos",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                   
                    
                    
                   this.videos=doc.data().videos.length
                    
                    console.log( this.videos)
                    this.nombre=doc.data().nombre
                    

                    
                });

            });


           

            
        

                    let scrollpos = window.scrollY
                    const header = document.querySelector("nav")
                    const header_height = header.offsetHeight

                    const add_class_on_scroll = () => header.classList.add("isActive")
                    const remove_class_on_scroll = () => header.classList.remove("isActive")

                    window.addEventListener('scroll', function() { 
                    scrollpos = window.scrollY;

                    if (scrollpos >= header_height) { 
                        add_class_on_scroll();
                        console.log(add_class_on_scroll);
                    }
                    else { 
                        remove_class_on_scroll(); 
                        console.log(remove_class_on_scroll);
                    }

                    })

    },
   

    methods: {
        
        toggleMenu () {
            const status =! this.isOpen
            this.isOpen= status

           



        },
        logout(){
            firebase.auth().signOut().then(()=> {
                this.$router.push({name: 'login'})
            })
        },
        
    },
    created(){
        firebase.auth().onAuthStateChanged(user=> {
            if(user){
                this.user =user

                   

                    
            }else{
                this.user=null

                   
              
            }
        })

    },
    

    
}
</script>
<style scoped>

nav.navbar.is-fixed-top {
  transition: background-color 0.5s ease;
  background: transparent;
}

nav.navbar.is-fixed-top.isActive{
  transition: background-color 0.9s ease;
  background: white;
  transform: translateY(-15%);
}

img:hover{
    
    -webkit-transform:scale(1.3);
    transform:scale(1.3);
}

.navbar-item:hover
{
     -webkit-transform:scale(1.1);
     transform:scale(1.1);
}
.message-header{
  height:0.1px; 
  width:auto;
}

</style>

