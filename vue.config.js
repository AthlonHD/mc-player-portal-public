module.exports = {
	devServer: {
		proxy: {
			//配置跨域
			'/api': {
				target: 'http://127.0.0.1:23333/',  // 此处填写运行app服务器的真实IP及后端端口
				// target: 'http://127.0.0.1:23334/',  // 开发环境
				changOrigin: true,  //允许跨域
				pathRewrite: {
			// eslint-disable-next-line no-mixed-spaces-and-tabs
		      /* 重写路径，当我们在浏览器中看到请求的地址为：http://localhost:8080/api/core/getData/userInfo 时
		        实际上访问的地址是：http://ip:port/core/getData/userInfo,因为重写了 /api
		       */
				'^/api': ''
				}
			},

		},
		// 前端端口
		port: 4000,
		disableHostCheck: true
	}
};
