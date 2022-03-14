<template>

  <content>

    <Alert type="warning">注意：需要选择所在区服后，再进行查询。否则数据将不一定准确！</Alert>

    <RadioGroup v-model="button_server" type="button" button-style="solid" size="large" style="width: 500px; margin-top: 200px; margin-left: 80px" onchange="">
      <Radio label="粘液一区"></Radio>
      <Radio label="粘液二区"></Radio>
      <Radio label="粘液三区"></Radio>
      <Radio label="粘液四区"></Radio>
    </RadioGroup>

    <Form :model="formItem" :label-width="80" style="margin-top: 50px">
      <FormItem>
        <Button type="primary" @click="checkMoney" size="large" icon="ios-search" shape="circle">点我查询</Button>
      </FormItem>
    </Form>

  </content>

</template>

<script>
import axios from "axios";

export default {
  name: "check-money",
    data () {
    return {
      formItem: '',
      userInfo: '',
      button_server: '粘液一区',
    }
  },

  inject: ['$authing'],
  mounted: function () {
    this.userInfo = localStorage.getItem('userInfo');
    console.log(this.userInfo)
  },

  methods: {

    checkMoney: function () {
			let _this = this;
			console.log(_this.userInfo);
      let userinfo = JSON.parse(_this.userInfo)
			let phone_num = userinfo.phone_number
      let button_server = this.button_server
      console.log(button_server)

      let server = this.server
      if (button_server === '粘液一区') {
        server = '0'
      } else if (button_server === '粘液二区') {
        server = '1'
      } else if (button_server === '粘液三区') {
        server = '2'
      } else if (button_server === '粘液四区') {
        server = '3'
      }
      console.log(server)

			axios({
				method: 'post',
				baseURL: '/api',
				url: '/checkmoney',
				header: 'application/json',
				data: {
          'phone_num': phone_num,
          'server': '0'
        }
      })
        .then(function (response) {
          console.log(response);
          console.log(response.data);
          _this.response = response.data
          let code = _this.response.code
          let message = _this.response.message
          let data = _this.response.data

          if (code === '0') {
            _this.$Modal.info({title: '当前铜板余额', content: data})

          } else if (code === '100') {
            _this.$Modal.error({title: '错误', content: message})
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