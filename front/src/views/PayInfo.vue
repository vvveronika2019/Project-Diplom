<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card style="padding: 20px" outlined>
          <v-card-title>
            <p style="font-size: 20px; color: black">ИНФОРМАЦИЯ ОБ ОПЛАТЕ</p>
          </v-card-title>
          <v-divider class="mx-5"></v-divider> <br>
          <p style="font-size: 24px; color: black">
            Мы принимаем оплату только переводом на расчетный счет предприятия в
            "Тинькофф Банке", который будет вам автоматически предложен на
            сайте.
            <br /><br />
            Это гарантирует безопасность вашего платежа, так как он юридически
            является оплатой товара. Соответственно, вы сможете вернуть деньги в
            случае отмены/возврата заказа. <br /><br />
            <v-icon color="error" large>mdi-alert</v-icon>
            Остерегайтесь мошенников и переводите деньги только на указанные
            реквизиты.
          </p>
        </v-card>
      </v-col>
      <v-col>
        <v-img src="../assets/tinkoff.png" max-width="530"></v-img>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "",
  methods: {},
};
</script>

<style>

</style>
