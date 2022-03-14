<template>

    <content>

      <Row>
        <Col span="24">
          <Form :model="formItem" :label-width="0">

            <RadioGroup v-model="button_server" type="button" button-style="solid" size="large" style="width: 500px; margin-top: 50px;" onchange="">
              <Radio label="粘液一区"></Radio>
              <Radio label="粘液二区"></Radio>
              <Radio label="粘液三区"></Radio>
              <Radio label="粘液四区"></Radio>
            </RadioGroup>

            <FormItem>
              <Input v-model="formItem.cmd" placeholder="请输入指令" style="width: 500px; margin-top: 50px" size="large"></Input>
            </FormItem>

            <FormItem>
              <Button type="primary" @click="command" icon="md-checkmark" size="large">执行</Button>

            </FormItem>
          </Form>
        </Col>
<!--        <Col span="8">-->

<!--          <iframe src="https://slimefun-helper.guizhanss.cn/"-->

<!--                scrolling="yes"-->
<!--                frameborder="0"-->
<!--                style="position:absolute;top:20px;left: 0; right:0; bottom:100px; height: 850px">-->

<!--          </iframe>-->

<!--        </Col>-->
      </Row>


    </content>


</template>

<script>
import axios from 'axios'

export default {
  name: "cmdline-console",

  data () {
    return {
      formItem: {
        cmd: '',

      },
      button_server: '粘液一区',
      server: '0',

    }
  },

  inject: ['$authing'],
  mounted: function () {
    this.userInfo = localStorage.getItem('userInfo');
    console.log(this.userInfo)
    this.checkAdmin_console()
  },


  methods: {
    success () {
      this.$Message.success({content: '执行成功', duration: 3});
    },
    warning () {
          this.$Message.warning('请输入执行内容');
    },
    error () {
          this.$Message.error('程序异常');
    },

    checkAdmin_console: function () {
      let _this = this;
      // console.log(_this.userInfo);
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

          if (code !== '0') {
            _this.$router.replace("/home")
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

    // 执行指令
    command: function() {
			let _this = this;
			let cmd = this.formItem.cmd
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
				url: '/cmd',
				header: 'application/json',
				data: {
					'cmd': cmd,
          'server': server
				}
			})
				.then(function (response) {
					console.log(response);
          console.log(response.data);
          _this.response = response.data
          let code = _this.response.code
          let data = _this.response.data
          if (code === '0') {
            _this.success()
            _this.$Message.success({content: data, duration: 3})

          } else if (code === '100') {
            _this.warning()
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
