<template>
  <div>
    <h2>{{$t('settings.title')}}</h2>
    <div v-if="!view.isLoaded" class="spinner spinner-lg"></div>
    <div v-if="view.isLoaded">
      <h3>{{$t('settings.configuration')}}</h3>
      <form class="form-horizontal" v-on:submit.prevent="saveSettings('status')">
        <div :class="['form-group', errors.status.hasError ? 'has-error' : '']">
              <label
                class="col-sm-2 control-label"
                for="textInput-modal-markup"
              >{{$t('settings.status')}}</label>
              <div class="col-sm-5">
                <toggle-button
                  class="min-toggle"
                  :width="40"
                  :height="20"
                  :color="{checked: '#0088ce', unchecked: '#bbbbbb'}"
                  :value="configuration.status"
                  :sync="true"
                  @change="toggleStatus()"
                />
                <span
                  v-if="errors.status.hasError"
                  class="help-block"
                >{{errors.status.message}}</span>
              </div>
        </div>
        <div
          v-if="configuration.status && ! configuration.urlcheckip.match(/checkip.dyndns.org/g)"
          :class="['form-group', errors.SSL.hasError ? 'has-error' : '']"
        >
          <label
            class="col-sm-2 control-label"
            for="textInput-modal-markup"
          >{{$t('settings.SSL')}}</label>
          <div class="col-sm-5">
            <input type="checkbox"   true-value="yes" false-value="no" v-model="configuration.SSL" class="form-control">
            <span
              v-if="errors.SSL.hasError"
              class="help-block"
            >{{errors.SSL.message}}</span>
          </div>
        </div>
        <div 
          v-if="configuration.status"
          :class="['form-group', errors.DeamonUpdate.hasError ? 'has-error' : '']">
          <label
            class="col-sm-2 control-label"
            for="textInput-modal-markup"
          >{{$t('settings.DeamonUpdate')}}
          </label>
          <div class="col-sm-5">
            <select
              required
              type="text"
              v-model="configuration.DeamonUpdate"
              class="combobox form-control"
            >
              <option value="300">300 {{$t('settings.seconds')}}</option>
              <option value="600">600 {{$t('settings.seconds')}}</option>
              <option value="900">900 {{$t('settings.seconds')}}</option>
              <option value="1800">1800 {{$t('settings.seconds')}}</option>
              <option value="3600">3600 {{$t('settings.seconds')}}</option>
            </select>
            <span v-if="errors.DeamonUpdate.hasError" class="help-block">
              {{$t('validation.validation_failed')}}:
              {{$t('validation.'+errors.DeamonUpdate.message)}}
            </span>
          </div>
        </div>

        <div 
          v-if="configuration.status"
          :class="['form-group', errors.urlcheckip.hasError ? 'has-error' : '']">
          <label
            class="col-sm-2 control-label"
            for="textInput-modal-markup"
          >{{$t('settings.urlcheckip')}}
          </label>
          <div class="col-sm-5">
            <select
              required
              type="text"
              v-model="configuration.urlcheckip"
              class="combobox form-control"
            >
              <option value="checkip.dyndns.org">no ssl checkip.dyndns.org</option>
              <!-- <option value="ipdetect.dnspark.com">ipdetect.dnspark.com</option> -->
              <option value="checkip.dyndns.org:8245">no ssl checkip.dyndns.org:8245</option>
              <option value="ip.changeip.com">ip.changeip.com</option>
              <option value="checkip.dynu.com">checkip.dynu.com</option>
              <!-- <option value="myip.dnsdynamic.org">myip.dnsdynamic.org</option> -->
            </select>
            <span v-if="errors.urlcheckip.hasError" class="help-block">
              {{$t('validation.validation_failed')}}:
              {{$t('validation.'+errors.urlcheckip.message)}}
            </span>
          </div>
        </div>
        <div class="form-group">
          <label class="col-sm-2 control-label" for="textInput-modal-markup">
            <div v-if="loaders" class="spinner spinner-sm form-spinner-loader adjust-top-loader"></div>
          </label>
          <div class="col-sm-5">
            <button class="btn btn-primary" type="submit">{{$t('save')}}</button>
          </div>
        </div>
      </form>
    </div>


  </div>
</template>

<script>
export default {
  name: "Settings",
  components: {
  },
  mounted() {
    this.getSettings();
  },
  beforeRouteLeave(to, from, next) {
    $(".modal").modal("hide");
    next();
  },
  data() {
  return {
    view: {
      isLoaded: false
    },
    configuration: {
            status: true,
            urlcheckip: "checkip.dyndns.org",
            SSL: "yes",
            DeamonUpdate: "300"
    },
    loaders: false,
    errors: this.initErrors()
  };
},
methods: {
  initErrors() {
    return {
      status: {
        hasError: false,
        message: ""
      },
      urlcheckip: {
        hasError: false,
        message: ""
      },
      SSL: {
        hasError: false,
        message: ""
      },
      DeamonUpdate: {
          haserror: false,
          message:""
      }
    };
  },
  getSettings() {
    var context = this;
    context.view.isLoaded = false;
    nethserver.exec(
      ["nethserver-ddclient/read"],
      {
        action: "configuration"
      },
      null,
      function(success) {
        try {
          success = JSON.parse(success);
        } catch (e) {
          console.error(e);
        }
        context.configuration = success.configuration;
         context.configuration.status = success.configuration.status == "enabled";
        context.view.isLoaded = true;
      },
      function(error) {
        console.error(error);
          context.view.isLoaded = true;
      }
    );
  },
  toggleStatus() {
    this.configuration.status = !this.configuration.status;
  },
  saveSettings(type) {
    var context = this;
    var settingsObj = {
      action: "configuration",
      status: context.configuration.status
        ? "enabled"
        : "disabled",
        SSL: context.configuration.SSL,
        DeamonUpdate: context.configuration.DeamonUpdate,
        urlcheckip: context.configuration.urlcheckip
    };
    context.loaders = true;
    context.errors = context.initErrors();
    nethserver.exec(
      ["nethserver-ddclient/validate"],
      settingsObj,
      null,
      function(success) {
        context.loaders = false;
    
        // notification
        nethserver.notifications.success = context.$i18n.t(
          "settings.settings_updated_ok"
        );
        nethserver.notifications.error = context.$i18n.t(
          "settings.settings_updated_error"
        );
        // update values
        nethserver.exec(
          ["nethserver-ddclient/update"],
          settingsObj,
          function(stream) {
            console.info("ddclient", stream);
          },
          function(success) {
            context.getSettings();
          },
          function(error, data) {
            console.error(error, data);
          },
          true //sudo
        );
      },
      function(error, data) {
        var errorData = {};
        context.loaders = false;
        context.errors = context.initErrors();
        try {
          errorData = JSON.parse(data);
          for (var e in errorData.attributes) {
            var attr = errorData.attributes[e];
            context.errors[attr.parameter].hasError = true;
            context.errors[attr.parameter].message = attr.error;
          }
        } catch (e) {
          console.error(e);
        }
    },
      true // sudo
  );
  }
}
};
</script>

<style>
</style>
