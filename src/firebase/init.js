import firebase from 'firebase'
import 'firebase/storage'
import firestore  from 'firebase/firestore'

const firebaseConfig = {
    apiKey: "AIzaSyC3mN6QjGno7UTQxOyMESsgvW9hNJqprgk",
    authDomain: "portafolio-web-87273.firebaseapp.com",
    projectId: "portafolio-web-87273",
    storageBucket: "portafolio-web-87273.appspot.com",
    messagingSenderId: "465953635489",
    appId: "1:465953635489:web:d5a5edfd0058527912c4e0",
    measurementId: "G-H5VBPYBBDH"
  };
  
 const firebaseApp= firebase.initializeApp(firebaseConfig);
 firebaseApp.firestore().settings({timestampsInSnapshots: true});
 var storage = firebase.storage();
 var fs=firebase.firestore();

 var provide = new firebase.auth.GoogleAuthProvider();

 export{
   storage,
   fs,
   firestore,
   provide
 }
 
 
 export default firebaseApp.firestore();
