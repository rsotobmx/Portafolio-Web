<template>

  <div >
   
    
     
      <Header/>
      
        <div id="wrapper">


            <section id="bloque1">

                
                <h1>Tu aliado para Cumplir tus sueños</h1>
                
        
            </section>

            <section id="bloque2">

                <p>Somos una empresa de diseño de páginas web, estamos ubicados en Valencia, Carabobo. Le ofrecemos todos los servicios necesarios para tener presencia efectiva en internet. Analizamos, le damos forma y vida a su proyecto!</p>

                <p>Que hacemos En RSL TECH, trabajamos para darle vida a sus ideas. 
                    Nuestro equipo de trabajo aportará todo su experiencia para que su proyecto sea un caso de exito</p>

              
          

            </section>


            <section id="bloque3">

                <h2>Creación profesional de páginas web con Vue.js y CSS3</h2>
                  

            </section>


            <section id="bloque4">
              
                <br>
              <br>
              <br>
              <br>
              <br>
            <article class="tile is-child notification is-warning">
                <p class="title">Características y beneficios</p>
                <p class="subtitle">de nuestras páginas web</p>
                <div class="content">
                    <p>En RSL TECH estamos mejorando cada día, con cada proyecto que desarrollamos mejoramos nuestro standard de calidad, 
                      nuestros proyectos cuentan con:</p>
                      <br>
                      <i class="fa fa-check"></i>
                        Diseño moderno
                      <i class="fa fa-check"></i>
                        Web responsive
                      <i class="fa fa-check"></i>
                        Optimizadas
                      <i class="fa fa-check"></i>
                      Facil de navegar
                </div>
            </article>
              <br>
              <br>
              <br>
              <br>
              <br>








               <article class="tile is-child notification is-danger">
               
                      <div class="subtitle">Informacion Del Administrador</div>
                      <div class="container">
                            <div class="row">
                                <div class="col-md-5">
                                  
                                  <h3> <strong> {{pNombre}}</strong></h3>
                                </div>

                                <div class="col-md-7">
                                    <div>{{Ppresentacion}}</div>
                                </div>
                          
                          </div>
                        
                        
                      </div>
                
                </article>

                <br>
                <div class="tile is-ancestor">
                  <div class="tile is-vertical is-7">
                    <div class="tile">
                      <div class="tile is-parent is-vertical ">
                        <article class="tile is-child notification is-warning ">
                          <div class="container-fluid"></div>
                          <p class="title has-text-centered">Servicios</p>
                          
                          <div class="content has-text-centered">
                            <p>Servicios Diseño gráfico, 
                              imágen corporativa, logotipos, 
                              redes sociales, hosting y dominios, 
                              redes sociales</p>
                        </div>                          
                        </article>
                      
                      </div>
                      <div class="tile is-parent  ">
                        <article class="tile is-child notification is-info">
                          
                            
                            <p class="title has-text-centered">Contacto</p>
                           
                            
                            
                            
                            <div class="content has-text-centered">
                              <p>Diseñados para adaptarse a sus necesidades, Promo Web, Web Corporativa, E-commerce, Inmobiliarias</p>
                              
                              <button id="btnModal" @click="modal()" class=" button is-primary">
                                <i class="fas fa-envelope-open-text large " >
                                  Contactanos
                                
                                <div  id="tvesModal" class="modalContainer">
                                        
                                        <div class="modal-content">
                                            <span  class="close" >×</span> 
                                            <p class="modal-card-title "> Enviar Mensaje</p>
                                              <h4>Rellene el formulario a continuación y 
                                              le contestaremos lo antes posible.</h4>

                                                 <div class="field">
                                                    <label class="label">Nombre</label>
                                                    <div class="control">
                                                        <input class="input" type="text" placeholder="e.g Alex Smith" v-model="nombre">
                                                    </div>
                                                  </div>


                                                  <div class="field">
                                                      <label class="label">Email</label>
                                                      <div class="control">
                                                          <input class="input" type="email" placeholder="e.g. alexsmith@gmail.com" v-model="correo">
                                                      </div>
                                                  </div>

                                                   <div class="field">
                                                      <label class="label">Numero De telefono</label>
                                                      <div class="control">
                                                          <input class="input" type="text" pattern="(?=.*\d).*" placeholder="+58 4127449249" v-model="telefono">
                                                      </div>
                                                  </div>

                                                     <div class="field">
                                                        <label class="label">Mensaje</label>
                                                        <div class="control">
                                                            <input class="textarea" type="text" placeholder="e.g Alex Smith" v-model="Mensaje">
                                                        </div>
                                                      </div>

                                                  

                                                 <div class="notification is-danger mt-10" v-if="error">
                    
                                                    {{error}}
                                                </div>
                                                <div class="notification is-success mt-10" v-if="enviado">
                    
                                                    {{enviado}}
                                                </div>
                                                                                
                                                  <button @click.prevent="SaveMessage"  type=submit class="button is-primary is-hoverable"> Enviar Mensaje</button>
                                                  <br/>
                                                  
                                              

                                        </div> 
                                </div>
                                </i>
                              </button>
                            </div>
                            
                         
                          
                        </article>
                        
                      </div>
                    </div>
                   
                  </div>
                  <div class="tile is-parent  ">
                    <article class="tile is-child notification box ">
                      <div class="content">
                        
                        <p class="title has-text-centered">Objetivos De RSL</p>
                        
                         <div class="content has-text-centered">
                            <p>Convertirse en una de las marcas líderes en el mercado nacional del ramo.
                              Superar el margen anual de ventas estipulado en al menos 50%.
                              Establecer un nicho de consumo internacional en un mercado incipiente.
                              Superar a la competencia en visibilidad y ventas dentro del mercado on-line del ramo nacional e internacional.
                            </p>
                          </div>
                      </div>
                    </article>
                  </div>
                </div>
                      
                      
                    
            </section>


        </div>

        <section id="portafolio">
          <div class="container">
          <br>
          <br>
          <br>
          <br>
          <h2 class="has-text-centered">Portafolio de Trabajos</h2>
          <p class="has-text-centered">
            Compruebe la cálidad en el diseño de las páginas web desarrolladas por RSL TECH
          </p>
          

          <div class="row">
       
            
              <div class="row" v-if="imagendesc!=false ">
                  <div class="" v-for="imagen in imagenes" :key="imagen">


                                <div class="col-sm-3">
                                  <div class="card">
                                    <img :src="imagen.foto" alt="" class="card-img-top">
                                    <div class="card-body">
                                      <h3 class="card-title">{{imagen.nombre}}</h3>
                                      <p class="card-text"><b>Categoria: </b>{{imagen.categoria}}.</p>
                                       <p class="card-text"><b>SubCategoria: </b>{{imagen.subcategoria}}.</p>
                                        <p class="card-text"><b>Desarrollo: </b>{{imagen.desarrollo}}.</p>
                                      <a v-bind:href="imagen.url" target="_blank" class="btn btn-primary">Reproducir</a>
                                    </div>
                                  </div>
                                </div>


                      <a class="" @click="modal2">
                      
                       <div class="modal" :class=" {'is-active': toggleModal } ">
                          <div class="modal-background"></div>
                          <div class="modal-content">
                              
                           
                           
                                
                               
                          </div>
                          <button class="modal-close is-large" @click="modal2"></button>
                      </div>
                     
                        
                    </a>
                      

                   
                      
                  </div>

              </div>
              
            </div>
            
          </div>
          
          
        </section>
        <br><br><br><br><br>

     

       



           
      <div>
        <p>Hola mundo</p>
        <br>
        <Footer/>
      </div>


     

  </div>
</template>

<script>

import footer from './footer'
import header from './header'

// @ is an alias to /src
import '@/firebase/init'
import firebase from 'firebase'
//import {storage} from '../firebase/init'
//const ref =storage.ref()

export default {
  

  data(){
    return{
      toggleModal: false,
        pNombre:'',
        Ppresentacion:'',
        showModal: false,
         imagendesc:false,
         imagenes:[],
        nombre:'',
        telefono:'',
        correo:'',
        Mensaje:'',
        error:'',
        enviado:'',
        
        mensajes:[],
            mensaje: {
                id:'',
                nombre:'',
                telefono:'',
                correo:'',
                mensaje:'',
                leido: '' 
             },


    }
  },
  
  components: {
    'Footer':footer,
    'Header':header,
    
   
  },
   mounted(){
         
          //Presentacion Y nombre del Usuario
             var db=firebase.firestore();
            var user = firebase.auth().currentUser;
            

             db.collection("usuarios").doc(user.photoURL)
             .get().then(result =>{
                 
                 this.Ppresentacion=result.data().presentacion
                  this.pNombre=result.data().nombre
                
             })

           //Carga de imagenes del portafolio
              db.collection("usuarios").where("videos",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                    
                    this.imagendesc=true
                    this.imagenes=doc.data().videos
                   
                    
                    
                    //tabla.innerHTML =' <tr> <th scope="row">'+ doc.data().array_id +'</th> <td> <br>'+ doc.data().array_nombrevideo+'</td><br> <td><br>'+ doc.data().array_categoria +'</td><br>  <td><br>'+ doc.data().array_subcategoria +'</td><br> <td><br>'+ doc.data().array_enlace +'</td><br>  </tr'
                    

                    
                });

            });

         


   },
  methods:{
   modal2(){
     
            this.toggleModal = !this.toggleModal
        
   },
      modal(){
        
       
            if(document.getElementById("btnModal")){
			var modal = document.getElementById("tvesModal");
			var btn = document.getElementById("btnModal");
            //var btn1 = document.getElementById("btnModal").value;
			var span = document.getElementsByClassName("close")[0];
			var body = document.getElementsByTagName("body")[0];
           

			btn.onclick = function() {
				modal.style.display = "block";

				body.style.position = "static";
				body.style.height = "100%";
				body.style.overflow = "hidden";
			}

			span.onclick = function() {
				modal.style.display = "none";
               
				body.style.position = "inherit";
				body.style.height = "auto";
				body.style.overflow = "visible";
			}

			window.onclick = function(event) {
				if (event.target == modal) {
					modal.style.display = "none";
                                      
					body.style.position = "inherit";
					body.style.height = "auto";
					body.style.overflow = "visible";


				}
			}
            
		}
        },

        SaveMessage(){
          if(this.nombre && this.telefono && this.correo && this.mensaje){

          
                          var user = firebase.auth().currentUser; 
                          console.log(user.photoURL)
                          var db=firebase.firestore();

                           var aux_mensaje=[]

                        
                          db.collection("usuarios").where("mensajes","!=",null)
                            .get()
                            
                            .then((querySnapshot) => {
                                
                            
                                querySnapshot.forEach((doc)=> {
                                    
                                    console.log("entroo")
                                    aux_mensaje=doc.data().mensajes
                                    console.log(aux_mensaje)


                                    

                                this.mensaje.nombre=this.nombre
                                this.mensaje.correo=this.correo
                                this.mensaje.telefono=this.telefono
                                this.mensaje.leido=false
                                this.mensaje.mensaje=this.Mensaje
                                this.mensaje.id=
                                aux_mensaje.push(this.mensaje)
                                    
                            
                            //aux_video.push(aux_video)
                            
                           
                            
                           // this.videos=aux_video

                            db.collection("usuarios").doc(user.photoURL)
                               
                            .update({
                                
                              mensajes: aux_mensaje

                            }).then(result=>{
                                    console.log("Guardo correctamente")
                                    console.log(result)
                                    
                                    this.nombre=''                                 
                                    this.Mensaje=''
                                    this.correo=''
                                    this.telefono=''
                                    this.enviado='Enviado al administrador'
                                    
                            })
                            .catch(error=>{
                                console.log("No se guardo correctamente en la bases de datos")
                                console.log(error)
                                this.error="No se guardo correctamente en la bases de datos"
                            }) 
                                    
                                })

                            })
                            .catch((error)=>{
                                console("error no se guardo",error)
                            })

                           

                          

          }else{
              this.error="todos los campos son obligatorios"
          }
        }
   
      
  }

  
  
}

</script>
<style>
#wrapper {
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.8);
    margin: 0 auto;
    max-width: 1440px;
    width: 100% !important;
}
section {
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-size: cover;
    height: 1100px;
    margin: 0 auto;
    max-width: 1440px;
    overflow: hidden;
    padding: 0;
    position: relative;
    width: 100% !important;
}
#bloque1 {
    background-image: url("https://www.ionos.es/digitalguide/fileadmin/DigitalGuide/Teaser/web-development-t.jpg");
}
#bloque2 {
    background-image: url("https://digitalisthub.com/wp-content/uploads/2018/09/disen%CC%83o-web-solomarketing.jpg");
}
#bloque3 {
    background-image: url("https://www.mediaroomsolutions.es/wp-content/uploads/2018/12/desarrollo-y-dise%C3%B1o-web_00-1024x675.jpg");
}
#bloque4 {
    background-image: url("https://www.ingeniovirtual.com/wp-content/uploads/desarrollo-de-aplicaciones-web.png");
}

h1 {
    background-color: #02223a;
    bottom: 0;
    color: rgba(255, 255, 255, 0.9);
    display: block;
    font-size: 5em;
    font-weight: bold;
    margin-top: 3em;
    opacity: 0.76;
    text-align: center;
    text-shadow: 1px 1px 1px #666;
    text-transform: uppercase;
    width: 100%;
}
h2 {
    color: black;
    background: white;
    font-size: 5em;
    font-weight: bold;
    margin-top: 0em;
    opacity: 0.85;
    text-align: center;
    text-shadow: 1px 1px 1px #ccc;
    text-transform: uppercase;
}
h3{
  font-size:2em;
}
#logo {
    display: block;
    margin: 6em auto 0;
    opacity: 0.8;
    width: 200px;
}
#bloque2 p {
    background-color: rgba(255, 255, 255, 0.8);
    color: #333;
    font-size: 1.2em;
    font-weight: normal;
    margin: 7em auto;
    max-width: 800px;
    padding: 1.5em;
}



.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}



 p:hover{
    
    -webkit-transform:scale(1.1);
    transform:scale(1.1);
 }
 .imgRedonda {
    height: 250px;
    width: 250px;
 }
 
 



</style>
