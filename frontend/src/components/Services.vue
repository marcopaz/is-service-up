<template>
  <div id="services">
    <div class="services-section">

      <ul class="nav nav-tabs" v-if="user.authenticated">
        <li role="presentation" v-for="(tab, index) in tabs" :class="[isActive(index) ? 'active' : '']"><a href="#" @click="goToTab(index, $event)">{{tab}}</a></li>
      </ul>

      <div class="loading" v-if="!services">
        <img src="/images/loading.gif" alt="loading.." title="loading.." />
        <div>Loading service status..</div>
      </div>
      <div class="empty-list" v-if="services && services.length == 0">
        No services starred, select your favorite services <a href="#" @click="goToAllTab($event)">here</a>.
      </div>
      <div class="services-container one-column" v-if="services && services.length > 0">
        <service v-for="(service,index) in sortedServices" :service="service" :showStar="user.authenticated && isAllTab" :key="service.name" :class="[index == sortedServices.length-1 ? 'last-element' : '']" ></service>
      </div>
      <div class="last-update" v-if="services && services.length > 0 && lastUpdate != null">
        Last update: <span class="last-update-seconds">{{lastUpdate}}</span> seconds ago
      </div>
    </div>
    <div class="legend visible-xxs">
      <ul class="legend-list">
        <li :class="'status-' + s.color" v-for="s in status"><span :class="['icon-indicator', 'fa', s.icon]"></span> <span class="status-description">{{s.human}}</span></li>
      </ul>
    </div>
  </div>
</template>

<script>
import * as config from '../config';
import * as api from '../api';
import auth from '../auth';
import {spawnNotification} from '../utils/notifications';
import Service from './Service';

function notifyStatusChange(serviceName, serviceIcon, oldStatus, newStatus) {
  var options = {
    icon: serviceIcon
  };
  var statusDesc = config.STATUS_DESCRIPTION[newStatus];
  var msg = serviceName + '\'s new status is "' + statusDesc + '"';
  spawnNotification(msg, options);
}

var ALL_TAB_NAME = 'All';
var FAV_TAB_NAME = 'Favorite'

var TABS = [FAV_TAB_NAME, ALL_TAB_NAME];

var status = config.STATUS_LIST.map((x) => ({
  name: x,
  icon: config.STATUS_ICON[x],
  human: config.STATUS_DESCRIPTION[x],
  color: config.STATUS_COLOR[x],
})).reverse();

export default {
  name: 'services',
  components: {
    Service,
  },

  data: function() {
    return  {
      tabs: TABS,
      activeTab: 1,
      services: null,
      lastUpdate: null,
      user: auth.user,
      status,
    };
  },

  created(){
    this.startFetchingProcess();
  },

  mounted(){
    this.startFetchingProcess();
  },

  beforeDestroy() {
    this.stopFetchingProcess();
  },

  methods: {

    startFetchingProcess() {
      this.fetchServices();
      this.startIntervals();
    },

    stopFetchingProcess() {
      this.stopIntervals();
    },

    startIntervals() {
      if (this._intervals) {
        this.stopIntervals();
      }
      this._intervals = [];
      this._intervals.push(setInterval(this.fetchServices.bind(this), config.SERVICES_REFRESH_INTERVAL * 1000));
      this._intervals.push(setInterval(this.increaseLastUpdate.bind(this), 1000));
    },

    stopIntervals() {
      if (!this._intervals) {
        return;
      }
      this._intervals.forEach(function(elm) {
        clearInterval(elm);
      });
      this._intervals = null;
    },

    fetchServices(){
      var self = this;
      api.getStatus(self.activeTabName, function(data) {
        var services = data.data.services;
        var prevServicesMap = {};
        $.each(self.services, function(i, service) {
          prevServicesMap[service.name] = service;
        });
        $.each(services, function(i, service) {
          if (prevServicesMap
              && prevServicesMap[service.name]
              && service.status != prevServicesMap[service.name].status) {
            var prevStatus = prevServicesMap[service.name].status;
            notifyStatusChange(service.name, service.icon_url, prevStatus, service.status);
          }
        });

        self.services = services;
        self.lastUpdate = 0;
      });
    },

    increaseLastUpdate() {
      if (this.lastUpdate === null) {
        return;
      }
      this.lastUpdate += 1;
    },

    isActive(index) {
      return index == this.activeTab;
    },

    goToTab(index, event) {
      if (event) {
        event.preventDefault();
      }
      this.activeTab = index;
      this.services = null;
      this.startFetchingProcess();
    },

    goToAllTab(event) {
      event.preventDefault();
      var idx = TABS.indexOf(ALL_TAB_NAME);
      this.goToTab(idx)
    },

  },

  computed: {
    sortedServices() {
      var clone = this.services.slice(0);
      clone.sort((a,b) => (a.name.toLowerCase() > b.name.toLowerCase()) ? 1 : -1);
      return clone;
    },

    activeTabName() {
      return this.tabs[this.activeTab];
    },

    isAllTab() {
      return this.activeTabName === ALL_TAB_NAME;
    }
  },

  watch: {

    'user.authenticated': {
      handler: function(value) {
        this.activeTab = value ? 0 : 1;
      },
      immediate: true,
    },

  },
}
</script>
