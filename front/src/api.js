import axios from 'axios'
let baseURL = 'http://127.0.0.1:8000'

const token = localStorage.getItem('token')
if (token) {
 axios.defaults.headers.common['Authorization'] = token
}
export default {
    getAllGoods() {
        return new Promise((resolve) => {
            axios.get(baseURL + '/good').then((value) => {resolve(value)})
        })
    },
    getGoodCountry() {
        return new Promise((resolve) => {
            axios.get(baseURL + '/good/country').then((value) => {resolve(value)})
        })
    },
    getGoodCategory() {
        return new Promise((resolve) => {
            axios.get(baseURL + '/good/category').then((value) => {resolve(value)})
        })
    },
    getGoodTheme() {
        return new Promise((resolve) => {
            axios.get(baseURL + '/good/theme').then((value) => {resolve(value)})
        })
    },
    getReviews() {
        return new Promise((resolve) => {
            axios.get(baseURL + '/feedback/reviewGET').then((value) => {resolve(value)})
        })
    },
    postReviews(payload){
        return new Promise((resolve) => {
            axios.post(baseURL + '/feedback/review', payload).then((value) => {resolve(value)})
        })
    },
    CreateUser(payload){
        return new Promise((resolve) => {
            axios.post(baseURL + '/user/create', payload).then((value) => {resolve(value)})
        })
    },
    LoginUser(input){
        return new Promise((resolve) => {
            axios.post(baseURL + '/user/login', input).then((value) => {resolve(value)})
        })
    },
    getUser() {
        return new Promise((resolve) => {
            axios.get(baseURL + '/user').then((value) => {resolve(value)})
        })
    },
    getNews() {
        return new Promise((resolve) => {
            axios.get(baseURL + '/news').then((value) => {resolve(value)})
        })
    },
    postCart(payload){
        return new Promise((resolve) => {
            axios.post(baseURL + '/cart/post', payload).then((value) => {resolve(value)})
        })
    },
    getCart() {
        return new Promise((resolve) => {
            axios.get(baseURL + '/cart/get').then((value) => {resolve(value)})
        })
    },
    logoutUser(){
        return new Promise((resolve) => {
            axios.get(baseURL + '/user/logout').then((value) => {resolve(value)})
        })
    },
    DeleteCart(info){
        return new Promise((resolve) => {
            axios.post(baseURL + '/cart/delete', info).then((value) => {resolve(value)}).catch((e)=> console.log("Удаление"))
        })
    },
    getSell(){
        return new Promise((resolve) => {
            axios.get(baseURL + '/sell').then((value) => {resolve(value)}).catch((e)=> console.log("Удаление"))
        })
    },
    getSellStatus(){
        return new Promise((resolve) => {
            axios.get(baseURL + '/sell/status').then((value) => {resolve(value)}).catch((e)=> console.log("Удаление"))
        })
    },
    postSell(payload){
        return new Promise((resolve) => {
            axios.post(baseURL + '/sell/post', payload).then((value) => {resolve(value)})
        })
    },
}