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

    <div class="boxed-group clearfix">
      <h3>Slack Notifications</h3>
      <form class="form-horizontal">
      <div class="boxed-group-inner">
        <div class="form-group form-group-sm">
          <label class="col-sm-2 control-label" for="slackWebhook">Webhook URL</label>

          <div class="col-sm-10">

            <div class="input-group">
              <span class="input-group-addon">https://hooks.slack.com/services/</span>
              <input type="text" class="form-control" id="slackWebhook" aria-describedby="inputGroupSuccess1Status">
            </div>

            <!--<input class="form-control" type="text" id="slackWebhook" placeholder="Slack Webhook URL">-->
          </div>
        </div>

        <p class="text-center"><button type="submit" class="btn btn-primary" @click="webNotSave($event)">Save</button></p>
      </div>
      </form>
    </div>

    <div class="boxed-group clearfix">
      <h3>Alert Level</h3>
      <div class="boxed-group-inner">
        <p>
          Choose which status change you want to be notified of
        </p>
        <div class="checkbox">
          <label class="status-red">
            <input type="checkbox" value="critical" v-model="checkedStatus">
            <span class="icon-indicator fa fa-times"></span> <span class="status-description">Major Outage</span>
          </label>
        </div>
        <div class="checkbox">
          <label class="status-orange">
            <input type="checkbox" value="major" v-model="checkedStatus">
            <span class="icon-indicator fa fa-exclamation-triangle"></span> <span class="status-description">Partial Outage</span>
          </label>
        </div>
        <div class="checkbox">
          <label class="status-yellow">
            <input type="checkbox" value="minor" v-model="checkedStatus">
            <span class="icon-indicator fa fa-minus-square"></span> <span class="status-description">Degraded Performance</span>
          </label>
        </div>
        <div class="checkbox">
          <label class="status-green">
            <input type="checkbox" value="ok" v-model="checkedStatus">
            <span class="icon-indicator fa fa-check"></span> <span class="status-description">Operational</span>
          </label>
        </div>
        <div class="checkbox">
          <label class="status-blue">
            <input type="checkbox" value="maintenance" v-model="checkedStatus">
            <span class="icon-indicator fa fa-wrench"></span> <span class="status-description">Maintenance</span>
          </label>
        </div>
        <div class="checkbox">
          <label class="status-gray">
            <input type="checkbox" value="unavailable" v-model="checkedStatus">
            <span class="icon-indicator fa fa-question"></span> <span class="status-description">Unavailable Status</span>
          </label>
        </div>

        <p class="text-center"><button type="submit" class="btn btn-primary">Save</button></p>
      </div>
    </div>
  </div>
</template>
<script>

var DEFAULT_CHECKED_STATUS = ['ok', 'major', 'critical'];

export default{
  data(){
    return{
      checkedStatus: DEFAULT_CHECKED_STATUS,
    }
  },

  watch: {
    checkedStatus(val) {
      console.log('checkedStatus=', val);
    }
  },

  methods: {
    webNotSave() {

    },
  }
}
</script>
