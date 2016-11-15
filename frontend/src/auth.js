import * as config from './config';

export default {

  user: {
    authenticated: false,
    username: null,
    avatar_url: null,
    monitored_status: null,
    slack_webhook: null,
  },

  login(code) {
    localStorage.setItem('auth_token', code);
    this.user.authenticated = true;
  },

  logout() {
    localStorage.removeItem('auth_token');
    localStorage.removeItem('user');
    this.user.authenticated = false;
    this.user.username = null;
    this.user.avatar_url = null;
  },

  restoreAuth() {
    var jwt = localStorage.getItem('auth_token');
    this.user.authenticated = !!jwt;
    if (this.user.authenticated) {
      var user = localStorage.getItem('user');
      if (user) {
        user = JSON.parse(user);
        this.user.username = user.username;
        this.user.avatar_url = user.avatar_url;
      }
    }
  },

  getAuthHeader() {
    return {
      'Authorization': 'Bearer ' + localStorage.getItem('auth_token'),
    };
  },

  setUserInfo(data) {
    $.each(data, x => {
      this.user[x] = data[x];
    });
    localStorage.setItem('user', JSON.stringify(data));
  }
}
