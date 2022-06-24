<template>
  <v-app-bar
    app
    color="white"
    prominent
    absolute
    elevation="0"
    extension-height="100"
  >
    <header style="width: 100%">
      <header style="background: #dcdcdc; height:50px;">
        <div class="hedertop1">
          <div class="leftsity">
            <div class="text-overline">
              <a style="color: black; font-size: 10px; margin-left: 10px">
                <v-icon x-small> mdi-map-marker </v-icon>
                Санкт-Петербург
              </a>
            </div>
          </div>
          <div class="rightc">
            <div class="rightcontact1 text-overline">
              <a
                href="tel:+79955959082"
                style="text-decoration: none; color: black; font-size: 10px"
                >+7(995)595-90-82
              </a>
            </div>
            <div class="rightcontact2 text-overline">
              <a
                href="https://vk.com/tkanicolibri78"
                target="_blanc"
                style="text-decoration: none; color: black; font-size: 10px"
              >
                vk.com/tkanicolibri78
              </a>
            </div>
            <div class="rightcontact3 text-overline">
              <a
                href="mailto:tkanicolibri@gmail.com"
                style="text-decoration: none; color: black; font-size: 10px"
              >
                tkanicolibri@gmail.com
              </a>
            </div>
          </div>
        </div>
      </header>

      <div class="hedertop">
        <div class="leftmenu">
          <div class="img">
            <router-link to="/">
              <v-img
                src="../assets/colibri_supernew.png"
                max-width="80px"
                style="margin-top: 5px"
              ></v-img>
            </router-link>
          </div>
          <div class="texttkani">
            <a class="text-h5 black--text">ТКАНИ•КОЛИБРИ</a>
          </div>
        </div>

        <div class="rightmenu">
          <div class="textprivet">
            <div class="text-overline">
              <a style="text-decoration: none; color: black; font-size: 13px">
                Добро пожаловать!
              </a>
            </div>
          </div>

          <div class="btnlogin">
            <div class="text-center">
              <v-dialog v-model="loginMode" width="560">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    elevation="0"
                    color="white"
                    @click="loginButtonHandler"
                    v-bind="attrs"
                    v-on="on"
                    large
                  >
                    Войти
                  </v-btn>
                  <a
                    style="
                      text-decoration: none;
                      color: black;
                      font-size: 14px;
                      margin-left: 10px;
                    "
                    class="gift"
                  >
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on, attrs }">
                        <v-icon
                          color="error"
                          dark
                          small
                          v-bind="attrs"
                          v-on="on"
                        >
                          mdi-gift
                        </v-icon>
                      </template>
                      <span>Подарок 200 бонусов за регистрацию!</span>
                    </v-tooltip>
                  </a>
                </template>
                <v-card>
                  <div style="padding: 20px">
                    <div>
                      <v-card-title> Вход </v-card-title>
                      <div>
                        <v-text-field
                          label="Email"
                          outlined
                          v-model="input.useremail"
                          :rules="[
                            () => !!input.useremail || 'Это поле обязательно',
                          ]"
                        ></v-text-field>
                      </div>
                      <div>
                        <v-text-field
                          v-model="input.userpassword"
                          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                          :type="show1 ? 'text' : 'password'"
                          name="input-10-1"
                          label="Пароль"
                          hint="At least 8 characters"
                          counter
                          outlined
                          @click:append="show1 = !show1"
                          :rules="[
                            () =>
                              !!input.userpassword || 'Это поле обязaтельно',
                          ]"
                        ></v-text-field>
                      </div>
                    </div>
                    <div>
                      <v-row no-gutters>
                        <v-col>
                          <v-btn outlined @click="login">Войти</v-btn>
                        </v-col>
                        <v-col align-self="center">
                          <a @click="RegistrationHandler">Нет аккаунта?</a>
                        </v-col>
                      </v-row>
                    </div>
                  </div>
                </v-card>
              </v-dialog>
            </div>
          </div>

          <div class="btnlogout">
            <div class="text-center">
              <v-dialog v-model="exitApp" width="500">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn v-bind="attrs" v-on="on" elevation="0" color="white">
                    <v-icon color="black"> mdi-exit-to-app </v-icon>
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title class="text-h5 grey lighten-2">
                    выход из приложения
                  </v-card-title>
                  <div style="margin: 30px">Вы уверены, что хотите выйти?</div>

                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="grey" text @click="logout"> Да </v-btn>
                    <v-btn outlined color="black" text @click="exitApp = false">
                      Нет
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </div>
          </div>
        </div>
      </div>
    </header>

    <template #extension>
      <v-toolbar elevation="0" color="secondary" dark height="75">
        <a style="decoration: none; margin-top: 11px" class="home">
          <v-icon @click="GoMain">mdi-home</v-icon>
        </a>

        <v-container style="padding: 0px">
          <div class="tooltip">
            <div class="leftinfo">
              <div class="dop">
                <v-menu offset-x>
                  <template v-slot:activator="{ on, attrs }">
                    <div v-bind="attrs" v-on="on">
                      <p class="text-overline">
                        <a style="text-decoration: none; color: white; font-size: 13px" >
                          дополнительная информация
                        </a> 
                      </p>
                    </div>
                  </template>
                  <v-list>
                    <router-link
                      to="/DeliveryInfo"
                      style="
                        text-decoration: none;
                        color: black;
                        font-size: 14px;
                      "
                    >
                      <v-list-item>
                        <v-list-item-title> Доставка </v-list-item-title>
                      </v-list-item>
                    </router-link>
                    <router-link
                      to="/PayInfo"
                      style="
                        text-decoration: none;
                        color: black;
                        font-size: 14px;
                      "
                    >
                      <v-list-item>
                        <v-list-item-title> Оплата </v-list-item-title>
                      </v-list-item>
                    </router-link>
                    <router-link
                      to="/AboutShop"
                      style="
                        text-decoration: none;
                        color: black;
                        font-size: 14px;
                      "
                    >
                      <v-list-item>
                        <v-list-item-title> О магазине </v-list-item-title>
                      </v-list-item>
                    </router-link>
                  </v-list>
                </v-menu>
              </div>
              <div class="search">
                <v-text-field
                  @input="filters"
                  label="Поиск"
                  rounded
                  solo
                  dense
                ></v-text-field>
              </div>
            </div>

            <div class="rightinfo">
              <div class="cart">
                <router-link
                  @click="toCart"
                  :to="{ name: 'CartPage', params: { cart_data: CART } }"
                  style="text-decoration: none"
                >
                  <v-btn elevation="0" color="transparent" fab small>
                    <v-icon color="white"> mdi-cart-heart </v-icon>
                  </v-btn>
                </router-link>
              </div>
              <div class="feedback">
                <v-btn
                  rounded
                  elevation="0"
                  color="#DCDCDC"
                  outlined
                  @click="OpenFeedback"
                >
                  Оставьте отзыв
                </v-btn>
              </div>
            </div>
          </div>
        </v-container>
      </v-toolbar>
    </template>
  </v-app-bar>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";
import api from "../api";
export default {
  name: "AppBar",

  data: () => ({
    exitApp: false,
    authenticated: false,
    loginMode: false,
    caseSensitive: false,
    input: {
      useremail: "",
      userpassword: "",
    },
    show1: false,
    success_auth: {},
    cart_app: {},
  }),
  mounted() {
    this.GET_GOODS();
    this.GET_CATEGORY();
    this.GET_USERS();
    this.ADD_TO_CART();
  },
  computed: {
    ...mapGetters(["GOODS", "CART", "CATEGORYS", "USERS"]),
  },
  methods: {
    toCart() {
      window.location.reload();
    },
    filters(data) {
      this.$store.dispatch("GET_FILTER", data);
    },
    GoMain() {
      this.$router.push("/");
      window.location.reload();
    },
    ...mapActions(["GET_GOODS", "GET_CATEGORY", "GET_USERS", "ADD_TO_CART"]),
    RegistrationHandler() {
      this.$router.push("/RegistrationPage");
      this.loginMode = false;
    },
    async login() {
      let input;
      let res;
      input = {
        useremail: this.input.useremail,
        userpassword: this.input.userpassword,
      };
      res = await api.LoginUser(input);
      let res2 = await api.getUser();
      if (res2.data != res.data) {
        console.log("Успешный вход!");
        this.success_auth = res2.data;
        this.loginMode = false;
        window.location.reload();
        for (let l in this.CART.current_user_products) {
          this.cart_app = this.CART.current_user_products[l];
          console.log(this.cart_app.cartuserfirstname);
        }
      } else {
        console.log("Неправильный пароль");
        alert("Пароль или логин неверные!");
        console.log(this.success_auth);
      }
    },
    OpenFeedback() {
      this.$router.push("/FeedbackPage");
    },

    async logout() {
      console.log("Успешный выход!");
      this.success_auth = await api.logoutUser();
      console.log(this.success_auth, ">>>>>>>>>>>");
      if (!this.exitApp) this.exitApp = true;
      else this.exitApp = false;
      window.location.reload();
    },
    loginButtonHandler() {
      if (!this.loginMode) {
        this.loginMode = true;
      } else {
        this.loginMode = false;
      }
    },
  },
};
</script>
<style>


.hedertop1 {
  display: flex;
  padding-top: 10px;
}
.hedertop {
  display: flex;
  align-items: center;
}
.rightc {
  display: flex;
  margin-left: auto;
}
.leftsity {
  margin-left: 10px;
}
.rightcontact1 {
  margin-right: 20px;
}
.rightcontact2 {
  margin-right: 20px;
}
.rightcontact3 {
  margin-right: 20px;
}
.rightmenu {
  display: flex;
  margin-left: auto;
}
.leftmenu {
  display: flex;
  margin-right: auto;
  align-items: center;
}
.img {
  margin-right: 20px;
}
.texttkani {
  margin-right: 20px;
}
.textprivet {
  margin-right: 100px;
  padding-top: 7px;
}
.btnlogin {
  margin-right: 30px;
}
.btnlogout {
  margin-right: 0px;
}
.leftinfo {
  display: flex;
  margin-right: auto;
  margin-left: 10px;
}
.rightinfo {
  display: flex;
}
.cart {
  margin-top: 10px;
  margin-right: 30px;
}
.feedback {
  margin-top: 10px;
}
.dop {
  margin-top: 15px;
}
.search {
  margin-top: 10px;
  margin-left: 30px;
}
.tooltip {
  display: flex;
}
@media only screen and (max-width: 730px) {
     .leftsity {
      display:none;
  }
}
@media only screen and (max-width: 850px) {
     .texttkani {
      display:none;
  }
}
@media only screen and (max-width: 560px) {
     .rightcontact2 {
      display:none;
  }
}
@media only screen and (max-width: 560px) {
     .rightcontact3 {
      display:none;
  }
}
@media only screen and (max-width: 620px) {
     .textprivet {
      display:none;
  }
}
@media only screen and (max-width: 870px) {
     .search {
      display:none;
  }
}
@media only screen and (max-width: 610px) {
     .feedback {
      display:none;
  }
}
@media only screen and (max-width: 437px) {
     .home {
      display:none;
  }
} 
@media only screen and (max-width: 400px) {
     .gift {
      display:none;
  }
} 

</style>