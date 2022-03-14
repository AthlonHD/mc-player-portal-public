<template>

  <content>

    <Form :model="formItem" :label-width="80" style="margin-top: 200px">
      <FormItem>
        <Button type="primary" @click="dailySign" size="large" icon="md-checkmark-circle-outline">点我签到</Button>
      </FormItem>
    </Form>

  </content>

</template>

<script>
import axios from 'axios'

export default {
  name: "daily-sign",
  data () {
    return {
      formItem: '',
      userInfo: '',
    }
  },

  inject: ['$authing'],
  mounted: function () {
    this.userInfo = localStorage.getItem('userInfo');
    console.log(this.userInfo)
  },

  methods: {
    success () {
      this.$Message.success({content: '签到成功！奖励已发放至游戏账户！', duration: 3});
    },
    warning () {
      this.$Message.warning('今天已经签到过啦~明天再来吧！');
    },
    error () {
      this.$Message.error('程序异常');
    },
    null_id () {
      this.$Message.error('未能找到玩家id！')
    },

    // 执行指令
    dailySign: function() {
			let _this = this;
			console.log(_this.userInfo);
      let userinfo = JSON.parse(_this.userInfo)
			let phone_num = userinfo.phone_number


			axios({
				method: 'post',
				baseURL: '/api',
				url: '/dailysign',
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
          // let data = _this.response.data
          if (code === '0') {
            _this.success()
            // _this.$Message.success({content: data+'(铜板不一定准确)', duration: 3})

          } else if (code === '100') {
            _this.warning()
          } else if (code === '200') {
            _this.error()
          } else if (code === '300') {
            _this.null_id()
          }

				})
				.catch(function (error) {
					console.log(error);
					_this.response = error
          _this.error()

				});

		},
  }

}
</script>

<style scoped>

</style>
