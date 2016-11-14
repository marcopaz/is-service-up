<template>
  <div id="user-menu" class="navigation">
    <div v-if="!user.authenticated" class="hidden-xs">
      <button type="button" class="btn btn-primary" @click="login($event)"><span class="fa fa-github"></span> Login with GitHub</button>
    </div>
    <div role="navigation" class="dropdown menu" v-if="user.authenticated">
      <a href="#" class="dropdown-toggle" data-toggle="dropdown" id="user-menu-dropdown" aria-haspopup="true" aria-expanded="false">
        <img :alt="user.username" class="avatar" :src="avatar_url + '&amp;s=80'" height="40" width="40">
        <span class="dropdown-caret"></span>
      </a>

      <ul class="dropdown-menu" aria-labelledby="user-menu-dropdown">

        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">{{user.username}}</strong>
        </div>

        <li role="separator" class="divider"></li>
        <li><router-link to="/settings">Settings</router-link></li>

        <li role="separator" class="divider"></li>
        <li><a href="#" @click="logout()">Logout</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import auth from '../auth';
import * as api from '../api';
import * as config from '../config';

var DEFAULT_AVATAR_URL = 'https://avatars2.githubusercontent.com/u/0?v=3';

export default{

    data(){
        return {
            user: auth.user,
        }
    },

    methods: {
        login(event) {
            event.preventDefault();
            console.log('redirect to  ' + config.GITHUB_LOGIN_URL);
            window.location = config.GITHUB_LOGIN_URL;
            return false;
        },
        logout() {
            api.logout();
            auth.logout();
        },
    },

    computed: {
        avatar_url() {
            return this.user.avatar_url || DEFAULT_AVATAR_URL;
        }
    },

}
</script>
