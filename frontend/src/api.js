import * as config from './config';
import auth from './auth';

$.ajaxSetup({
  error: function(jqXHR, exception) {
    if (jqXHR.status == 401) {
      auth.logout();
    }
  }
});

function makeAPIRequest(path, options, callback) {
  var defaultOptions = {
    url: config.API_HOST + path,
    type: "GET",
    beforeSend: function(xhr){
      var authHeaders = auth.getAuthHeader();
      Object.keys(authHeaders).forEach(function(k, i) {
        xhr.setRequestHeader(k, authHeaders[k]);
      });
    },
    // data: JSON.stringify({ ... }),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: callback,
  };

  var ajaxOptions = $.extend({}, defaultOptions, options);
  $.ajax(ajaxOptions);
}

export function getStatus(type, callback) {
  var options = {
    data: {
      type: type.toLowerCase(),
    },
  };
  makeAPIRequest('/status', options, callback);
}

export function getUserInfo(callback) {
  makeAPIRequest('/user', {}, callback);
}

export function logout(callback) {
  makeAPIRequest('/user/logout', {}, callback);
}

export function updateFavoriteStatus(status, service_id, callback) {
  var options = {
    type: 'POST',
    data: JSON.stringify({
      status: status,
      service_id: service_id,
    }),
  };
  makeAPIRequest('/user/favorite', options, callback);
}
