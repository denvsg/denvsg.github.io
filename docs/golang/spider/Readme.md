# golang 爬虫

#### Go语言爬虫框架有 Colly和Goquery

```golang
// visit https://github.com/gocolly/colly
package main

import (
	"fmt"
	"github.com/gocolly/colly"
)

func main() {
	fmt.Println("golang spider")
	c := colly.NewCollector()

	// Find and visit all links
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		e.Request.Visit(e.Attr("href"))
	})

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})

	c.Visit("http://go-colly.org/")
}
```

##### **colly 支持的事件类型，如下：**

OnRequest 请求执行之前调用  
OnResponse 响应返回之后调用  
OnHTML 监听执行 selector  
OnXML 监听执行 selector  
OnHTMLDetach，取消监听，参数为 selector 字符串  
OnXMLDetach，取消监听，参数为 selector 字符串  
OnScraped，完成抓取后执行，完成所有工作后执行  
OnError，错误回调  
最后，c.Visit() 正式启动网页访问。  
c.Visit("http://go-colly.org/")



<br />
<br />
<br />
<br />
<br />

......     
[回到目录](../contents_page.md)     
......
