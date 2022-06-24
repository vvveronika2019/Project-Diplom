<template>
  <v-container>
    <v-card width="700" style="margin: auto; padding: 20px">
      <v-row>
        <v-col>
          <v-text-field
            elevation="0"
            background-color="grey lighten-2"
            color="cyan"
            label="Ваше имя"
            required
            v-model="input.name"
          ></v-text-field>
          <v-textarea
            background-color="grey lighten-2"
            color="cyan"
            label="Напишите отзыв"
            v-model="input.value"
          ></v-textarea>
        </v-col>
      </v-row>
      <v-row>
        <v-col></v-col>
        <v-col cols="auto">
          <v-btn outlined elevation="0" @click="AddFeedback">
            Оставить отзыв
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
    <div style="margin: 20px">
      <h1 align="center">ОТЗЫВЫ</h1>
      <v-divider></v-divider>
    </div>
    <v-card
      style="margin: 10px"
      class="mx-auto"
      max-width="500"
      outlined
      v-for="feedback in REVIEWS"
      :key="feedback.id"
    >
      <v-list-item three-line>
        <v-list-item-content>
          <div class="text-overline mb-4" style="background: #d3d3d3">
            {{ feedback.reviewuser }}
          </div>
          <v-list-item-subtitle>
            {{ feedback.reviewvalue }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";
import api from "../api";

export default {
  data: () => ({
    input: {
      name: "",
      value: "",
    },
  }),
  mounted() {
    this.GET_REVIEW();
  },
  computed: {
    ...mapGetters(["REVIEWS"]),
  },
  methods: {
    ...mapActions(["GET_REVIEW"]),
    async AddFeedback() {
      let payload;
      let res;
      payload = {
        reviewuser: this.input.name,
        reviewvalue: this.input.value,
      };
      res = await api.postReviews(payload);
      alert('Спасибо за отзыв!')
    },
  },
};
</script>
