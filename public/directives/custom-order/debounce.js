let debounceFunc,timeout,debounceTimer
let executeFunc = async function(){
  debounceTimer = await setTimeout(() => {
    if(debounceFunc)debounceFunc()
  }, timeout);
}
let clearTimer = function(){
  clearTimeout(debounceTimer)
  debounceTimer = null;
}
const debounce = {
  bind: (el, binding) => {
    // console.log('指令与元素绑定')
    let val = binding.value||{}
    debounceFunc = val.debounceFunc
    timeout = val.timeout || 3 * 1000
    el.addEventListener('input', () => {
      if (debounceTimer) {
        console.warn('先清除上次还未执行的延时事件')
        clearTimer()
        executeFunc()
      }else{
        executeFunc()
      }
    }, true);
  },
  unbind(el) {
    el.removeEventListener('input', el.handler)
  }
}
export default debounce
