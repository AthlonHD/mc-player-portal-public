<template>
  <div>
    <iframe src="https://slimefun-helper.guizhanss.cn/"
            id="mobsf"
            scrolling="yes"
            frameborder="0"
            style="position:absolute;top:64px;left: 0px;right:0px;bottom:100px;">

    </iframe>
  </div>
</template>

<script>
export default {
  name: "slimefun-helper",

  mounted() {

    /**
    * iframe-宽高自适应显示
    */
    function changeMobsfIframe(){
    const mobsf = document.getElementById('mobsf');
    const deviceWidth = document.body.clientWidth;
    const deviceHeight = document.body.clientHeight;
    mobsf.style.width = (Number(deviceWidth)-2) + 'px'; //数字是页面布局宽度差值
    mobsf.style.height = (Number(deviceHeight)-64) + 'px'; //数字是页面布局高度差
    }

    changeMobsfIframe()

    window.onresize = function(){
    changeMobsfIframe()
    }

  }
}
</script>

<style scoped>

</style>
