
import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    goods: [],
    cart: {},
    category: [],
    country: [],
    theme: [],
    user: [],
    review: [],
    filter: '',
    news: [],
    sell:[],
  },
  getters: {
    GOODS(state) {
      return state.goods
    },
    CART(state) {
      return state.cart
    },
    CATEGORYS(state) {
      return state.category
    },
    COUNTRYS(state) {
      return state.country
    },
    THEMES(state) {
      return state.theme
    },
    USERS(state) {
      return state.user
    },
    REVIEWS(state) {
      return state.review
    },
    FILTERS(state) {
      return state.filter
    },
    NEWS(state) {
      return state.news
    },
    SELL(state) {
      return state.sell
    }
  },

  actions: {
    async GET_NEWS({ commit }) {
      let res = await api.getNews();
      let NEW = res.data;
      commit('SET_NEWS', NEW)
    },
    GET_FILTER({ commit }, data) {
      commit('SET_FILTER', data)
    },
    async GET_USERS({ commit }) {
      let res = await api.getUser();
      let USER = res.data;
      commit('SET_USERS', USER)
    },
    async GET_SELLS({ commit }) {
      let res1 = await api.getSell();
      let SELLS1 = res1.data;
      var SELLS = JSON.parse(SELLS1);
      commit('SET_SELLS', SELLS)
    },
    async GET_REVIEW({ commit }) {
      let res = await api.getReviews();
      let REVIEW = res.data;
      console.log(res);
      commit('SET_REVIEWS', REVIEW)
    },
    async GET_GOODS({ commit }) {
      let res1 = await api.getAllGoods();
      let res2 = await api.getGoodCountry();
      let res3 = await api.getGoodCategory();
      let res4 = await api.getGoodTheme();
      let GOOD = res1.data
      let COUNTRY = res2.data
      let CATEGORY = res3.data
      let THEME = res4.data
      GOOD = GOOD.map((item) => {
        let index1 = COUNTRY.findIndex((country) => {
          return country.goodcountryid === item.goodcountry;
        });
        let index2 = CATEGORY.findIndex((category) => {
          return category.goodcategoryid === item.goodcategory;
        });
        let index3 = THEME.findIndex((theme) => {
          return theme.goodthemeid === item.goodtheme;
        });
        if (index1 === -1) {
          item.goodcountry = "Россия";
        } else {
          item.goodcountry = COUNTRY[index1].goodcountryname;
        }
        if (index2 === -1) {
          item.goodcategory = "Без категории";
        } else {
          item.goodcategory = CATEGORY[index2].goodcategoryname;
        }
        if (index3 === -1) {
          item.goodtheme = {};
        } else {
          item.goodtheme = THEME[index3].goodthemename;
        }
        return item;

      });
      commit('SET_GOODS', GOOD)
    },
    async GET_CATEGORY({ commit }) {
      let resp = await api.getGoodCategory();
      let CATEGORY = resp.data;
      commit('SET_CATEGORY', CATEGORY)
    },
    async GET_COUNTRY({ commit }) {
      let resp = await api.getGoodCountry();
      let COUNTRY = resp.data;
      commit('SET_COUNTRY', COUNTRY)
    },
    async GET_THEME({ commit }) {
      let resp = await api.getGoodTheme();
      let THEME = resp.data;
      commit('SET_THEME', THEME)
    },
    async ADD_TO_CART({ commit }) {
      let res = await api.getCart();
      let CartUser = res.data
      commit('SET_CART', CartUser)
    },
    async DELETE_FROM_CART({ commit }, info) {
      let res = await api.DeleteCart(info)
      let CART_DELETE = res.data
      commit('REMOVE_FROM_CART', CART_DELETE)
    },
  },

  mutations: {
    SET_NEWS: (state, NEW) => {
      state.news = { ...NEW }
    },
    SET_SELLS: (state, SELL) => {
      state.sell = { ...SELL }
    },
    SET_FILTER: (state, data) => {
      state.filter = data
    },
    SET_REVIEWS: (state, REVIEW) => {
      state.review = { ...REVIEW }
    },
    SET_USERS: (state, USER) => {
      state.user = { ...USER }
    },
    SET_GOODS: (state, GOOD) => {
      state.goods = { ...GOOD };
    },
    SET_CATEGORY: (state, CATEGORY) => {
      state.category = { ...CATEGORY };
    },
    SET_COUNTRY: (state, COUNTRY) => {
      state.country = { ...COUNTRY };
    },
    SET_THEME: (state, THEME) => {
      state.theme = { ...THEME };
    },
    SET_CART: (state, CartUser) => {
      if (CartUser == '{"current_user_products": "none"}') {
        console.log("current_user_products-none");
      } else {
        var obj = JSON.parse(CartUser);
        state.cart = obj
      }
    }
  }
});

