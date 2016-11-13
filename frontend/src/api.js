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

  if (!callback) {
    if (options) {
      callback = options;
      options = {};
    } else {
      callback = function(){};
    }
  }

  var defaultOptions = {
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

  var ajaxOptions = {};
  $.extend(ajaxOptions, defaultOptions, options);
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
  makeAPIRequest('/user', callback);
}

export function logout(callback) {
  makeAPIRequest('/user/logout', callback);
}
