


       
<template>

    <nav  :fixed-top="true"  :transparent="true" class="navbar is-fixed-top navbar-brand is-hoverable " role="navigation" aria-label="main navigation">
        <div class="container">

                 <div  class="navbar-brand">
            <router-link class="navbar-item" to="/">
                <div class="logo">
                    <img src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/208/4822454208_e6c5094a-c93c-4020-ae86-63567f6d6254.png?cb=1615316196" width= "120px" height= "120px"  >
                    
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
            
                <a>Contacto</a>
               
            </router-link>
             <router-link class="navbar-item is-primary " to="/galeria">
            
                Portafolio
               
            </router-link>
            

        
            </div>
            
            <div class="navbar-end">
            
                               
            <div class="navbar-item">
                <template v-if="user">
                    
                    <div class="navbar-item has-dropdown is-hoverable">
                      
                            
                        
                        <a class="navbar-link">
                            
                            
                            {{ nombre  }}

                        </a>
                        

                        <div class="navbar-dropdown">
                            <router-link class="navbar-item" to="/dashboard">
                                Perfil Administrador
                            </router-link>
                           
                            <a class="navbar-item" to=/mensaje>
                                Componentes Web
                            </a>

                            <router-link class="navbar-item" to="/galeria">
                                Galería de Videos
                            </router-link>

                            <router-link class="navbar-item" to="/mensaje">
                                Mensajes    <article  class="message is-success">
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
            nombre:''
        }

    },
    mounted(){
        
            var user = firebase.auth().currentUser;
            var db=firebase.firestore();

             db.collection("usuarios").doc(user.photoURL)
             .get().then(result =>{
                 
                 this.mensajes=result.data().mensajes.length
                 console.log( this.mensajes.length ) 
                 this.nombre=result.data().nombre
                
             })

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

