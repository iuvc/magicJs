const draggable = {
  inserted: function (el, binding) {
    let bodyClientWidth = parseInt(document.body.clientWidth)
    let bodyClientHeight = parseInt(document.body.clientHeight)
    let dragMoveReal = el
    let dialogTop = binding.value || '15vh'
    let dragMoveRealWidth = parseInt(dragMoveReal.style.width)
    if (dragMoveReal.style.width && dragMoveReal.style.width.indexOf) { // 这里是避免dragMoveReal获取的宽度为rem或者%定义的宽度
      if (dragMoveReal.style.width.indexOf('rem') != -1) {
        dragMoveRealWidth = parseInt(dragMoveReal.style.width) * 100
      } else if (dragMoveReal.style.width.indexOf('%') != -1) {
        dragMoveRealWidth = parseInt(dragMoveReal.style.width) / 100 * bodyClientWidth
      }
    }
    let dialogLeft = (bodyClientWidth - dragMoveRealWidth) / 2
    dragMoveReal.style.cursor = 'move'
    dragMoveReal.style.position = 'fixed'
    dragMoveReal.style.left = dialogLeft + 'px'
    dragMoveReal.style.top = dialogTop
    dragMoveReal.style.margin = '0'
    dragMoveReal.onmousedown = function (e) {
      let disx = e.pageX - dragMoveReal.offsetLeft
      let disy = e.pageY - dragMoveReal.offsetTop
      document.onmousemove = function (e) {
        let x = e.pageX - disx
        let y = e.pageY - disy
        let maxX = bodyClientWidth - parseInt(window.getComputedStyle(dragMoveReal).width)
        let maxY = bodyClientHeight - parseInt(window.getComputedStyle(dragMoveReal).height)
        if (x < 0) {
          x = 0
        } else if (x > maxX) {
          x = maxX
        }

        if (y < 0) {
          y = 0
        } else if (y > maxY) {
          y = maxY
        }
        dragMoveReal.style.left = x + 'px'
        dragMoveReal.style.top = y + 'px'
      }
      document.onmouseup = function () {
        document.onmousemove = document.onmouseup = null
      }
    }
  }
}
export default draggable
