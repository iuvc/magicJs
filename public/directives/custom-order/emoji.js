let findEle = (parent, type) => {
  console.log( parent.type)
  return parent.tagName.toLowerCase() === type ? parent : parent.querySelector(type)
}
 
const trigger = (el, type) => {
  const e = document.createEvent('HTMLEvents')
  e.initEvent(type, true, true)
  el.dispatchEvent(e)
}
 
const emoji = {
  bind: function (el) {
    // 正则规则可根据需求自定义
    var regRule = /[^u4E00-u9FA5|\d|a-zA-Z|_\-~?+.]/g
    let $inp = findEle(el, 'input')
    el.$inp = $inp
    $inp.handle = function () {
      let val = $inp.value
      let result = regRule.test(val)
      console.log(result,val)
      $inp.value = val.replace(regRule, '')
      trigger($inp, 'input')
    }
    $inp.addEventListener('keyup', $inp.handle)
  },
  unbind: function (el) {
    el.$inp.removeEventListener('keyup', el.$inp.handle)
  },
}
 
export default emoji