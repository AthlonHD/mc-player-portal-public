<template>
  <content>

    <div>

      <h2 style="text-align: left; margin-left: 40px; margin-top: 30px">请点击系统以进入：</h2>

      <Row>

        <router-link to="/home/white-list" tag="div">
          <Card style="width:320px; margin: 25px 25px 25px 75px;">
            <div style="text-align:center">
              <Icon type="md-people" size="45"/>
              <h3>白名单申请系统</h3>
            </div>
          </Card>
        </router-link>

<!--        <Card style="width:320px; margin: 25px;">-->
<!--          <div style="text-align:center">-->
<!--            <img src="../../public/single_user.jpeg" alt="白名单logo" style="width: 50px">-->
<!--            <h3>其他系统</h3>-->
<!--          </div>-->
<!--        </Card>-->

      </Row>


    </div>

  </content>

</template>

<script>
export default {
  name: "user-info",

  data () {
    return {

    }
  }
}
</script>

<style scoped>

</style>
