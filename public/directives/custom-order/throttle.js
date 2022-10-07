const throttle = {
  bind: (el, binding) => {
    // console.log('指令与元素绑定')
    let { throttleFunc, onThrottle, timeout } = binding.value||{}
    timeout = timeout || 2 * 1000 
    let throttleTimer;
    el.addEventListener('click', event => {
      if (!throttleTimer) {
        if(throttleFunc)throttleFunc() // 节流取消或者第一次触发时的事件
        throttleTimer = setTimeout(() => {
          throttleTimer = null;
        }, timeout);
      } else {
        console.warn('处于节流，无法触发点击事件，防误触时间间隔：'+timeout+' ms')
        if(onThrottle)onThrottle() // 触发节流时触发的事件
        event && event.stopImmediatePropagation();
      }
    }, true);
  },
  unbind(el) {
    // console.warn('指令与元素解绑')
    el.removeEventListener('click', el.handler)
  }
}
export default throttle
