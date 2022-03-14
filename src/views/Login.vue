<template>

  <div class="limiter">
		<div class="container-login100">

			<div class="wrap-login100">

        <row>

          <form class="login100-form validate-form" autocomplete="off" style="padding-top: 50px;">

            <row>

<!--              <img src="../../public/logo.png" alt="logo" style="width: 100%; margin-bottom: 150px">-->

            </row>


            <span class="login100-form-title p-b-43">
                服务器名称
              <p>Minecraft服务器玩家门户</p>
            </span>

            <div class="container-login100-form-btn">
              <div class="login100-form-btn" @click="handeLogin" style="background: #333333">
                  点击进入
              </div>
            </div>
          </form>

        </row>


			</div>
		</div>
	</div>


</template>

<script>


export default {
	name: 'Login',
	inject: ['$authing'],
	methods: {
		handeLogin: async function() {
			// PKCE 场景使用示例
			// 生成一个 code_verifier
			let codeChallenge = this.$authing.generateCodeChallenge();
			localStorage.setItem('codeChallenge', codeChallenge);
			// 计算 code_verifier 的 SHA256 摘要
			let codeChallengeDigest = this.$authing.getCodeChallengeDigest({ codeChallenge, method: 'S256' });
			// 构造 OIDC 授权码 + PKCE 模式登录 URL
			let url = this.$authing.buildAuthorizeUrl({ codeChallenge: codeChallengeDigest, codeChallengeMethod: 'S256' });
      console.log(url)
			window.location.href = url;
		}
	}
};
</script>

<style>
@import './login.scss';
.p-b-43 {
  padding-bottom: 43px;
}

:root {
  --el-color-primary: #409eff;
  --el-color-success: #67c23a;
  --el-color-warning: #e6a23c;
  --el-color-danger: #f56c6c;
  --el-color-error: #f56c6c;
  --el-color-info: #909399;
}


</style>
