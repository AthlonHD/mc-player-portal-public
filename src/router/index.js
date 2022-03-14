import Vue from 'vue'
import VueRouter from 'vue-router'
import userInfo from "@/views/user-info";
import dashboard from "@/views/dashboard";
import whiteList from "@/views/white-list";
import cmdlineConsole from "@/views/cmdline-console";
import dailySign from "@/views/daily-sign";
import slimefunHelper from "@/views/slimefun-helper";
import checkMoney from "@/views/check-money";
import adminInfo from "@/views/admin-info";
import mcsm from "@/views/mcsm";
import lottery from "@/views/lottery";
import lotteryReward from "@/views/lottery-reward";


Vue.use(VueRouter)


const routes = [
	{
		path: '/',
		name: 'Login',
		component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
	},
	{
		path: '/callback',
		name: 'callback',
		component: () => import(/* webpackChunkName: "about" */ '../views/callback.vue')
	},
	{
		path: '/home',
		name: 'home',
		component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue'),
		children: [
			{
				path: '/home',
				name: 'dashboard',
				component: dashboard
			},
			{
				path: '/home/user-info',
				name: 'user-info',
				component: userInfo
			},
			{
				path: '/home/white-list',
				name: 'white-list',
				component: whiteList
			},
			{
				path: '/home/cmdline-console',
				name: 'cmdline-console',
				component: cmdlineConsole
			},
			{
				path: '/home/daily-sign',
				name: 'daily-sign',
				component: dailySign
			},
			{
				path: '/home/check-money',
				name: 'check-money',
				component: checkMoney
			},
			{
				path: '/home/slimefun-helper',
				name: 'slimefun-helper',
				component: slimefunHelper
			},
			{
				path: '/home/admin-info',
				name: 'admin-info',
				component: adminInfo
			},
			{
				path: '/home/mcsm',
				name: 'mcsm',
				component: mcsm
			},
			{
				path: '/home/lottery',
				name: 'lottery',
				component: lottery
			},
			{
				path: '/home/lottery-reward',
				name: 'lottery-reward',
				component: lotteryReward
			}
		]
	}
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
});


// const router = new VueRouter({
//   routes
// })

export default router
