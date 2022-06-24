import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '../views/MainPage.vue'

import AboutShop from '../views/AboutShop'
import DeliveryInfo from '../views/DeliveryInfo'
import PayInfo from '../views/PayInfo'
import CartPage from '../views/CartPage' 
import FeedbackPage from '../views/FeedbackPage'
import RegistrationPage from '../views/RegistrationPage'
import ProccessingPolicy from '../views/ProccessingPolicy' 
import SellPage from '../views/SellPage' 
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage,
    props:true
  },
  {
    path: '/AboutShop',
    name: 'AboutShop',
    component: AboutShop,
    props:true
  },
  {
    path: '/DeliveryInfo',
    name: 'DeliveryInfo',
    component: DeliveryInfo,
    props:true
  },
  {
    path: '/PayInfo',
    name: 'PayInfo',
    component: PayInfo,
    props:true
  },
  {
    path: '/CartPage',
    name: 'CartPage',
    component: CartPage,
    props:true
  },
  {
    path: '/FeedbackPage',
    name: 'FeedbackPage',
    component: FeedbackPage,
    props:true
  }, 
  {
    path: '/RegistrationPage',
    name: 'RegistrationPage',
    component: RegistrationPage,
    props:true
  },
  {
    path:'/ProccessingPolicy',
    name: 'ProccessingPolicy',
    component: ProccessingPolicy,
    props: true
  },
  {
    path: '/SellPage',
    name: 'SellPage',
    component: SellPage,
    props:true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
