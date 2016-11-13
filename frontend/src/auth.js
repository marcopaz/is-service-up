import * as config from './config';

export default {

  user: {
    authenticated: false,
    username: null,
    avatar_url: null,
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

  checkAuth() {
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
    this.user.username = data.username;
    this.user.avatar_url = data.avatar_url;
    localStorage.setItem('user', JSON.stringify(data));
  }
}
