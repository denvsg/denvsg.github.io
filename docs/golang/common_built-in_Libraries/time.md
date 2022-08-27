# golang 内置库 time

## time 常用函数

#### 1. func After(d Duration) <-chan Time  // 等待持续时间过去后，然后在返回的通道上发送当前时间。它相当于NewTimer（d）.C。在计时器触发之前，垃圾回收器不会恢复基础计时器。如果效率是一个问题，请改用 NewTimer，如果不再需要计时器，请调用 Timer。停止。

```golang
package main

import (
	"fmt"
	"time"
)

var c chan int

func handle(int) {}

func main() {
	select {
	case m := <-c:
		handle(m)
	case <-time.After(10 * time.Second):
		fmt.Println("timed out")
	}
}
```

#### 2. func Sleep(d Duration) // 睡眠将暂停当前 goroutine 至少持续时间 d。负持续时间或零持续时间会导致睡眠立即恢复。

```golang
package main

import (
	"time"
)

func main() {
	time.Sleep(100 * time.Millisecond)
}
```

#### 3. func Date(year int, month Month, day, hour, min, sec, nsec int, loc *Location) Time //Date 返回对应于  yyyy-mm-dd hh:mm:ss + nsec nanoseconds  在给定位置的相应时间区域中。

```golang
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
	fmt.Printf("Go launched at %s\n", t.Local()) // Go launched at 2009-11-10 15:00:00 -0800 PST
}
```
#### 4. func Now() Time // Now 返回当前本地时间。
```golang
package main

import (
    "fmt"
    "time"
)

func main(){
    fmt.println(time.Now())
}
```


[back](Readme.md)