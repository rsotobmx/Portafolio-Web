import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import login from '../views/auth/login.vue'
import register from '../views/auth/register.vue'
import dashboard from '../views/dashboard.vue'
import mensaje from '../views/mensaje.vue'
import galeria from '../views/galeria.vue'
import firebase from 'firebase'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },  
 
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/register',
    name: 'register',
    component: register
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: dashboard,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/mensaje',
    name: 'mensaje',
    component: mensaje,
    
    meta:{
      requiresAuth: true
    }

  },
  {
    path: '/galeria',
    name: 'galeria',
    component: galeria,
    
    meta:{
      requiresAuth: true
    }

  }
  
]

const router = new VueRouter({
  routes
});

router.beforeEach((to,from,next)=> {
  if(to.matched.some(ruta => ruta.meta.requiresAuth)){
    const user= firebase.auth().currentUser;
    if(user){
      next();
    }else{
      next({
        name: 'login'
      })
    }

  }else{
    next();
  }
})

export default router
