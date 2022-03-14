<template>

  <content>

    <Alert type="warning">注意：id中不能带有空格以及中文汉字，若因注册时id不合法导致无法进入服务器后果自负</Alert>


    <Form :model="formItem" :label-width="0">
      <FormItem>
        <Input v-model="formItem.game_id" placeholder="请输入游戏id" style="width: 200px; margin-top: 50px" size="large"></Input>
      </FormItem>

      <FormItem>
        <Button type="primary" @click="createID" size="large">申请白名单</Button>
<!--        <Button type="info" style="margin-left: 16px">检查ID</Button>-->
<!--        <Button style="margin-left: 16px">查询当前账号绑定ID</Button>-->
      </FormItem>
      </Form>

  </content>


</template>

<script>
import axios from 'axios'

export default {
  name: "white-list",

  data () {
    return {
      formItem: {
        game_id: '',

      },
      userInfo: '',
			response: {},
    }
  },

  inject: ['$authing'],

  mounted: function () {
    this.userInfo = localStorage.getItem('userInfo');
    console.log(this.userInfo)
  },

  methods: {
    instance (type) {
      switch (type) {
        case 'success':
          this.$Modal.success({
              title: '成功',
              content: '白名单账号创建成功！'
          });
          break;
        case 'same_id':
          this.$Modal.warning({
              title: '失败',
              content: '此ID已经被使用！'
          });
          break;
        case 'phone_exists':
          this.$Modal.warning({
              title: '失败',
              content: '此手机号已绑定账号！'
          });
          break;
        case 'error':
          this.$Modal.error({
              title: '程序异常',
              content: '请联系群内相关人员支持！'
          });
          break;
      }
    },

    // 创建id
    createID: function() {
			let _this = this;
			console.log(_this.userInfo);
			let userinfo = JSON.parse(_this.userInfo)
			let phone_num = userinfo.phone_number
			let sub_id = userinfo.sub
			let game_id = this.formItem.game_id


			axios({
				method: 'post',
				baseURL: '/api',
				url: '/createid',
				header: 'application/json',
				data: {
					'game_id': game_id,
					'phone_num': phone_num,
					'sub_id': sub_id
				}
			})
				.then(function (response) {
					console.log(response);
          console.log(response.data);
          _this.response = response.data
          let code = _this.response.code
          if (code === '0') {
            _this.instance('success')

          } else if (code === '100') {
            _this.instance('same_id')
          } else if (code === '200') {
            _this.instance('phone_exists')
          }


				})
				.catch(function (error) {
					console.log(error);
					_this.response = error
          _this.instance('error')

				});

		},
  }
}
</script>

<style scoped>

</style>
