
const dateTime = {
  secondFmt: 'yyyy-MM-dd hh:mm:ss',
  minuteFmt: 'yyyy-MM-dd hh:mm',
  hourMin: 'yyyy-MM-dd hh',
  dateFmt: 'yyyy-MM-dd',
  monthFmt: 'yyyy-MM',
  yearFmt: 'yyyy',
  /**
   * 获取本月1号时间
   * @param {*} date 日期
   * @param {*} fmt 格式化匹配格式
   */
  getMonthFirstDay: function (opts) {
    let { date, fmt } = opts || {}
    fmt = fmt || this.dateFmt

    let now = (typeof opts === 'string') ? new Date(opts) : (new Date(date || new Date()))
    let reDate = new Date(now.getFullYear(), now.getMonth(), 1)
    return this.dateToStr({ date: reDate, fmt })
  },
  /**
   * 获取本月最后一天时间
   * @param {*} date 日期
   * @param {*} fmt 格式化匹配格式
   * @param {*} isTotal 是否返回本月天数，默认返回日期格式
  */
  getMonthLastDay: function (opts, isTotal) {
    let { date, fmt } = opts || {}
    fmt = fmt || this.dateFmt

    let now = (typeof opts === 'string') ? new Date(opts) : (new Date(date || new Date()))
    let reDate = new Date(now.getFullYear(), now.getMonth() + 1, 0)
    return isTotal ? reDate.getDate() : this.dateToStr({ date: reDate, fmt })
  },
  /**
   * 获取与当前时间间隔几天，几月，几年的时间，默认返回上月。
   * 间隔月因为每个月最大天数不同，进行特殊处理。
   * @param {*} date 日期
   * @param {*} fmt 格式化匹配格式
   * @param {*} interval 间隔几天，几月，几年
   * @param {*} period 间隔周期，年、月、日
  */
  getIntervalDate(opts,followDefault) {
    let { date, fmt, interval, period} = opts || {}
    fmt = fmt || this.dateFmt
    interval = interval || -1
    period = period || 'month'

    let now = (typeof opts === 'string') ? new Date(opts) : (new Date(date || new Date()))
    let nowYear = period === 'year' ? now.getFullYear() + interval : now.getFullYear()
    let nowMonth = period === 'month' ? now.getMonth() + interval : now.getMonth()
    let nowDate = period === 'day' ? now.getDate() + interval : now.getDate()
    // 对年，月进行处理
    // 例如 2020-02-29减一年，应为2019-02-28
    // 例如 2020-03-30减一月，应为2019-02-28
    let isAddDay = false
    let currMonthMaxDay = null
    if ((period === 'month' || period === 'year')&&!followDefault) {
      currMonthMaxDay = this.getMonthLastDay({date: new Date(nowYear, nowMonth)}, true)
      if (currMonthMaxDay < nowDate) {
        isAddDay = true
      }
    }
    let reDate = new Date(nowYear, nowMonth, (isAddDay ? currMonthMaxDay : nowDate), now.getHours(), now.getMinutes(), now.getSeconds())
    return this.dateToStr({ date: reDate, fmt })
  },
  /**
   * 时间转字符串
   * @param {*} date 日期
   * @param {*} fmt 格式化匹配格式
  */
  dateToStr: function (opts) {
    let { date, fmt } = opts || {}
    date = (typeof opts === 'string') ? new Date(opts) : (new Date(date || new Date()))
    fmt = fmt || this.dateFmt

    let o = {
      'M+': date.getMonth() + 1, // 月份
      'd+': date.getDate(), // 日
      'h+': date.getHours(), // 小时
      'm+': date.getMinutes(), // 分
      's+': date.getSeconds(), // 秒
      'q+': Math.floor((date.getMonth() + 3) / 3), // 季度
      S: date.getMilliseconds() // 毫秒
    }

    if (/(y+)/.test(fmt)) {
      fmt = fmt.replace(
        RegExp.$1,
        (date.getFullYear() + '').substr(4 - RegExp.$1.length)
      )
    }
    for (let k in o) {
      if (new RegExp('(' + k + ')').test(fmt)) {
        fmt = fmt.replace(
          RegExp.$1,
          RegExp.$1.length === 1 ? o[k] : ('00' + o[k]).substr(('' + o[k]).length)
        )
      }
    }
    return fmt
  }
}

export default dateTime
