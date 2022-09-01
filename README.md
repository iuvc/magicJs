# magicJs
Find fun on the way to learn JavaScript.
# 前端界面展示 Json 数据字符串 format 格式化

&emsp;&emsp;在日常工作使用中，Json数据通常使用在与后端交互的场景中，但是很少在前端界面直接展示Json数据，这里介绍一种json数据格式化的简单方法  [JSON.stringify()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)。

#### JSON.stringify()：

**参数：**
 1. **value**：将要序列化成 一个 JSON 字符串的值。
 2. **replacer**（可选）：如果该参数是一个函数，则在序列化过程中，被序列化的值的每个属性都会经过该函数的转换和处理；如果该参数是一个数组，则只有包含在这个数组中的属性名才会被序列化到最终的 JSON 字符串中；如果该参数为 null 或者未提供，则对象所有的属性都会被序列化。
 3. **space**（可选）：指定缩进用的空白字符串，用于美化输出（pretty-print）；如果参数是个数字，它代表有多少的空格；上限为 10。该值若小于 1，则意味着没有空格；如果该参数为字符串（当字符串长度超过 10 个字母，取其前 10 个字母），该字符串将被作为空格；如果该参数没有提供（或者为 null），将没有空格。
 
 **返回值：**<br>
一个表示给定值的 JSON 字符串。

**格式化效果：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/9f64feb1f27d4f008636ce18b0485fb8.png)<br>
实现代码： <font color="red">需要注意的是需要用 类似HTML \<pre> 标签显示可定义预格式化的文本。 
```javascript
let jsonData = {
	"result": "OK",
	"data": [
		{
			" result": "OK",
			"检测数据": {
				"漏电流(mA)": "0.04",
				"理论时间[HH:MM:SS]": "00:01:00"
			},
			"检测方案": {
				"漏电流(mA)": "1.0",
				"上升时间(S)": "30",
				"测试时间(s)": "60",
				"耐压方式": "电压电流对辅助",
				"耐压值(KV)": "3.5"
			}
		}
	],
	"data_time": "2022-08-30 17:46:31",
	"product_id": "P095161863",
	"secondary_process_node": "HighVoltageA",
	"execute_result": "00000001",
	"process_node": "DXJC-0002"
}
JSON.stringify(jsonData,null,'\t')
```
