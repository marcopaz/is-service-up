<template>
  <div id="app" class="container">

    <div id="header">
      <div class="row">
        <div class="col-lg-12">
          <div class="logo">
            <router-link to="/">
              <img class="logo-img" src="/images/logo.png" title="isServiceUp" height="60" />
              <!--<h1>Monitor the status of your cloud services</h1>-->
            </router-link>
          </div>

          <UserMenu />
        </div>
      </div>
    </div>

    <div id="content">
      <router-view></router-view>
    </div>

    <div id="footer" class="footer">
      <a href="https://github.com/marcopaz/is-service-up">Fork me on GitHub <span class="fa fa-github"></span></a>
    </div>

  </div>
</template>

<script>
import UserMenu from './UserMenu';
import auth from './../auth';
import * as api from './../api';

export default {
  data() {
      return {
          user: auth.user,
      };
  },

  components: {
      UserMenu,
  },

  methods: {
  },

  watch: {
      'user.authenticated': {
          handler: function(value, oldValue) {
              if (!value) {
                  return;
              }
              api.getUserInfo(function(data) {
                  auth.setUserInfo(data);
              });
          },
          immediate: true,
      },
  },

  //beforeMount() {
  //  console.log('beforeMount called');
  //  this.$watch(() => auth.user, function (value, oldVal) {
  //    // do something
  //    console.log('value=', value, 'oldValue=', oldValue);
  //  });
  //}
}
</script>
