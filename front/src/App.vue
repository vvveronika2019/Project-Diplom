<template>
  <v-app id="app">
    <app-bar />
    
    <v-main>
      <v-container fluid class="back">
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer dark padless>
      <v-card
        flat
        tile
        color="secondary"
        dark
        class="lighten-1 white--text text-center"
      >
        <v-card-text class="text-center">
          <v-btn
            class="mx-4 white--text"
            color="transparent"
            elevation="0"
            onclick="window.location.href = 'https://vk.com/tkanicolibri78';"
          >
            <v-img src="./assets/vk.png"></v-img>
          </v-btn>
        </v-card-text>

        <v-card-text class="white--text pt-0">
          <v-row>
            <v-col>
              <v-card
                outlined
                width="479"
                flat
                tile
                color="secondary"
                dark
                class="lighten-1 white--text"
              >
                <div class="text-center">
                  <b>КОМПАНИЯ КОЛИБРИ</b>
                </div>
                <ul>
                  <br />
                  <li>
                    <router-link
                      style="text-decoration: none; color: white"
                      to="/"
                    >
                      Новости
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      style="text-decoration: none; color: white"
                      to="/FeedbackPage"
                    >
                      Оставить отзыв
                    </router-link>
                  </li>
                </ul>
              </v-card>
            </v-col>
            <v-col>
              <v-card
                outlined
                width="480"
                flat
                tile
                color="secondary"
                dark
                class="lighten-1 white--text"
              >
                <div class="text-center">
                  <b>ИНТЕРНЕТ-МАГАЗИН</b>
                </div>
                <ul>
                  <br />
                  <li>
                    <router-link
                      style="text-decoration: none; color: white"
                      to="/CartPage"
                      >Как сделать заказ?</router-link
                    >
                  </li>
                  <li>
                    <router-link
                      style="text-decoration: none; color: white"
                      to="/PayInfo"
                    >
                      Информация об оплате
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      style="text-decoration: none; color: white"
                      to="/DeliveryInfo"
                    >
                      Информация о доставке
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      style="text-decoration: none; color: white"
                      to="/AboutShop"
                    >
                      Информация о магазине
                    </router-link>
                  </li>
                </ul>
              </v-card>
            </v-col>
            <v-col>
              <v-card
                outlined
                width="479"
                flat
                tile
                color="secondary"
                dark
                class="lighten-1 white--text"
              >
                <div class="text-center">
                  <b>ОБРАТНАЯ СВЯЗЬ</b>
                </div>
                <ul>
                  <br />
                  <li>
                    <a
                      href="mailto:tkanicolibri@gmail.com"
                      style="
                        text-decoration: none;
                        color: white;
                        font-size: 14px;
                      "
                    >
                      tkanicolibri@gmail.com
                    </a>
                  </li>
                  <li>
                    <a
                      href="tel:+79955959082"
                      style="
                        text-decoration: none;
                        color: white;
                        font-size: 14px;
                      "
                    >
                      <v-icon small> mdi-phone</v-icon>
                      +7(995)595-90-82
                    </a>
                  </li>
                  <li>
                    <a
                      href="https://vk.com/tkanicolibri78"
                      target="_blanc"
                      style="
                        text-decoration: none;
                        color: white;
                        font-size: 14px;
                      "
                    >
                      vk.com/tkanicolibri78
                    </a>
                  </li>
                </ul>
              </v-card>
            </v-col>
          </v-row>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>©КОЛИБРИ</strong>
          <v-row>
            <v-col>
              <p align="left" style="font-size: 13px">
                Разработчики: Максим Крисько, Филиппова Вероника
              </p>
            </v-col>
            <v-col>
              <router-link to="/ProccessingPolicy" style="color: white; font-size: 13px">
                Политика обработки данных
              </router-link>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
import AppBar from "./components/AppBar.vue";
export default {
  name: "App",

  components: { AppBar },
};
</script>

<style>
.back {
  background-color: white;
}
#app {
  margin: 0px;
  padding: 0px;
}
p {
  color: white;
  font-size: 18px;
}
li {
  list-style-type: none;
}
</style>