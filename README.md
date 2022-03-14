# Minecraft Player Portal
我的世界玩家门户

### 当前功能清单

#### 1.白名单申请
![](https://s3.bmp.ovh/imgs/2022/03/a515e27ec81457c8.png)
#### 2.每日签到领奖励
![](https://i.bmp.ovh/imgs/2022/03/06cc20ccbaa3cca8.png)
#### 3.网页指令分区服发送
![](https://i.bmp.ovh/imgs/2022/03/2aeb83c3bc4ad79f.png)
#### 4.链接跳转mcsm
![](https://i.bmp.ovh/imgs/2022/03/49b0b302f1cae65b.png)
#### 5.抽奖系统
![](https://i.bmp.ovh/imgs/2022/03/6f804b302d56f861.png)
#### 6.内嵌粘液科技小助手 Created by https://github.com/ybw0014
（不需要的可以直接注释掉
![](https://i.bmp.ovh/imgs/2022/03/521e665a2f1882e2.png)

### 功能说明
```angular2html
1.为节省开发成本（各方面），所以账号系统用的是authing提供的服务（有一定免费额度）
2.使用前需要注册一个authing应用，然后把对应参数填入配置文件 -> https://console.authing.cn/
3.因为当前精力不足以处处维护到位，所以配置化做的不是很好（ ，遇到问题可以提issue
```


### 需要修改参数部分
```angular2html
./config.json
    ｜  main              
        ｜  redirectUri   此处填写authing上的登出回调地址
        ｜  appId         此处填写authing上的APPID
        ｜  appHost       此处填写authing上的认证地址

    ｜  rcon
        |  url            此处填写需要执行rcon服务器的地址
        |  port           此处填写需要执行rcon服务器的rcon端口
        |  passwd         此处填写需要执行rcon服务器的rcon密码

    |  mcsm_url           mcsm网址

    |  jdbc
        |  host           数据库地址
        |  port           数据库端口 （int类型）
        |  user           数据库账号
        |  passwd         数据库密码
        |  db             数据库

./vue.config.js
    ｜  api
        |  target         此处填写app后端的IP及端口

```

### 数据库表创建

#### mc_whitelist
```angular2html
CREATE TABLE mc.mc_whitelist (
	id INT auto_increment NOT NULL,
	game_id varchar(100) NOT NULL,
	phone_num varchar(100) NOT NULL,
	sub_id varchar(100) NOT NULL,
	CONSTRAINT mc_whitelist_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci
AUTO_INCREMENT=1;
```
#### game_id
```angular2html
CREATE TABLE `game_id` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=785 DEFAULT CHARSET=utf8;
```
#### portal_admin
```angular2html
CREATE TABLE `portal_admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin_sub_id` varchar(100) NOT NULL COMMENT '管理员门户系统用户id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
```
#### daily_sign
```angular2html
CREATE TABLE `daily_sign` (
  `id` int NOT NULL AUTO_INCREMENT,
  `phone_num` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户手机号',
  `sign_date` varchar(26) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=719 DEFAULT CHARSET=utf8;
```
#### lottery_bind_server_new
```angular2html
CREATE TABLE `lottery_bind_server_new` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sub_id` varchar(100) NOT NULL,
  `bind_server` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
```
#### lottery_record
```
CREATE TABLE `lottery_record` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sub_id` varchar(100) NOT NULL,
  `reward` varchar(100) NOT NULL,
  `is_delivered` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6316 DEFAULT CHARSET=utf8;
```

### 安装项目
```
pnpm install
```

### 开发环境编译及热更新
```
pnpm serve
```

### 生产环境编译及压缩
```
pnpm build
```

### 项目运行地址
```
localhost:4000
```


### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
