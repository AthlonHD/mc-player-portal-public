<template>

  <content>

    <Alert>提示：手机用户请横屏使用</Alert>

    <Table border :columns="columns" :data="data_reward" style="margin: auto;">
        <template slot-scope="{ row }" slot="reward">
            <strong>{{ row.reward }}</strong>
        </template>
        <template slot-scope="{ row, index }" slot="action">
            <Button type="primary" size="medium" style="margin-right: 5px" @click="pushRewards(index)">发放</Button>
        </template>
    </Table>

  </content>

</template>

<script>
import axios from "axios";

export default {
  name: "lottery-reward",

  data () {
    return {
      columns: [
        {
          title: '物品名称',
          slot: 'reward',

        },
        {
          title: '操作',
          slot: 'action',
          width: 150,
          align: 'center'
        }
      ],
      data_reward: [
        {
          reward: ''
        },


      ]

    }


  },

  inject: ['$authing'],
  mounted: function () {
    this.userInfo = localStorage.getItem('userInfo');
    console.log(this.userInfo)

    this.queryRewards()

  },

  methods: {

    queryRewards: function () {
      let _this = this
      console.log(_this.userInfo);
      let userinfo = JSON.parse(_this.userInfo)
      let sub_id = userinfo.sub
      console.log(sub_id)

      axios({
        method: 'post',
        baseURL: '/api',
        url: '/lottery.queryreward',
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
          let data = _this.response.data
          console.log(code)

          // eslint-disable-next-line no-debugger
          // debugger
          if (code === '0') {
            _this.$Notice.success({title: '数据查询成功'})
            _this.data_reward = data
          } else if (code === '100') {
            _this.$Notice.info({title: '未查到到数据'})
          }

        })
        .catch(function (error) {
          console.log(error);
          _this.response = error
          _this.error()

        });


    },

    pushRewards: function (index) {
      let _this = this
      _this.$Loading.start()
      console.log(_this.data_reward[index].reward)

      let userinfo = JSON.parse(_this.userInfo)
      let sub_id = userinfo.sub
      console.log(sub_id)

      let reward = _this.data_reward[index].reward

      axios({
        method: 'post',
        baseURL: '/api',
        url: '/lottery.pushreward',
        header: 'application/json',
        data: {
          'sub_id': sub_id,
          'reward': reward
        }
      })
        .then(function (response) {
          console.log(response);
          console.log(response.data);
          _this.response = response.data
          let code = _this.response.code
          let data = _this.response.data
          console.log(code)

          if (code === '0') {
            _this.$Loading.finish()
            _this.data_reward = data
            _this.$Modal.success({title: '发放成功', content: data})

            _this.queryRewards()

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