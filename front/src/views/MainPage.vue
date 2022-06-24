<template>
  <div class="main">
    <div class="main__carousel">
      <v-row>
        <v-col class="carusel">
          <v-carousel style="max-width: 1000px; margin: 0 auto" hide-delimiters >
            <v-carousel-item
              v-for="(item, i) in items"
              :key="i"
              :src="item.src"
              reverse-transition="fade-transition"
              transition="fade-transition"
              class="carusel_item"
            >
            </v-carousel-item>
          </v-carousel>
        </v-col>
        <v-col>
          <v-card min-width="200" max-width="400" outlined class="news">
            <v-card-title style="background: #dcdcdc">
              НОВОСТИ КОЛИБРИ
            </v-card-title>
            <v-expansion-panels>
              <v-expansion-panel
                v-for="(news, index) in NewsPoint"
                :key="index" 
              >
                <v-expansion-panel-header class="text-overline">
                  {{news.newdata}} {{ news.newname }}
                </v-expansion-panel-header>
                <v-expansion-panel-content class="text-overline">
                  {{ news.newvalue }}
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-card>
        </v-col>
      </v-row>
    </div>

    <div>
      <br>
      <div class="t" style="font-size:22px" align="center">ТКАНИ </div>
      <v-divider></v-divider>

      <div class="main__cards">
        <card-product
          class="main__cards_card"
          v-for="(good, index) in filtredGoods"
          :key="index"
          :good_data="good"
          @AddToCart="AddToCart"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";
import CardProduct from "../components/CardProduct.vue";

export default {
  name: "MainPage",

  data: () => ({
    dialog: false,
    items: [
      {
        src: "http://127.0.0.1:8887/samovyvoz.png",
      },
      {
        src: "http://127.0.0.1:8887/registration_bonus_1.png",
      },
      {
        src: "http://127.0.0.1:8887/dostavka.png",
      },
      {
        src: "http://127.0.0.1:8887/otrezy.png",
      },
    ],
  }),
  components: {
    CardProduct,
  },
  mounted() {
    this.GET_GOODS();
    this.GET_CATEGORY();
    this.GET_COUNTRY();
    this.GET_THEME();
    this.GET_FILTER();
    this.GET_NEWS();
  },
  computed: {
    ...mapGetters([
      "GOODS",
      "CATEGORYS",
      "COUNTRYS",
      "THEMES",
      "FILTERS",
      "NEWS",
    ]),
    NewsPoint() {
      return this.NEWS;
    },
    filtredGoods() {
      let filter = {};
      if (this.GOODS) {
        for (let key in this.GOODS) {
          if (this.GOODS[key].goodname.indexOf(this.FILTERS) != -1) {
            filter[key] = this.GOODS[key];
          } else if (!this.FILTERS) {
            filter[key] = this.GOODS[key];
          }
        }
      }
      return filter;
    },
  },
  methods: {
    ...mapActions([
      "GET_GOODS",
      "ADD_TO_CART",
      "GET_CATEGORY",
      "GET_COUNTRY",
      "GET_THEME",
      "GET_FILTER",
      "GET_NEWS",
    ]),
    AddToCart() {
      this.ADD_TO_CART();
    },
  },
};
</script>

<style>
.main__carousel {
  align-content: center;
}
.main__cards_card {
  margin-top: 30px;
  margin: 10px;
  padding: 20px 10px;
  width: calc(33% - 24px);
  display: inline-block;
}
.main__cards {
  position: relative;
  width: 100%;
  display: block;
  margin: 0 auto;
  padding: 0;
  text-align: center;
}
.t::first-line {
  letter-spacing: 4px;
  word-spacing: 4px;
}
@media only screen and (max-width: 860px) {
     .carusel {
      display:none;
  }
}
@media only screen and (max-width: 860px) {
     .news {
      display:none;
  }
}
</style>

