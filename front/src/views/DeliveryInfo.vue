<template>
  <v-container>
    <div>
      <v-row>
        <v-col>
          <v-card outlined style="padding:10px" width="600" height="365">
            <v-card-title>ИНФОРМАЦИЯ О ДОСТАВКЕ</v-card-title>
            <v-divider class="mx-5"></v-divider> <br>
            <ul>
              <li>
                <p style="text-decoration: none; color: black; font-size: 20px">
                  24 часа пункт самовывоза Ткани КОЛИБРИ 78<br />
                  Маршала Захарова 25 к1, Ленинский проспект
                </p>
              </li>
              <br />
              <li>
                <p style="text-decoration: none; color: black; font-size: 20px">
                  Пункт самовывоза Ткани КОЛИБРИ 78<br />
                  Кораблестроителей 37,Приморская
                </p>
              </li>
            </ul>
          </v-card>
        </v-col>
        <v-col>
          <v-img max-width="400" src="../assets/map.png"></v-img>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "",
  data() {
    return {};
  },
  methods: {},
};
</script>
<style>
</style>
