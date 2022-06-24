<template>
  <v-container style="width: 600px">
    <v-card style="padding: 20px">
      <div>
        <h1>Регистрация</h1>
        <div>
          <v-text-field
            label="Введите Вашу фамилию"
            outlined
            v-model="input.surname"
            :rules="[() => !!input.surname || 'Это поле обязательно']"
          ></v-text-field>
        </div>
        <div>
          <v-text-field
            label="Введите Ваше имя"
            outlined
            v-model="input.firstName"
            :rules="[() => !!input.firstName || 'Это поле обязательно']"
          ></v-text-field>
        </div>
        <div>
          <v-text-field
            label="Введите Ваше отчество"
            outlined
            v-model="input.patronimys"
            :rules="[() => !!input.patronimys || 'Это поле обязательно']"
          ></v-text-field>
        </div>
        <div>
          <v-text-field
            label="Введите Ваш адрес"
            outlined
            v-model="input.adress"
            :rules="[() => !!input.adress || 'Это поле обязательно']"
          ></v-text-field>
        </div>
        <div>
          <v-text-field
            label="Введите Ваш Email"
            outlined
            v-model="input.email"
            :rules="[() => !!input.email || 'Это поле обязательно']"
          ></v-text-field>
        </div>
        <div>
          <v-text-field
            label="Введите Ваш номер телефона"
            outlined
            v-model="input.phone"
            :rules="[() => !!input.phone || 'Это поле обязательно']"
          ></v-text-field>
        </div>
        <div>
          <v-text-field
            v-model="input.password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Введите пароль"
            hint="At least 8 characters"
            counter
            outlined
            @click:append="show1 = !show1"
            :rules="[() => !!input.password || 'Это поле обязательно']"
          ></v-text-field>
        </div>
        <div>
          Ознакомьтесь с <router-link to="/ProccessingPolicy">политикой обработки и защиты информации</router-link>
        </div>
      </div>
      <v-btn elevation="0" outlined @click="RegistrationUser"
        >Зарегестрироваться</v-btn
      >
    </v-card>
  </v-container>
</template>

<script>
import api from "../api";
export default {
  name: "RegistrationPage",
  data() {
    return {
      input: {
        surname: "",
        firstName: "",
        patronimys: "",
        adress: "",
        email: "",
        phone: "",
        password: "",
      },
      show1: false,
    };
  },
  methods: {
    async RegistrationUser() {
      let payload;
      let res;
      payload = {
        userlastname: this.input.surname,
        username: this.input.firstName,
        userpatronimys: this.input.patronimys,
        userbaseadress: this.input.adress,
        useremail: this.input.email,
        userphone: this.input.phone,
        userpassword: this.input.password,
        userdiscountpoints: 200,
      };
      console.log(payload);
      res = await api.CreateUser(payload);
      console.log(res);
      this.$router.push("/");
    },
    login() {
      const formUser = {
        firstName: this.input.firstName,
        surname: this.input.surname,
        email: this.input.email,
        password: this.input.password,
      };
      console.log(formUser);
      this.$router.push("/CodForRegistration");
    },
  },
};
</script>
<style>
</style>
