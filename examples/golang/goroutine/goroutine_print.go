package main

import "fmt"

func main() {
	goroutineNum := 4
	ch := make(chan struct{})
	chanSlice := make([]chan struct{}, 0)
	exitC := make(chan struct{})
	for i := 0; i < goroutineNum; i++ {
		chanSlice = append(chanSlice, ch)
	}
	res := 1
	j := 1
	for i := 0; i < goroutineNum; i++ {
		go func(i int) {
			for {
				<-chanSlice[i]
				if res > 100 {
					exitC <- struct{}{}
					break
				}
				fmt.Printf("%d,%d\n", i, res)
				res++
				if j == goroutineNum-1 {
					j = 0
				} else {
					j++
				}
				chanSlice[j] <- struct{}{}
			}
		}(i)
	}
	chanSlice[0] <- struct{}{}
	select {
	case <-exitC:
		fmt.Println("end")
	}
}
