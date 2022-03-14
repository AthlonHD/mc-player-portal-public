<template>
  <div>

    <Menu mode="horizontal" theme="primary" active-name="1" width="auto">
        <MenuItem name="1">
            <router-link to="/home/user-info" tag="div">
              <Icon type="ios-people" />
              账户管理
            </router-link>
        </MenuItem>
        <MenuItem name="2">
          <router-link to="/home/admin-info" tag="div">
            <Icon type="ios-paper" />
            内容管理
          </router-link>
        </MenuItem>
        <MenuItem name="3" disabled="">
          <router-link to="/home/lottery" tag="div">
            <Icon type="md-grid" />
            抽奖系统
          </router-link>
        </MenuItem>
        <Submenu name="4">
            <template slot="title">
                <Icon type="ios-construct" />
                工具箱
            </template>
            <MenuGroup title="个人">
                <MenuItem name="3-1">
                  <router-link to="/home/daily-sign" tag="div">
                    <Icon type="md-checkmark-circle-outline" />每日签到
                  </router-link>
                </MenuItem>
                <MenuItem name="3-2">
                  <router-link to="/home/check-money" tag="div">
                    <Icon type="ios-search" />铜板查询
                  </router-link>
                </MenuItem>
                <MenuItem name="3-3" disabled="true">
                  <Icon type="md-cube" />物品申领
                </MenuItem>
            </MenuGroup>
            <MenuGroup title="全部">
                <MenuItem name="3-4">
                  <router-link to="/home/slimefun-helper" tag="div">
                    <Icon type="ios-apps" />粘液科技小助手
                  </router-link>
                </MenuItem>
<!--                <MenuItem name="3-5">当前在线用户查询</MenuItem>-->
<!--                <MenuItem name="3-6">服务器铜板排名查询</MenuItem>-->
            </MenuGroup>
        </Submenu>
<!--        <MenuItem name="4">-->
<!--            <Icon type="ios-settings" />-->
<!--            综合设置-->
<!--        </MenuItem>-->

      <div style="text-align: right; margin-right: 40px">

        <Poptip trigger="hover" title="当前账号" :content="phone_number" style="text-align: center">
          <Button type="info" @click="handleLogout">登出</Button>
        </Poptip>

      </div>

<!--        <Poptip trigger="hover" title="当前账号" :content="phone_number">-->
<!--          <Button type="info" @click="handleLogout">登出</Button>-->
<!--        </Poptip>-->

    </Menu>


  </div>
</template>

<script>
import main from '../../config.json'

let redirectUri = main.main.redirectUri

export default {
  name: "navigator",

  data () {
    return {
      userInfo: '',
      phone_number: ''
    }

  },

  inject: ['$authing'],
  mounted: function () {
    this.userInfo = localStorage.getItem('userInfo');
    console.log(this.userInfo)
    this.phone_number = JSON.parse(this.userInfo).phone_number
    console.log(this.phone_number)

  },
  methods: {
    // input有内容输入就更新试图
    // updateView () {
    // 	this.$forceUpdate()
    // },
    handleLogout: function () {
      localStorage.clear();
      // 此处填写authing上登出回调地址
      window.location.href = this.$authing.buildLogoutUrl({redirectUri: redirectUri});
    },
  }
}
</script>

<style scoped>

</style>
