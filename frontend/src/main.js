import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './components/App';
import Services from './components/Services';
import Settings from './components/Settings.vue';
import auth from './auth';

Vue.use(VueRouter);

/* eslint-disable no-new */

auth.restoreAuth();

// check if page come from server redirect
var hash = window.location.hash;
if (hash.startsWith('#/?code=')) {
  let code = hash.substr('#/?code='.length);
  auth.login(code);
  // remove code from url for safety purposes
  window.location.hash = '#/?login-success';
}

var authMiddleware = (to, from, next) => {
  if (!auth.user.authenticated) {
    next({ path:'/' });
  } else {
    next()
  }
};

var routes = [
  {path: '/', component: Services },
  {path: '/settings', component: Settings, beforeEnter: authMiddleware, },
];

export var router = new VueRouter({
  routes
});

const app = new Vue({
  el: '#app',
  router,
  render: h => h(App)
});
