<template>
  <content>

    <div>

      <h2 style="text-align: left; margin-left: 40px; margin-top: 30px">请点击系统以进入：</h2>

      <Row>

<!--        <router-link to="/home/mcsm" tag="div">-->
<!--          <Card style="width:320px; margin: 25px;">-->
<!--            <div style="text-align:center">-->
<!--              <Icon type="ios-cog" size="45"/>-->
<!--              <h3>实例管理面板</h3>-->
<!--            </div>-->
<!--          </Card>-->
<!--        </router-link>-->

        <Card style="width:320px; margin: 25px 25px 25px 75px;">
          <div style="text-align:center" @click="openMcsm">
            <Icon type="ios-cog" size="45"/>
            <h3>实例管理面板</h3>
          </div>
        </Card>

        <Card style="width:320px; margin: 25px;">
          <div style="text-align:center" @click="openConsole">
            <Icon type="md-code" size="45" />
            <h3 >网页指令面板</h3>
          </div>
        </Card>

      </Row>


    </div>

  </content>
</template>

<script>
import main from '../../config.json'
import axios from "axios";


let mcsm_url = main.mcsm_url

export default {
  name: "admin-info",

  data () {
    return {
      userInfo: '',
    }
  },

  inject: ['$authing'],
  mounted: function () {
    this.userInfo = localStorage.getItem('userInfo');
    console.log(this.userInfo)
  },

  methods: {

    openMcsm: function () {
      let _this = this;
      _this.checkAdmin()
    },

    openConsole: function () {
      let _this = this;
      _this.checkAdmin_console()

    },

    checkAdmin: function () {
			let _this = this;
			console.log(_this.userInfo);
      let userinfo = JSON.parse(_this.userInfo)
      let sub_id = userinfo.sub
      console.log(sub_id)

      axios({
				method: 'post',
				baseURL: '/api',
				url: '/checkadmin',
				header: 'application/json',
				data: {
          'sub_id': sub_id
        }
      })
        .then(function (response) {
          console.log(response);
          console.log(response.data);
          _this.response = response.data
          let code = _this.response.code

          if (code === '0') {
            window.open(mcsm_url)
          } else {
            _this.$Notice.error({
              title: '拒绝访问',
              desc: '非管理员禁止访问该页面！'
            })
          }

        })
        .catch(function (error) {
					console.log(error);
					_this.response = error
          _this.error()

				});

    },

    checkAdmin_console: function () {
      let _this = this;
      console.log(_this.userInfo);
      let userinfo = JSON.parse(_this.userInfo)
      let sub_id = userinfo.sub
      console.log(sub_id)

      axios({
        method: 'post',
        baseURL: '/api',
        url: '/checkadmin',
        header: 'application/json',
        data: {
          'sub_id': sub_id
        }
      })
        .then(function (response) {
          console.log(response);
          console.log(response.data);
          _this.response = response.data
          let code = _this.response.code

          if (code === '0') {
            _this.$router.replace("/home/cmdline-console")
          } else {
            _this.$Notice.error({
              title: '拒绝访问',
              desc: '非管理员禁止访问该页面！'
            })
          }

        })
        .catch(function (error) {
          console.log(error);
          _this.response = error
          _this.error()

        });

    }

  }
}
</script>

<style scoped>

</style>
