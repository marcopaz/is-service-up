import * as config from './config';
import auth from './auth';

$.ajaxSetup({
  error: function(jqXHR, exception) {
    if (jqXHR.status == 401) {
      auth.logout();
    }
  }
});

function makeAPIRequest(path, callback) {
  var options = {
    url: config.API_HOST + path,
    type: "GET",
    beforeSend: function(xhr){
      var authHeaders = auth.getAuthHeader();
      Object.keys(authHeaders).forEach(function(k, i) {
        xhr.setRequestHeader(k, authHeaders[k]);
      });
    },
    success: callback,
  };
  $.ajax(options);
}

export function getStatus(callback) {
  makeAPIRequest('/status', callback);
}

export function getUserInfo(callback) {
  makeAPIRequest('/user', callback);
}
