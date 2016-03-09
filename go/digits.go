package main

// A solution to http://programmingpraxis.com/2015/09/04/reversing-digits/
// Todo: make this work with big numbers

import (
	"fmt"
	"os"
	"strconv"
)

func Reverse(n int) int {
	r := 0
	for n > 0 {
		r *= 10
		r += n % 10
		n /= 10
	}
	return r
}

func main() {
	if len(os.Args) != 2 {
		os.Exit(1)
	}
	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		os.Exit(1)
	}
	fmt.Println(Reverse(n))
}
