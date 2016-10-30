<template>
  <div>
      <div class="services-container one-column" id="services">
        <service v-for="service in services" :service="service"></service>
      </div>
      <div class="last-update">
        Last update: <span class="last-update-seconds">{{last_update}}</span> seconds ago
      </div>
  </div>
</template>

<script>
import * as config from '../config';
import {spawnNotification} from '../utils/notifications';
import Service from './Service';

function notifyStatusChanges(oldServices, newServices) {
  $.each(oldServices, function(i, oldService) {
    var newService = newServices[i];
    if (!oldService || newService.status == oldService.status) {
      return;
    }
    notifyStatusChange(newService.name, newService.icon, newService.description)
    var options = {
      icon: icon
    };
    var msg = name + '\'s new status is "' + newStatus + '"';
    spawnNotification(msg, options);
  });
}

export default {
  name: 'services',
  components: {
    Service,
  },

  data: function() {
    return  {
      services: [],
      last_update: null,
    };
  },

  created: function _ready(){
    this.fetchServices();
    setInterval(this.fetchServices.bind(this), config.SERVICES_REFRESH_INTERVAL * 1000);
    setInterval(this.increaseLastUpdate.bind(this), 1000);
  },

  methods: {

    fetchServices: function _fetchServices(){
      var self = this;
      $.get(config.API_HOST + '/status', function(data) {
        var services = data.data.services;
        // sort services
        services = services.sort((a,b) => (a.name.toLowerCase() > b.name.toLowerCase()) ? 1 : -1);
        notifyStatusChanges(self.services, data.data.services);
        self.services = data.data.services;
        self.last_update = data.data.last_update;
      });
    },

    increaseLastUpdate: function() {
console.log('increaseLastUpdate')
      if (this.last_update === null) {
        return;
      }
      this.last_update += 1;
    },

  }
}
</script>
