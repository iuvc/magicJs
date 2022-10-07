import emoji from './custom-order/emoji'
import throttle from './custom-order/throttle'
import debounce from './custom-order/debounce'
import draggable from './custom-order/draggable'
// 自定义指令
const directives = {
  throttle,
  debounce,
  emoji,
  draggable
}
export default {
  install(Vue) {
    Object.keys(directives).forEach((key) => {
      Vue.directive(key, directives[key])
    })
  },
}