package main

// http://programmingpraxis.com/2012/06/15/counting-ones/

import (
	"fmt"
	"time"
)

func countOnes(n int, c chan int) {
	ones := 0
	switch {
	case n == 1:
		ones = 1
	default:
		for n > 0 {
			d := n % 10
			if d == 1 {
				ones++
			}
			n = n / 10
		}
	}
	c <- ones
}

func main() {
	n := 1000
	c := make(chan int)
	start := time.Now()
	for i := 0; i <= n; i++ {
		go countOnes(i, c)
	}
	total := 0
	for i := 0; i <= n; i++ {
		total += <-c
	}
	fmt.Printf("%d [%s]\n", total, time.Since(start))
}
