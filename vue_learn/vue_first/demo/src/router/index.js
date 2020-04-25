import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import HelloWorld from '../components/HelloWorld.vue'
import Users from '../components/user/Users.vue'
Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', name: 'Login', component: Login },
    {
      path: '/home', 
      name: 'Home', 
      component: Home, 
      redirect:'/helloword',
      children: [
        {path:'/helloword',component:HelloWorld},
        {path:'/unsatisfy',component:Users}
      ]
    }
  ]
})
