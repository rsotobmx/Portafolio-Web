<template>
    
    <footer >
        
        <div class="container">

         <div class="row">
             <div class="col-md-6">

                <h4> <strong>CONTACTO</strong></h4>
                <nav>
                    <ul>
                        <li class="phone">
                            <i class="fa fa-map-marker">
                            </i>
                            Av. Bolívar Centro Profesional Norte piso 3 oficina 3-2 al lado del Nautilus Jardin Gourmet, Valencia, Edo. Carabobo

                        </li>
                        <li>
                            <a href="rsotobmx@gmail.com">
                                <i class="fa fa-envelope">
                                </i>
                                Rsotobmx@gmail.com
                            </a>

                        </li>
                        <li>
                              <p class="buttons">
                                    <a href="https://github.com/cindybek" target="_blank" class="button">
                                        <span class="icon">
                                        <i class="fab fa-github"></i>
                                        </span>
                                        <span>GitHub</span>
                                    </a>

                                    <a href="https://twitter.com/Roberts82357163" target="_blank" class="button ">
                                            <span class="icon">
                                            <i class="fab fa-twitter"></i>
                                            </span>
                                            <span>Twitter</span>
                                        </a>

                                        <a href="https://www.facebook.com/robertsoto24/" target="_blank" class="button ">
                                            <span class="icon">
                                            <i class="fab fa-facebook"></i>
                                            </span>
                                            <span>Facebook</span>
                                        </a>
                                </p>

                        </li>
                    </ul>
                
                 
                       
                               


                    </nav>
                        

             </div>
             <div class="col-md-3">
                 <h4><strong>Sistema Predictivo</strong></h4>
                 <nav>
                     <ul>
                         <li>
                             <a href="">Inteligencia Artificial</a>
                         </li>
                         <li>
                             <a href="">Base de datos</a>
                         </li>
                         <li>
                             <a href="">Estrategia de trading</a>

                         </li>
                         <li>
                             <a href="">Ganancias</a>
                         </li>
                     </ul>
                 </nav>
             </div>
              
                       

         </div>   
                      

           
            <p class=" has-text-centered">
                
                {{ footerText }}
            </p>
        </div>
    </footer>
    
</template>

<script>
export default {
    data(){
        return{
            footerText:' Created By Robert Yovanni Soto Lopez & José Coronado'
        }
    }

}
</script>

<style>

footer{
    background: rgb(235, 235, 238);
}


.table{
    background-color: lightgreen;
   
}

td{
   border:hidden;
  
}


</style>