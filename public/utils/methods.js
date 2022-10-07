/**
 * 判断数据类型 
 * @param {*} data 传入数据，判断类型
 */
export function outputDataType(data) {
  let dataTypeStr = Object.prototype.toString.call(data)
  // let dataTypeStr = Object.prototype.toString.apply(data)
  // toString返回的是[object xxx],进行字符串截取返回对应数据类型
  dataTypeStr = dataTypeStr.match(/\[object (\S*)\]/)[1]
  // console.log(dataTypeStr)
  return dataTypeStr
}
/**
 * 查找列表中符合值的数据
 * @param {*} list 数据集合
 * @param {*} key 对比取值key
 * @param {*} value 对比value
 */
export function findListItemByKey(list,key,value) {
  let result = null
  list.forEach(item=>{ if(item[key]===value) result = item })
  return result
}
/**
 * 初始化数据。
 * @param {*} item 传入数据
 */
export function clearItemValue(item) {
  switch (outputDataType(item)) {
    case 'Number': item = null; break;
    case 'String': item = ''; break;
    case 'Boolean': item = null; break;
    case 'Null': item = null; break;
    case 'Undefined': item = null; break;
    case 'Symbol': item = null; break;
    case 'Object': item = {}; break;
    case 'Date': item = new Date(); break;
    case 'RegExp': item = new RegExp(); break;
    case 'Array': item = []; break;
    case 'Function': item = function () { }; break;
    default: item = null; break;
  }
  return item
}
/**
 * 清除对象属性值，仅支持Object/Array数据清除。
 * @param {*} obj 传入数据
 */
export function clearObjectValue(initalObj, finalObj = {}) {
  let bol = isArrayOrObject(initalObj)
  if (!bol) return clearItemValue(initalObj)
  Object.keys(initalObj).forEach((key) => {
    bol = isArrayOrObject(initalObj[key])
    finalObj[key] = bol ? clearObjectValue(initalObj[key], bol === 'Array' ? [] : {}) : clearItemValue(initalObj[key])
  })
  // // 或者采用 for in
  // for (var key in initalObj) {
  //   bol = isArrayOrObject(initalObj[key])
  //   finalObj[key] = bol ? clearObjectValue(initalObj[key], bol === 'Array' ? [] : {}) : clearItemValue(initalObj[key])
  // }
  return finalObj;
}

/**
 * 递归实现深拷贝。
 * @param {*} initalObj 传入参数
 */
export function cloneDepth(initalObj, finalObj = {}) {
  let bol = isArrayOrObject(initalObj)
  if (!bol) return initalObj 
  Object.keys(initalObj).forEach((key) => {
    bol = isArrayOrObject(initalObj[key])
    finalObj[key] = bol ? cloneDepth(initalObj[key], bol === 'Array' ? [] : {}) : initalObj[key]
  })
  // // 或者采用 for in
  // for (var key in initalObj) {
  //   bol = isArrayOrObject(initalObj[key])
  //   finalObj[key] = bol ? cloneDepth(initalObj[key], bol === 'Array' ? [] : {}) : initalObj[key]
  // }
  return finalObj;
}
export function isArrayOrObject(list) {
  let isBool = false
  switch (outputDataType(list)) {
    case 'Object': isBool = 'Object'; break;
    case 'Array': isBool = 'Array'; break;
    default: isBool = false; break;
  }
  return isBool
}
