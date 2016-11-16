<template>
  <div id="settings">

    <h2 style="margin-bottom: 30px">Settings</h2>

    <!--<div class="boxed-group clearfix">-->
      <!--<h3>Web Notifications</h3>-->
      <!--<div class="boxed-group-inner">-->
        <!--<p class="checkbox">-->
          <!--<label for="webnot">-->
            <!--<input id="webnot" name="webnot" type="checkbox" value="1">-->
            <!--Enable web notifications</label>-->
        <!--</p>-->

        <!--<p class="text-center"><button type="submit" class="btn btn-primary" @click="webNotSave($event)">Save</button></p>-->
      <!--</div>-->
    <!--</div>-->

    <div class="alert alert-success fade in" v-if="alert === 'success'">
      <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
      <strong>Setting saved succesfully!</strong>
    </div>

    <div class="alert alert-danger fade in" v-if="alert === 'fail'">
      <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
      <strong>An error occurred</strong>
    </div>


    <div class="boxed-group clearfix">
      <h3>Slack Notifications</h3>
      <form class="form-horizontal">
      <div class="boxed-group-inner">
        <div class="form-group form-group-sm">
          <label class="col-sm-2 control-label" for="slackWebhook">Webhook URL</label>

          <div class="col-sm-10">
            <input v-model="user.slack_webhook" class="form-control" type="text" id="slackWebhook" placeholder="https://hooks.slack.com/services/...">
          </div>
        </div>

        <p class="text-center"><button type="submit" class="btn btn-primary" @click="save('slack_webhook', $event)">Save</button></p>
      </div>
      </form>
    </div>

    <div class="boxed-group clearfix">
      <h3>Alert Level</h3>
      <div class="boxed-group-inner">
        <p>
          Choose which status change you want to be notified of.
        </p>
        <span class="note">
          You'll be notified for status changes of a service, according
          to your preferences above,
          if both the old and the new status of
          the service are selected below.
        </span>

        <div class="checkbox" v-for='s in status'>
          <label :class="'status-' + s.color">
            <input type="checkbox" :value="s.name" v-model="user.monitored_status">
            <span :class="['icon-indicator', 'fa', s.icon]"></span> <span class="status-description">{{s.human}}</span>
          </label>
        </div>

        <p class="text-center"><button type="submit" class="btn btn-primary" @click="save('monitored_status', $event)">Save</button></p>
      </div>
    </div>
  </div>
</template>
<script>
import * as config from '../config';
import * as api from '../api';
import auth from '../auth';

var status = config.STATUS_LIST.map((x) => ({
  name: x,
  icon: config.STATUS_ICON[x],
  human: config.STATUS_DESCRIPTION[x],
  color: config.STATUS_COLOR[x],
})).reverse();

export default{
  data(){
    return {
      status,
      user: auth.user,
      alert: null,
    };
  },

  //created() {
  //  api.getUserInfo((data) => auth.setUserInfo(data));
  //},

  methods: {

    showTemporaryAlert(alert) {
      this.alert = alert;
      setTimeout(() => { this.alert = null }, 3000);
    },

    save(field, event) {
      event.preventDefault();
      var data = {};
      data[field] = this.user[field];
      api.updateUserInfo(data, () => {
        this.showTemporaryAlert('success');
      }).fail((x) => {
        this.showTemporaryAlert('fail');
      });
    },
  },

  computed: {
    checkedStatus() {
      return this.user.monitored_status;
    }
  }
}
</script>
