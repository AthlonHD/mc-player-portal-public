import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/iview.js'
import { AuthenticationClient } from 'authing-js-sdk';
import main from '../config.json'


// console.log(main)
let appId = main.main.appId
let appHost = main.main.appHost
let redirectUri = main.main.redirectUri + 'callback'
// console.log(appId)
// console.log(appHost)
// console.log(redirectUri)


const authing = new AuthenticationClient({
    // 此处填写authing上的APPID
	appId: appId,
    // 此处填写authing上的认证地址
	appHost: appHost,
    // 此处填写authing上的登录回调地址
	redirectUri: redirectUri,
	tokenEndPointAuthMethod: 'none'
});

Vue.config.productionTip = false

new Vue({
  router,
  provide: {
    $authing: authing
  },

  render: h => h(App)
}).$mount('#app')
