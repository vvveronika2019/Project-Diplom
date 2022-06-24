<template>
  <v-card width="300" height="450" outlined>
    <v-img
      max-width="300"
      max-height="160"
      :src="`${publicPath}photo/${good_data.goodphoto}`"
      alt="img"
    ></v-img>
    <v-row style="height: 100px">
      <v-card-text class="text-overline mb-4">{{ good_data.goodname }}</v-card-text>
    </v-row>
    <v-divider class="mx-5"></v-divider>
    <v-card-text>
      <div class="text-overline mb-4" style="color:black">{{ good_data.goodcost }} рублей</div>
      <v-chip-group>
        <v-chip outlined class="text-overline mb-4">
          {{ good_data.goodcountry }}
        </v-chip>
        <v-chip outlined class="text-overline mb-4">
          {{ good_data.goodcategory }}
        </v-chip>
      </v-chip-group>
    </v-card-text>
    <v-card-actions class="center">
      <v-btn rounded color="deep-purple lighten-2" text @click="AddToCart">
        добавить в корзину
      </v-btn>
      <v-btn color="deep-purple lighten-2" rounded text @click="LikeHeandler">
        <v-icon v-if="!like"> mdi-heart-outline </v-icon>
        <v-icon v-if="like"> mdi-heart </v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api from '../api'
export default {
  name: "CardProduct",
  props: {
    good_data: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data: () => ({
    AboutGoodMode: false,
    publicPath: process.env.BASE_URL,
    like: false,
  }),
  methods: {
    AboutGood() {
      if (!this.AboutGoodMode) this.AboutGoodMode = true;
      else this.AboutGoodMode = false;
    },
    LikeHeandler() {
      if (!this.like) this.like = true;
      else this.like = false;
    },
    AddToCart() {
      let payload;
      let res;
      payload = {
        cartuserlastname: '' ,
        cartuserfirstname: '',
        cartusepatronyc:'',
        cartuseradress: '',
        cartuseremail: '',
        cartuserphone: '',
        cartgoodphoto:this.good_data.goodphoto,
        cartgoodname:this.good_data.goodname,
        cartgoodcost: this.good_data.goodcost,
        cartgoodquantity: 1
        }
      res = api.postCart(payload).catch((e) => console.log(e))
      console.log(res);
      this.$emit("AddToCart", this.good_data);
    },
  },
};
</script>
