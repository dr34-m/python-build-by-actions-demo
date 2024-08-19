import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '@/views/layout.vue'

const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter)

const routes = [{
		path: '/',
		name: '首页',
		meta: {
			disableLeft: true,
			letfIndex: ''
		},
		component: () => import('@/views/index')
	},
	{
		path: '/login',
		name: '登录',
		meta: {
			disableLeft: true,
			letfIndex: ''
		},
		component: () => import('@/views/Login')
	},
	{
		path: '/home',
		component: Layout,
		children: [{
			path: '',
			component: () => import('@/views/page/home/index'),
			name: 'home',
			meta: {
				letfIndex: '/home'
			}
		}]
	},
	{
		path: '/setting',
		component: Layout,
		children: [{
			path: '',
			component: () => import('@/views/page/setting/index'),
			name: 'setting',
			meta: {
				letfIndex: '/setting'
			}
		}]
	}
]

const router = new VueRouter({
	mode: 'hash',
	routes
})

export default router