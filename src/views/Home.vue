<template>
  <div class="home">

<!--    布局开始-->
    <Layout :style="'height:' + fullHeight + 'px;'">

<!--      导航栏-->
      <navigator></navigator>


<!--      内部容器开始-->
      <Content :style="fullHeight - '110px'">

        <!--      路由内部嵌套-->
        <router-view></router-view>

<!--        内部容器结束-->
      </Content>


<!--      页面底部开始-->
      <Footer>
        <p>
          <Icon type="md-paper-plane" /> Copyright © 2022 AthlonHD
        </p>
<!--        页面底部结束-->
      </Footer>

<!--      布局结束-->
    </Layout>



  </div>
</template>

<script>
// @ is an alias to /src
import navigator from "@/components/navigator";
import axios from 'axios';
import main from '../../config.json'

let appHost = main.main.appHost
let check_url = appHost + '/api/v2/oidc/validate_token'
let redirectUri = main.main.redirectUri

let accessToken = localStorage.getItem("accessToken")
console.log('idToken:   ' + accessToken)


export default {
  name: 'Home',
  components: {
    navigator
  },


  data: function () {
    return {

      fullHeight: document.documentElement.clientHeight

    };
  },

  watch: {
    fullHeight (val) {
      if (!this.timer) {
        this.fullHeight = val
        this.timer = true
        let _this = this
        setTimeout(function () {
          _this.timer = false
        }, 400)
      }
    }
  },

  inject: ['$authing'],
  mounted: function () {
    this.checkToken()

    this.get_bodyHeight()

  },

  methods: {

    get_bodyHeight () {
      const _this = this
      window.onresize = () => {
        return (() => {
          window.fullHeight = document.documentElement.clientHeight
              _this.fullHeight = window.fullHeight
            }

        )()
      }
    },

    // 校验token
    checkToken: function () {
      let _this = this
      if (accessToken === null) {
        _this.handleLogout()
        return
      }

      axios({
        method: 'get',
        url: check_url,
        params: {
          'access_token': accessToken
        }
      })
        .then(function (response) {
					// console.log(response);
          console.log(response.data);
          _this.response = response.data
          let code = _this.response.code
          if (code != null) {
            _this.handleLogout()

          }

				})
				.catch(function (error) {
					console.log(error);
          _this.handleLogout()
				});

    },

    handleLogout: function () {
      this.$Modal.error({title: '登录失效', content: '请点击登出后，重新登录！'})

      localStorage.clear();
      // 此处填写authing上登出回调地址
      window.location.href = this.$authing.buildLogoutUrl({redirectUri: redirectUri});
    },
  }



}
</script>
