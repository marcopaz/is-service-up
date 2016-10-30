import Vue from 'vue';
import Services from './components/Services';
import {requestNotificationPermission} from './utils/notifications';

/* eslint-disable no-new */

requestNotificationPermission();

new Vue({
  el: '#services',
  template: '<Services/>',
  components: { Services },
});
