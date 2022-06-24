<template>
  <v-container>
    <div>
      <v-card style="padding: 20px" outlined>
        <v-card-title> Как сделать заказ? </v-card-title>
        <v-card-text class="text-overline mb-4">
        <ul>
          <li>
            -Выбрать товары, которые вы хотите купить, и добавить их в корзину
          </li>
          <li>
            -Убедиться, что вы добавили все товары и выбрали нужное их
            количество
          </li>
          <li>
            -Нажать на кнопку "Оформить заказ", после чего выбрать способ
            доставки, способ оплаты из предложенных, указать адрес доставки или
            пункта самовывоза
          </li>
          <li>-Оплатить заказ в появившемся окне</li>
          <li>
            -Получить подтверждение заказа. В случае каких-либо проблем, заказ
            будет отменен, а деньги возвращены.
          </li>
          <li>
            -Получить заказ. В течение двух недель вы можете оформить возврат.
            Для этого необходимо написать менеджеру
          </li>
        </ul>
        </v-card-text>
      </v-card>
    </div>

    <div style="margin: 5px" v-for="card in GET_CART_USER" :key="card.id">
      <v-card outlined style="padding: 5px">
        <v-row>
          <v-col>
            <v-img
              max-width="270"
              max-height="160"
              style="border-radius: 7px"
              :src="`${publicPath}photo/${card.cartgoodphoto}`"
            ></v-img>
          </v-col>
          <v-col cols="3" align-self="center">
            <v-card-text class="text-overline">
            {{ card.cartgoodname }}
            </v-card-text>
          </v-col>
          <v-col align-self="center">
            <v-card-text class="text-overline mb-4">
            {{ card.cartgoodcost }} рублей
            </v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="text-overline mb-4">
            <v-btn color="white" elevation="0" @click="deleteFromCart()">
              Удалить
            </v-btn>
            </v-card-text>
          </v-col>
        </v-row>
      </v-card>
    </div>
    <v-row>
      <v-col>
        <router-link style="color: black" to="/SellPage"
          >Посмотреть статус заказа</router-link
        >
      </v-col>
      <v-col></v-col><v-col></v-col><v-col></v-col>
      <v-col>
        <v-dialog v-model="dialog" width="700">
          <template v-slot:activator="{ on, attrs }">
            <v-btn outlined elevation="0" v-bind="attrs" v-on="on">
              ОФОРМИТЬ ЗАКАЗ
            </v-btn>
          </template>
          <v-card min-height="500">
            <v-card-title class="text-h5 grey lighten-2">
              ОФОРМЛЕНИЕ ЗАКАЗА
            </v-card-title>
            <v-card-text>
              <v-card width="500" outlined style="margin: auto; padding: 10px">
                <v-container fluid>
                  <p style="color: black">Выберите пункт самовывоза:</p>
                  <v-radio-group v-model="radios" mandatory>
                    <v-radio
                      color="black"
                      value=" Маршала Захарова 25 к1"
                      label=" Маршала Захарова 25 к1"
                    ></v-radio>
                    <v-radio
                      color="black"
                      value="Кораблестроителей 37"
                      label="Кораблестроителей 37"
                    ></v-radio>
                    <v-radio
                      color="black"
                      value="Заберу по моему адресу"
                      label="Заберу по моему адресу"
                    ></v-radio>
                  </v-radio-group>
                </v-container>
                <div>
                  ОПЛАТА ПО QR КОДУ:
                  <v-img src="../assets/pay_qr.png" max-width="200"></v-img>
                </div>
              </v-card>

              <v-divider></v-divider>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn elevation="0" color="grey" text @click="dialog = false">
                отмена
              </v-btn>
              <v-btn
                elevation="0"
                outlined
                color="black"
                text
                @click="OrderHandler"
              >
                ОФОРМИТЬ ЗАКАЗ
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
    <div style="height: 200px"></div>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";
import api from '../api'
export default {
  name: "CartPage",
  data() {
    return {
      dialog: false,
      radios: null,
      cart_x: null,
      publicPath: process.env.BASE_URL,
      informationAboutUserCart: {},
      informationAboutUserCart1: {},
      radios:''
    };
  },
  props: {
    cart_data: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  computed: {
    ...mapGetters(["CART"]),
    GET_CART_USER() {
      this.informationAboutUserCart = { ...this.CART.current_user_products };
      return this.informationAboutUserCart;
    },
  },
  mounted() {
    this.ADD_TO_CART();
    this.DELETE_FROM_CART();
  },
  methods: {
    ...mapActions(["ADD_TO_CART", "DELETE_FROM_CART"]),
   async OrderHandler() {
      this.dialog = false;
      for (let cart in this.informationAboutUserCart) {
        let payload;
        let res;
        payload = {
          selluserlastname: '' ,
          selluserfirstname: '',
          sellusepatronyc:'',
          selluseradress: '',
          selluseremail: '',
          selluserphone: '',
          sellgoodphoto: this.informationAboutUserCart[cart].cartgoodphoto,
          sellgoodname: this.informationAboutUserCart[cart].cartgoodname,
          sellgoodcost: this.informationAboutUserCart[cart].cartgoodcost,
          sellgoodquantity: 1,
          selladresspoint: this.radios,
          }
          console.log(payload);
          res =await api.postSell(payload)
          console.log(res);
      }
      alert(
        "Заказ сформирован. Вам позвонит менеджер для подтверждения заказа"
      );
    },
    deleteFromCart() {
      let info = { ...this.CART.current_user_products };
      this.DELETE_FROM_CART(info);
      alert("Товар удален из корзины");
      window.location.reload();
    },
  },
};
</script>
<style>
</style>