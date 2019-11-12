<!--
/*
 *
 * This script is part of NethServer.
 *
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License,
 * or any later version.
 *
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see COPYING.
 */
-->

<template>
  <div>
    <h2>{{ $t('dyndns.title') }}</h2>
    <div v-if="!view.isLoaded" class="spinner spinner-lg view-spinner"></div>
    <div v-show="view.isLoaded">
      <h3 v-if="dyndns.length > 0">{{$t('dyndns.actions')}}</h3>
      <div v-if="dyndns.length > 0" class="btn-group">
        <button
          @click="openCreateDyndns()"
          class="btn btn-primary btn-lg"
        >{{$t('dyndns.create_dyndns')}}</button>
      </div>
      <h3 v-if="dyndns.length > 0">{{$t('dyndns.dyndns_list')}}</h3>
      <div v-if="dyndns.length > 0" class="row">
        <form role="form" class="search-pf has-button search col-sm-6 no-padding-left">
          <div class="form-group has-clear">
            <div class="search-pf-input-group">
              <label class="sr-only">Search</label>
              <input
                v-focus
                type="search"
                v-model="searchString"
                class="form-control input-lg"
                :placeholder="$t('dyndns.search')+'...'"
              >
            </div>
          </div>
        </form>
      </div>
      <div v-if="dyndns.length == 0" class="blank-slate-pf">
        <div class="blank-slate-pf-icon">
          <span class="pf-icon pf-icon-process-automation"></span>
        </div>
        <h1>{{$t('dyndns.jobs_not_found')}}</h1>
        <p>{{$t('dyndns.jobs_not_found_desc')}}.</p>
        <div class="blank-slate-pf-main-action">
          <button
            @click="openCreateDyndns()"
            class="btn btn-primary btn-lg"
          >{{$t('dyndns.create_job')}}</button>
        </div>
      </div>

      <div
        v-if="dyndns.length > 0"
        class="list-group list-view-pf list-view-pf-view no-mg-top mg-top-10"
      >
        <div
          v-for="(m, mk) in filteredDyndns"
          v-bind:key="mk"
          :class="['list-group-item', m.status == 'disabled' ? 'gray' : '']"
        >
          <div  class="list-view-pf-actions">
            <button
              @click="m.status == 'disabled' ? toggleStatusDyndns(m) : openEditDyndns(m)"
              :class="['btn btn-default', m.status == 'disabled' ? 'btn-primary' : '']"
            >
              <span
                :class="['fa', m.status == 'disabled' ? 'fa-check' : 'fa-pencil', 'span-right-margin']"
              ></span>
              {{m.status == 'disabled' ? $t('enable') : $t('edit')}}
            </button>
            <div class="dropup pull-right dropdown-kebab-pf">
              <button
                class="btn btn-link dropdown-toggle"
                type="button"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="true"
              >
                <span class="fa fa-ellipsis-v"></span>
              </button>
              <ul class="dropdown-menu dropdown-menu-right">
                <!-- <li>
                  <a @click="toggleStatusDyndns(m)">
                    <span
                      :class="['fa', m.status == 'enabled' ? 'fa-lock' : 'fa-check', 'span-right-margin']"
                    ></span>
                    {{m.status == 'enabled' ? $t('disable') : $t('enable')}}
                  </a>
                </li>
                <li role="presentation" class="divider"></li> -->
                <li>
                  <a @click="openDeleteDyndns(m)">
                    <span class="fa fa-times span-right-margin"></span>
                    {{$t('delete')}}
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div  class="list-view-pf-main-info small-list">
            <div class="list-view-pf-left">
              <span :class="['fa', 'list-view-pf-icon-sm', 'fa fa-user']"></span>
            </div>
            <div class="list-view-pf-body">
              <div class="list-view-pf-description">
                <div class="list-group-item-heading">{{m.name}}</div>
                <!-- <div class="list-group-item-text">{{$t('dyndns.mode')}} {{(m.Advanced === 'enabled') ? $t('dyndns.advanced'): $t('dyndns.simplified') }}</div>
                <div class="list-group-item-text">{{$t('dyndns.dyndns_Owner')}} : {{(m.Advanced === 'enabled') ? m.AdvancedUser : m.User}}</div> -->
              </div>
              <div class="list-view-pf-additional-info rules-info"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal" id="createDyndnsModal" tabindex="-1" role="dialog" data-backdrop="static">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4
              class="modal-title"
            >{{currentDyndns.isEdit ? $t('dyndns.edit_job') + ' '+ currentDyndns.name : $t('dyndns.add_job')}}</h4>
          </div>
          <form class="form-horizontal" v-on:submit.prevent="saveDyndns(currentDyndns)">
            <div class="modal-body">
              
              <div :class="['form-group', currentDyndns.errors.name.hasError ? 'has-error' : '']">
                <label
                  :class="['col-sm-3', 'control-label']"
                  for="textInput-modal-markup"
                >{{$t('dyndns.name')}}</label>
                <div :class="'col-sm-9'">
                  <input  :disabled="currentDyndns.isEdit" required type="text" v-model="currentDyndns.name" class="form-control">
                  <span
                    v-if="currentDyndns.errors.name.hasError"
                    class="help-block"
                  >{{$t('validation.validation_failed')}}: {{$t('validation.'+currentDyndns.errors.name.message)}}</span>
                </div>
              </div>
              
              <div :class="['form-group', currentDyndns.errors.Description.hasError ? 'has-error' : '']">
                <label
                  :class="['col-sm-3', 'control-label']"
                  for="textInput-modal-markup"
                >{{$t('dyndns.Description')}}</label>
                <div :class="'col-sm-9'">
                  <input   required type="text" v-model="currentDyndns.Description" class="form-control">
                  <span
                    v-if="currentDyndns.errors.Description.hasError"
                    class="help-block"
                  >{{$t('validation.validation_failed')}}: {{$t('validation.'+currentDyndns.errors.Description.message)}}</span>
                </div>
              </div>
              
              <div  :class="['form-group', currentDyndns.errors.Description.CustomService ? 'has-error' : '']">
                <label
                  :class="['col-sm-3', 'control-label']"
                  for="textInput-modal-markup"
                >{{$t('dyndns.CustomService')}}</label>
                <div :class="'col-sm-9'">
                <input  id='CustomService' type="checkbox" true-value="enabled" false-value="disabled" v-model="currentDyndns.CustomService" >
                  <span
                    v-if="currentDyndns.errors.CustomService.hasError"
                    class="help-block"
                  >{{$t('validation.validation_failed')}}: {{$t('validation.'+currentDyndns.errors.CustomService.message)}}</span>
                </div>
              </div>
              
              <div 
               v-if="currentDyndns.CustomService === 'disabled'"
               :class="['form-group', currentDyndns.errors.DynServer.hasError ? 'has-error' : '']">
               <label
                 class="col-sm-3 control-label"
                 for="textInput-modal-markup"
               >{{$t('dyndns.DynServer')}}
               </label>
               <div class="col-sm-9">
                 <select
                   required
                   type="text"
                   v-model="currentDyndns.DynServer"
                   class="combobox form-control"
                 >
                   <option value="CHANGEIP">{{$t('dyndns.CHANGEIP')}}</option>
                   <option value="DNSDYNAMIC">{{$t('dyndns.DNSDYNAMIC')}}</option>
                   <option value="DNSPARK">{{$t('dyndns.DNSPARK')}}</option>
                   <option value="DSLREPORTS">{{$t('dyndns.DSLREPORTS')}}</option>
                   <option value="DYNDNS1">{{$t('dyndns.DYNDNS1')}}</option>
                   <option value="DYNDNS2">{{$t('dyndns.DYNDNS2')}}</option>
                   <option value="DYNDNS3">{{$t('dyndns.DYNDNS3')}}</option>
                   <option value="DYNDNSFREE">{{$t('dyndns.DYNDNSFREE')}}</option>
                   <option value="DYNHOST">{{$t('dyndns.DYNHOST')}}</option>
                   <option value="DYNU">{{$t('dyndns.DYNU')}}</option>
                   <option value="EASYDNS">{{$t('dyndns.EASYDNS')}}</option>
                   <option value="EURODYNDNS">{{$t('dyndns.EURODYNDNS')}}</option>
                   <option value="FREEDNS">{{$t('dyndns.FREEDNS')}}</option>
                   <option value="HAMMER">{{$t('dyndns.HAMMER')}}</option>
                   <option value="LOOPIA">{{$t('dyndns.LOOPIA')}}</option>
                   <option value="NAMECHEAP">{{$t('dyndns.NAMECHEAP')}}</option>
                   <option value="NOIP">{{$t('dyndns.NOIP')}}</option>
                   <option value="SELFHOST">{{$t('dyndns.SELFHOST')}}</option>
                   <option value="STRATO">{{$t('dyndns.STRATO')}}</option>
                   <option value="ZONEDIT">{{$t('dyndns.ZONEDIT')}}</option>
                 </select>
                 <span v-if="currentDyndns.errors.DynServer.hasError" class="help-block">
                   {{$t('validation.validation_failed')}}:
                   {{$t('validation.'+currentDyndns.errors.DynServer.message)}}
                  </span>
                 </div>
             </div>
              
              <div v-if="currentDyndns.CustomService ==='enabled'" :class="['form-group', currentDyndns.errors.DynServer.hasError ? 'has-error' : '']">
                <label
                  :class="['col-sm-3', 'control-label']"
                  for="textInput-modal-markup"
                >{{$t('dyndns.DynServer')}}</label>
                <div :class="'col-sm-9'">
                  <input   required type="text" v-model="currentDyndns.DynServer" class="form-control">
                  <span
                    v-if="currentDyndns.errors.DynServer.hasError"
                    class="help-block"
                  >{{$t('validation.validation_failed')}}: {{$t('validation.'+currentDyndns.errors.DynServer.message)}}</span>
                </div>
              </div>
              
              <div v-if="currentDyndns.CustomService ==='enabled'":class="['form-group', currentDyndns.errors.DynDns.hasError ? 'has-error' : '']">
                <label
                  :class="['col-sm-3', 'control-label']"
                  for="textInput-modal-markup"
                >{{$t('dyndns.Dyndns_Protocol')}}</label>
                <div :class="'col-sm-9'">
                  <input   required type="text" v-model="currentDyndns.DynDns" class="form-control">
                  <span
                    v-if="currentDyndns.errors.DynDns.hasError"
                    class="help-block"
                  >{{$t('validation.validation_failed')}}: {{$t('validation.'+currentDyndns.errors.DynDns.message)}}</span>
                </div>
              </div>
              

              <div :class="['form-group', currentDyndns.errors.login.hasError ? 'has-error' : '']">
                <label
                  :class="['col-sm-3', 'control-label']"
                  for="textInput-modal-markup"
                >{{$t('dyndns.Login')}}</label>
                <div :class="'col-sm-9'">
                  <input   required type="text" v-model="currentDyndns.login" class="form-control">
                  <span
                    v-if="currentDyndns.errors.login.hasError"
                    class="help-block"
                  >{{$t('validation.validation_failed')}}: {{$t('validation.'+currentDyndns.errors.login.message)}}</span>
                </div>
              </div>

              <div :class="['form-group', currentDyndns.errors.password.hasError ? 'has-error' : '']">
                <label
                  :class="['col-sm-3', 'control-label']"
                  for="textInput-modal-markup"
                >{{$t('dyndns.password')}}</label>
                <div :class="'col-sm-6'">
                  <input  required :type="togglePass ? 'password' : 'text'"  v-model="currentDyndns.password" class="form-control">
                  <span
                    v-if="currentDyndns.errors.password.hasError"
                    class="help-block"
                  >{{$t('validation.validation_failed')}}: {{$t('validation.'+currentDyndns.errors.password.message)}}</span>
                </div>
                <div class="col-sm-2">
                  <button class="btn btn-primary" type="button" @click="togglePassHidden()">
                      <span :class="['fa', togglePass ? 'fa-eye-slash' : 'fa-eye']"></span>
                  </button>
                </div>
              </div>
              
              
              <div :class="['form-group', currentDyndns.errors.mx.hasError ? 'has-error' : '']">
                <label
                  :class="['col-sm-3', 'control-label']"
                  for="textInput-modal-markup"
                >{{$t('dyndns.mx')}}</label>
                <div :class="'col-sm-9'">
                  <input  required type="text" v-model="currentDyndns.mx" class="form-control">
                  <span
                    v-if="currentDyndns.errors.mx.hasError"
                    class="help-block"
                  >{{$t('validation.validation_failed')}}: {{$t('validation.'+currentDyndns.errors.mx.message)}}</span>
                </div>
              </div>

            <div class="modal-footer">
              <div v-if="currentDyndns.isLoading" class="spinner spinner-sm form-spinner-loader"></div>
              <button class="btn btn-default" type="button" data-dismiss="modal">{{$t('cancel')}}</button>
              <button
                class="btn btn-primary"
                type="submit"
              >{{currentDyndns.isEdit ? $t('edit') : $t('save')}}</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="modal" id="deleteDyndnsModal" tabindex="-1" role="dialog" data-backdrop="static">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">{{$t('dyndns.delete_job')}} {{toDeleteDyndns.name}}</h4>
          </div>
          <form class="form-horizontal" v-on:submit.prevent="deleteDyndns(toDeleteDyndns)">
            <div class="modal-body">
              <div class="form-group">
                <label
                  class="col-sm-3 control-label"
                  for="textInput-modal-markup"
                >{{$t('are_you_sure')}}?</label>
              </div>
            </div>
            <div class="modal-footer">
              <button class="btn btn-default" type="button" data-dismiss="modal">{{$t('cancel')}}</button>
              <button class="btn btn-danger" type="submit">{{$t('delete')}}</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// var nethserver = window.nethserver;
// var console = window.console;

export default {
  name: "Settings",
  mounted() {
    this.getDyndns();
  },
  beforeRouteLeave(to, from, next) {
    $(".modal").modal("hide");
    next();
  },
  data() {
    return {
      view: {
        isLoaded: false,
        isRoot: false,
        isAdmin: false,
        user: null
      },
      searchString: "",
      togglePass: true,
      dyndns: [],
      currentDyndns: this.initDyndns(),
      toDeleteDyndns: { 
        name: ""
      },
    };
  },
  computed: {
    filteredDyndns() {
      var returnObj = [];
      for (var r in this.dyndns) {
        var cat = JSON.stringify(this.dyndns[r]);
        if (cat.toLowerCase().includes(this.searchString.toLowerCase())) {
          returnObj.push(this.dyndns[r]);
        }
      }

      return returnObj;
    }
  },
  methods: {
    initDyndns() {
      return {
        name: "",
        CustomService:"disabled",
        Description: "",
        DynDns:"",
        DynServer:"",
        login:"",
        mx: "",
        password:"",
        errors: this.initDyndnsErrors(),
        isLoading: false,
        isEdit: false,
        togglePass: true
      };
    },
    initDyndnsErrors() {
      return {
        name: {
          hasError: false,
          message: ""
        },
        CustomService: {
          hasError: false,
          message: ""
        },
        Description: {
          hasError: false,
          message: ""
        },
        DynDns: {
          hasError: false,
          message: ""
        },
        DynServer: {
          hasError: false,
          message: ""
        },
        login: {
          hasError: false,
          message: ""
        },
        mx: {
          hasError: false,
          message: ""
        },
        password: {
          hasError: false,
          message: ""
        }
      };
    },
    togglePassHidden() {
      this.togglePass = !this.togglePass;
      this.$forceUpdate();
    },
    getDyndns() {
      var context = this;
      context.view.isLoaded = false;
      nethserver.exec(
        ["nethserver-ddclient/read"],
        {
          action: "dyndns"
        },
        null,
        function(success) {
          try {
            success = JSON.parse(success);
          } catch (e) {
            console.error(e);
          }
          context.dyndns = success.dyndns;
          context.view.isLoaded = true;
        },
        function(error) {
          console.error(error);
            context.view.isLoaded = true;
        }
      );
    },
    openCreateDyndns() {
      var context = this;
      context.currentDyndns = context.initDyndns();
      $("#createDyndnsModal").modal("show");
    },
    openEditDyndns(job) {
      this.currentDyndns = JSON.parse(JSON.stringify(job));
      this.currentDyndns.errors = this.initDyndnsErrors();

      this.currentDyndns.isEdit = true;
      this.currentDyndns.isLoading = false;
      this.togglePass = true;
      $("#createDyndnsModal").modal("show");
    },
    saveDyndns(dyndns) {
      var context = this;

      var dyndnsObj = {
        action: dyndns.isEdit ? "update" : "create",
        name: dyndns.name,
        CustomService: dyndns.CustomService,
        Description: dyndns.Description,
        DynDns:dyndns.DynDns,
        DynServer: dyndns.DynServer,
        login: dyndns.login,
        mx: dyndns.mx,
        password:dyndns.password,
      };

      context.currentDyndns.isLoading = true;
      context.$forceUpdate();
      nethserver.exec(
        ["nethserver-ddclient/validate"],
        dyndnsObj,
        null,
        function(success) {
          context.currentDyndns.isLoading = false;
          $("#createDyndnsModal").modal("hide");

          // notification
          nethserver.notifications.success = context.$i18n.t(
            "dyndns.dyndns_" +
              (context.currentDyndns.isEdit ? "updated" : "created") +
              "_ok"
          );
          nethserver.notifications.error = context.$i18n.t(
            "dyndns.dyndns_" +
              (context.currentDyndns.isEdit ? "updated" : "created") +
              "_error"
          );

          // update values
          if (dyndns.isEdit) {
            nethserver.exec(
              ["nethserver-ddclient/update"],
              dyndnsObj,
              function(stream) {
                console.info("job-edit", stream);
              },
              function(success) {
                // get all
                context.getDyndns();
              },
              function(error, data) {
                console.error(error, data);
              }
            );
          } else {
            nethserver.exec(
              ["nethserver-ddclient/create"],
              dyndnsObj,
              function(stream) {
                console.info("job-create", stream);
              },
              function(success) {
                // get all
                context.getDyndns();
              },
              function(error, data) {
                console.error(error, data);
              }
            );
          }
        },
        function(error, data) {
          var errorData = {};
          context.currentDyndns.isLoading = false;
          context.currentDyndns.errors = context.initDyndnsErrors();

          try {
            errorData = JSON.parse(data);
            for (var e in errorData.attributes) {
              var attr = errorData.attributes[e];
              context.currentDyndns.errors[attr.parameter].hasError = true;
              context.currentDyndns.errors[attr.parameter].message = attr.error;
              context.currentDyndns.errors[attr.parameter].value = attr.value;
              context.$forceUpdate();
            }
          } catch (e) {
            console.error(e);
          }
        }
      );
    },
    toggleStatusDyndns(job) {
      var context = this;
      // notification
      nethserver.notifications.success = context.$i18n.t(
        "dyndns.dyndns_updated_ok"
      );
      nethserver.notifications.error = context.$i18n.t(
        "dyndns.dyndns_updated_error"
      );

      // update values
      nethserver.exec(
        ["nethserver-ddclient/update"],
        {
          action: job.status == "enabled" ? "disable" : "enable",
          name: job.name
        },
        function(stream) {
          console.info("update-status", stream);
        },
        function(success) {
          // get all
          context.getDyndns();
        },
        function(error, data) {
          console.error(error, data);
        }
      );
    },
    openDeleteDyndns(job) {
      this.toDeleteDyndns = JSON.parse(JSON.stringify(job));
      $("#deleteDyndnsModal").modal("show");
    },
    deleteDyndns(dyndns) {
      var context = this;

      // notification
      nethserver.notifications.success = context.$i18n.t(
        "dyndns.dyndns_deleted_ok"
      );
      nethserver.notifications.error = context.$i18n.t(
        "dyndns.dyndns_deleted_error"
      );

      $("#deleteDyndnsModal").modal("hide");
      nethserver.exec(
        ["nethserver-ddclient/delete"],
        {
          name: dyndns.name
        },
        function(stream) {
          console.info("job-delete", stream);
        },
        function(success) {
          // get all
          context.getDyndns();
        },
        function(error, data) {
          console.error(error, data);
        }
      );
    }
  }
};
</script>

<style>
.list-group-item-heading {
  width: calc(50% - 20px) !important;
}
.list-group-item-text {
  width: calc(50% - 40px) !important;
}
.list-view-pf-description {
  flex: 1 0 70% !important;
}
.list-view-pf-actions {
  z-index: 2;
}
.remove-cat {
  margin-top: 6px;
  color: dimgrey;
}
.remove-cat:hover {
  cursor: pointer;
  color: #39a5dc;
}

.adjust-mg-bottom {
  margin-bottom: 4px;
}
.adjust-divider {
  margin-top: 15px;
}
.adjust-filter-cat {
  margin-top: 5px;
}

.right {
  float: right;
}

.eachCheckBox {
  margin-left: 20px;
}

.green {
  color: #3f9c35;
}
.red {
  color: #cc0000;
}
.gray {
  color: gray;
}

.no-padding-left {
  padding-left: 0px;
}
</style>
