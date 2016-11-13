<template>
  <div id="services">
    <div class="services-section">

      <ul class="nav nav-tabs">
        <li role="presentation" v-for="(tab, index) in tabs" :class="[isActive(index) ? 'active' : '']"><a href="#" @click="goToTab($event, index)">{{tab}}</a></li>
      </ul>

      <div class="loading" v-if="!services || services.length == 0">
        <img src="/images/loading.gif" alt="loading.." title="loading.." />
        <div>Loading service status..</div>
      </div>
      <div class="services-container one-column" v-if="services && services.length > 0">
        <service v-for="service in sortedServices" :service="service" :key="service.name"></service>
      </div>
      <div class="last-update" v-if="lastUpdate != null">
        Last update: <span class="last-update-seconds">{{lastUpdate}}</span> seconds ago
      </div>
    </div>
    <div class="legend visible-xxs">
      <ul class="legend-list">
        <li class="status-green"><span class="icon-indicator fa fa-check"></span> <span class="status-description">Operational</span></li>
        <li class="status-yellow"><span class="icon-indicator fa fa-minus-square"></span> <span class="status-description">Degraded Performance</span></li>
        <li class="status-orange"><span class="icon-indicator fa fa-exclamation-triangle"></span> <span class="status-description">Partial Outage</span></li>
        <li class="status-red"><span class="icon-indicator fa fa-times"></span> <span class="status-description">Major Outage</span></li>
        <li class="status-blue"><span class="icon-indicator fa fa-wrench"></span> <span class="status-description">Maintenance</span></li>
        <li class="status-gray"><span class="icon-indicator fa fa-question"></span> <span class="status-description">Unavailable Status</span></li>
      </ul>
    </div>
  </div>
</template>

<script>
import * as config from '../config';
import * as api from '../api';
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

export default {
  name: 'services',
  components: {
    Service,
  },

  data: function() {
    return  {
      tabs: TABS,
      activeTab: 0,
      services: [],
      lastUpdate: null,
    };
  },

  created(){
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

    goToTab(event, index) {
      event.preventDefault();
      this.activeTab = index;
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
  },

  watch: {

    activeTab() {
      this.startFetchingProcess();
    },

  },
}
</script>
