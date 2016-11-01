<template>
  <div class="service-row">
    <div class="service-container border-color" v-on:click="goToStatusPage">
      <div class="service-inner-container" :class="'status-' + color">
        <img class="service-icon" :src="service.icon_url" :title="service.name"/>
        <span class="service-name">{{service.name}}</span>
        <span class="icon-indicator fa" :class="icon"></span>
        <span class="service-status hidden-xxs"><a :href="service.status_url">{{description}}</a></span>
      </div>
    </div>
  </div>
</template>

<script>
import * as config from '../config';

export default {
  name: 'service',
  props: ['service'],
  data: function() {
    return {
    };
  },
  methods: {
    goToStatusPage: function() {
      window.location = this.service.status_url;
      return false;
    },
  },
  computed: {
    color: function() {
      return config.STATUS_COLOR[this.service.status];
    },
    icon: function() {
      return config.STATUS_ICON[this.service.status];
    },
    description: function() {
      return config.STATUS_DESCRIPTION[this.service.status];
    },
  }
};
</script>
