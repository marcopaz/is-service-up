<template>
  <div class="service-row">
    <div class="service-star" v-if="showStar" @click="toggleServiceStar()">
      <span :class="['fa', service.star ? 'fa-star' : 'fa-star-o']"></span>
    </div>
    <div class="service-container" :class="'status-' + color" @click="goToStatusPage()">
      <img class="service-icon" :src="service.icon_url" :title="service.name"/>
      <span class="service-name">{{service.name}}</span>
      <span class="icon-indicator fa" :class="icon"></span>
      <span class="service-status hidden-xxs"><a :href="service.status_url">{{description}}</a></span>
    </div>
  </div>
</template>

<script>
import * as config from '../config';
import * as api from '../api';

export default {
  name: 'service',
  props: {
    service: {
      required: true,
      twoWay: true,
    },
    showStar: Boolean,
  },
  data: function() {
    return {
    };
  },
  methods: {
    goToStatusPage() {
      window.location = this.service.status_url;
      return false;
    },
    toggleServiceStar() {
      this.service.star = !this.service.star;
      api.updateFavoriteStatus(this.service.star, this.service.id);
    },
  },
  computed: {
    color() {
      return config.STATUS_COLOR[this.service.status];
    },
    icon() {
      return config.STATUS_ICON[this.service.status];
    },
    description() {
      return config.STATUS_DESCRIPTION[this.service.status];
    },
  },
};
</script>
