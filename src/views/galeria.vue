<template>
<div   class="container mt-50">
       <div class="columns">
           <div class="column is-6 is-offset-3">
               <h3 class="title is-3">Registro De Videos</h3><hr/>
               <form action="#"  >

                  
                   <div  class="field">
                        <label class="label">Nombre del Video</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="Video de artes" id="nombre" v-model="nombre">
                        </div>
                        </div>


                        <div class=categoria @click.prevent="selection" >
                            <div  class="field">
                                <label for="areas" class="label">Categoria</label>
                                <div class="control">
                                    <div class="select">
                                        
                                        <select id="areas" v-model="category">
                                            
                                            <option value="0">Seleccione una categoria</option>
                                        </select>
                                        <br>
                                    </div>
                                
                                
                                </div>

                            </div>
                           
                           


                            <div class="field" >
                                <label for="areas" class="label">Subcategoria </label>
                                <div class="control ">
                                    <div class="select">

                                    

                                        
                                        <select id="categorias" v-model="subcategory">
                                            <option value="0">Seleccione Una Subcategoria</option>
                                        </select>
                                        

                                        

                                    
                                
                                    </div>   
                                </div>
                            </div>
                            
                            

                            <div class="field" >
                                <label for="areas" class="label">Plataforma de Desarrollo </label>
                                <div class="control ">
                                    <div class="select">

                                        
                                        <select id="subCategorias"  v-model="desarrollo">
                                            <option value="0" >selecccione Una Plataforma de Desarrollo</option>
                                        </select>
                                        

                                    </div>
                                </div>
                            
                            </div>

                        </div>     
                             
                             
                             <br>
                        
                            <label class="label">Foto de Captura</label>
                            <div class="control">
                                <input class="input is-primary" @change="uploadimage($event)" type="file"  accept="image/*">
                            </div>
                        



                        <div class="field">
                            <label class="label">Enlace</label>
                            <div class="control">
                                <input class="input"  title="Ingrese un enlace de youtube" type="text" id="url" v-model="enlace" >
                            </div>
                        </div>

                        

                        <button type=submit @click.prevent="guardar"  class="button is-primary"> Guardar</button>
                        <br/>
                        <br/>
                        <button type=submit  id="boton"  class="button is-secondary"> </button>
                        <br/>
                         
                       


               </form>
                <div class="notification is-danger mt-10" v-if="error">
                    
                    {{error}}
                </div>
                
                
                
               

               
                <h3 class="title is-3">Videos Registrados</h3><hr/>
                  

  
                  
                    
                    <table class="table is-hoverable  is-fullwidth">
                        <thead>
                            <tr>
                            
                            <th scope="col">Nombre</th>
                            <th scope="col">Categoria</th>
                            <th scope="col">Subcategoria</th>
                            <th scope="col">Enlace</th>
                            
                            <th scope="col">eliminar</th>
                            <th scope="col">editar</th>
                            </tr>
                        </thead>
                        <tbody >
                            <tr v-for="video in videos" :key="video.id" >
                               
                                <td>{{ video.nombre }}</td>
                                <td>{{ video.categoria}}</td>
                                <td>{{ video.subcategoria }}</td>
                                <td><button  @click="modal()" id="btnModal" >{{video.url}}</button></td>
                                <div id="tvesModal" class="modalContainer">
                                        <div class="modal-content">
                                            <span  class="close">×</span> <h3>Modal</h3>
                                            <iframe width="560" height="315" src="https://www.youtube.com/embed/z83gU1lV_mI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                                        </div> 
                                </div>
                                
                                <td><button class="button is-danger" @click.prevent="borrar(videos,video.id)" >Eliminar</button></td>
                                <td><button class="button is-warning" @click.prevent="editar(videos,video.id,video.nombre,video.url)">editar</button></td>
                                
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
import {storage} from '../firebase/init'
const ref =storage.ref()



 var bandera=true
 


  var areas = [
            {id:1,name:"Web"},
            {id:2,name:"Aplicacion de Escritorio"},
            {id:3,name:"Movil"}
            ]

            var categorias = [
            {id:1,name:"Juegos",idArea:1},
            {id:2,name:"Gadget",idArea:1},
            
            {id:3,name:"Blog",idArea:2},
            {id:4,name:"CRM",idArea:2},
            
            {id:5,name:"ECommerce",idArea:3},
            {id:6,name:"Bigcoins",idArea:3},
            
            ]

            var subCategorias = [
            {id:1,name:"JavaScript",idCategoria:1},
            {id:2,name:"Vue",idCategoria:1},
            {id:3,name:"React",idCategoria:1},

            {id:4,name:"JavaScript",idCategoria:2},
            {id:5,name:"Vue",idCategoria:2},
            {id:6,name:"React",idCategoria:2},

            {id:7,name:"Java",idCategoria:3},
            {id:8,name:"Python",idCategoria:3},
            {id:9,name:"C++",idCategoria:3},

            {id:10,name:"Java",idCategoria:4},
            {id:11,name:"Python",idCategoria:4},
            {id:12,name:"C++",idCategoria:4},

            {id:13,name:"IOS",idCategoria:5},
            {id:14,name:"Android",idCategoria:5},
            {id:15,name:"Java",idCategoria:5},

            {id:16,name:"IOS",idCategoria:6},
            {id:17,name:"Android",idCategoria:6},
            {id:18,name:"Java",idCategoria:6},
            ]
 
//import firebase from 'firebase'
export default {
     
  

    components:{
        
    },


    data (){
        return{
            showModal:false,
            videos:[],
            video: {
                id:'',
                nombre:'',
                categoria:'',
                subcategoria:'',
                desarrollo:'',
                url: '' ,
                foto:null
             },

           nombre: '',
           category: '',
           subcategory:'',
           desarrollo: '',
           enlace: '',
            printn:[],

           error: '',
          
           
    
        }
    },
    mounted(){
        this.mostrarPresentacion()
    },
    methods:{
        uploadimage(e){
            

            let file= e.target.files[0];
           var storageref= ref.child('portafolio/' + file.name);
            let uploadtask= storageref.put(file);

            uploadtask.on('state_changed', ()=>{
                
                
                }, (error) =>{
                    console.log(error)
                }, () =>{
                
                uploadtask.snapshot.ref.getDownloadURL().then((downloadURL) =>{
                    this.video.foto=downloadURL;
                    console.log('File available at', downloadURL);
                 });
                });

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

        editar(array,pos,name,enla){

            var user = firebase.auth().currentUser;
            var db=firebase.firestore();
            console.log(array[pos-1])
            var aux=array
            this.nombre=name
           
            
            this.enlace=enla
             var boton = document.getElementById('boton')
             boton.innerHTML="Editar"         

             boton.onclick=function(){
                 

                
               var nam= document.getElementById('nombre').value
                var url = document.getElementById('url').value
                var cat= document.getElementById('areas').value
                var sub= document.getElementById('categorias').value

                var datos= ' '
                      
                        
                         for(let step  =0; step< 3 ;step++){
                            if(cat==areas.[step].id){

                                
                                
                                datos= areas.[step].name
                                }
                        }

                        var datos2=" "
                        for(let step  =0; step< 6 ;step++){
                            if(sub==categorias.[step].id){

                                
                                
                                datos2= categorias.[step].name
                                }
                        }

                
                

                    console.log("entro aqui")
                    console.log(url,"areaaas",cat)

                    aux[pos-1].nombre=nam
                    aux[pos-1].categoria=datos
                    aux[pos-1].subcategoria=datos2
                    
                    aux[pos-1].url=url

                    console.log(aux)
                    db.collection("usuarios").doc(user.photoURL)


                    
                    .update({
                        videos: aux
                        
                    })
                    .then(() => {
                        console.log("se guardo correctamente");
                                    document.getElementById('nombre').value=''
                                     document.getElementById('url').value=''
                                    document.getElementById('areas').value=''
                                   document.getElementById('categorias').value=''
                                   document.getElementById('subCategorias').value=''
                                  

                    })
                    .catch((error) => {
                        // The document probably doesn't exist.
                        console.error("Error : ", error);
                    });

                   


             }
                        
                       
           
            
            

            
        },
        borrar(video,valor){
           var user = firebase.auth().currentUser;
            var db=firebase.firestore();

           console.log(video.length)
             
                
                    video.shift()
                    console.log(valor) 
                    db.collection("usuarios").doc(user.photoURL)
                                    
                                    .update({
                                        
                                    videos: video

                                    }).then(result=>{
                                            console.log("Guardo correctamente")
                                            console.log(result)

                                    })



        },
            mostrarPresentacion(){
            //var user = firebase.auth().currentUser;
            var db=firebase.firestore();
            

             db.collection("usuarios").where("videos",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                    
                    
                    this.videos=doc.data().videos
                    console.log(this.videos)
                    
                    
                    //tabla.innerHTML =' <tr> <th scope="row">'+ doc.data().array_id +'</th> <td> <br>'+ doc.data().array_nombrevideo+'</td><br> <td><br>'+ doc.data().array_categoria +'</td><br>  <td><br>'+ doc.data().array_subcategoria +'</td><br> <td><br>'+ doc.data().array_enlace +'</td><br>  </tr'
                    

                    
                });

            });
                


            },
        guardar(){
            if(this.nombre && this.category && this.subcategory && this.desarrollo && this.enlace)
            {
                    var datos= ' '
                      
                        
                         for(let step  =0; step< 3 ;step++){
                            if(this.category==areas.[step].id){

                                
                                
                                datos= areas.[step].name
                                }
                        }

                        var datos2=" "
                        for(let step  =0; step< 6 ;step++){
                            if(this.subcategory==categorias.[step].id){

                                
                                
                                datos2= categorias.[step].name
                                }
                        }

                         var datos3=" "
                        for(let step  =0; step< 18 ;step++){
                            if(this.desarrollo==subCategorias.[step].id){

                                
                                
                                datos3= subCategorias.[step].name
                                }
                        }

                        
                      
                        //var band=false
                       // var aux_video1,aux_video2,aux_video3,aux_video4=[]

                        var user = firebase.auth().currentUser; 
                          console.log(user.photoURL)
                          var db=firebase.firestore();

                           var aux_video=[]

                        
                          db.collection("usuarios").where("videos","!=",null)
                            .get()
                            
                            .then((querySnapshot) => {
                                
                            
                                querySnapshot.forEach((doc)=> {
                                    
                                    console.log("entroo")
                                    aux_video=doc.data().videos
                                    console.log(aux_video)


                                    

                                this.video.nombre=this.nombre
                                this.video.categoria=datos
                                this.video.subcategoria=datos2
                                this.video.desarrollo=datos3
                                this.video.url=this.enlace
                                this.video.id=
                                aux_video.push(this.video)
                                    
                            
                            //aux_video.push(aux_video)
                            
                           
                            
                           // this.videos=aux_video

                            db.collection("usuarios").doc("ldMsmEagn2qDQLhoMX8q")
                               
                            .update({
                                
                              videos: aux_video

                            }).then(result=>{
                                    console.log("Guardo correctamente")
                                    console.log(result)
                                    
                                    this.nombre=''                                 
                                    this.category=''
                                    this.subcategory=''
                                    this.desarrollo=''
                                    this.enlace=''
                                    
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
                            }),

                            console.log(aux_video)
                            console.log(datos)

                            console.log(datos2)
                             console.log(datos3)

            }
            else{
                this.error="todos los campos son obligatorios"
            }
                        


        },

    
        selection(){
           
 
            
            

            
           
            
            if(bandera){
           
                //creando los options de area
                var areasSelect = document.getElementById('areas');
                var categoriasSelect = document.getElementById('categorias');
                var subCategoriasSelect = document.getElementById('subCategorias');
                
                
                
                
              
                
                areasSelect.addEventListener("change", cargarCategorias);
                categoriasSelect.addEventListener("change", cargarSubCategorias); 
                
               

                areas.forEach(function(area){
                    let opcion = document.createElement('option')
                    opcion.value = area.id
                    opcion.text = area.name
                    
                    
                    areasSelect.add(opcion)
                    
                })

                console.log("entro")
                bandera=false
            }   

            function cargarCategorias(){
            categoriasSelect.options.length = 1;
            subCategoriasSelect.options.length = 1;
            categorias
            .filter(function (categoria){
                return categoria.idArea == this;
            }, areasSelect.value)
            .forEach(function(categoria){
                let opcion = document.createElement('option')
                opcion.value = categoria.id
                opcion.text = categoria.name
               
                categoriasSelect.add(opcion);
                
            });
            }

            function cargarSubCategorias(){
                subCategoriasSelect.options.length = 1;
                subCategorias
                .filter(function (subCategoria){
                    return subCategoria.idCategoria == this;
                }, categoriasSelect.value)
                .forEach(function(subCategoria){
                    let opcion = document.createElement('option')
                    opcion.value = subCategoria.id
                    opcion.text = subCategoria.name
                    
                    subCategoriasSelect.add(opcion);
                    
                });
            
            }
           


                
            

            
        
        }

    
    
    
    }

}
</script>

<style>
.modalContainer {
			display: none; 
			position: fixed; 
			z-index: 1;
			padding-top: 100px;
			left: 0;
			top: 0;
			width: 100%;
			height: 100%; 
			overflow: auto; 
			background-color: rgb(0,0,0);
			background-color: rgba(0,0,0,0.4);
		}
.modalContainer .modal-content {
			background-color: #fefefe;
			margin: auto;
			padding: 20px;
			border: 1px solid lightgray;
			border-top: 10px solid #58abb7;
			width: 60%;
}

.modalContainer .close {
			color: #aaaaaa;
			float: right;
			font-size: 28px;
			font-weight: bold;
}

.modalContainer .close:hover,
.modalContainer .close:focus {
			color: #000;
			text-decoration: none;
			cursor: pointer;
}
.table{
    background: white;
}
 
 


</style>