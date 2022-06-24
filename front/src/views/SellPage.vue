<template>
  <v-app>
    <v-card outlined>
      <v-card-title>Информация о статусе вашего заказа</v-card-title>
      <v-card-text class="text-overline mb-4">
        <ul>
          <li>
            "В обработке" - менеджер скоро с вами свяжется и уточнит подробности
            заказа.
          </li>
          <li>"Принят" - ваш заказ находится в этапе сборки и упаковки</li>
          <li>
            "Передан в доставку" - на этом этапе наш менеджер отправит вам
            трекер для отслеживания заказа
          </li>
          <li>"Доставлен" - ваш заказ доставлен в пункт выдачи</li>
        </ul>
        Если что-то пошло не так или у вас возникли вопросы, обращайтесь к
        менеджеру.
      </v-card-text>
    </v-card>
    <br />
    <v-card
      v-for="sell in SELL.current_user_sell"
      :key="sell.id"
      outlined
      style="padding: 5px"
    >
      <v-row>
        <v-col align-self="center">
          <v-img
            style="border-radius: 7px"
            max-width="270"
            max-height="160"
            :src="`${publicPath}photo/${sell.sellgoodphoto}`"
            alt="img"
          ></v-img>
        </v-col>
        <v-col align-self="center">
          <v-card-text class="text-overline mb-4">{{
            sell.sellgoodname
          }}</v-card-text>
        </v-col>
        <v-col align-self="center">
          <v-card-text class="text-overline mb-4"
            >{{ sell.sellgoodcost }} рублей</v-card-text
          >
        </v-col>
        <v-col align-self="center">
          <v-card-text class="text-overline mb-4"
            >Количество: {{ sell.sellgoodquantity }}</v-card-text
          >
        </v-col>
        <v-col align-self="center">
          <v-card-text class="text-overline mb-4"
            >Адрес: {{ sell.selladresspoint }}</v-card-text
          >
        </v-col>
        <v-col align-self="center">
          <div v-if="sell.sellstatus_id == 1">
            <v-card-text class="text-overline mb-4"
              >Статус: В обработке</v-card-text
            >
          </div>
          <div v-if="sell.sellstatus_id == 2">
            <v-card-text class="text-overline mb-4"
              >Статус: Принят</v-card-text
            >
          </div>
          <div v-if="sell.sellstatus_id == 3">
            <v-card-text class="text-overline mb-4"
              >Статус: В доставке</v-card-text
            >
          </div>
          <div v-if="sell.sellstatus_id == 4">
            <v-card-text class="text-overline mb-4"
              >Статус: Доставлен</v-card-text
            >
          </div>
        </v-col>
      </v-row>
    </v-card>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";
export default {
  name: "SellPage",
  data: () => ({
    publicPath: process.env.BASE_URL,
  }),
  computed: {
    ...mapGetters(["SELL"]),
  },
  mounted() {
    this.GET_SELLS();
  },
  methods: {
    ...mapActions(["GET_SELLS"]),
  },
};
</script>
