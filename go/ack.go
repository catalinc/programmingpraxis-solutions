package main

import (
	"fmt"
	"os"
	"strconv"
)

func ack(m, n int) int {
	switch {
	case m == 0:
		return n + 1
	case m > 0 && n == 0:
		return ack(m-1, 1)
	case m > 0 && n > 0:
		return ack(m-1, ack(m, n-1))
	}
	panic(fmt.Sprintf("invalid arguments m=%d n=%d", m, n))
}

func main() {
	if len(os.Args) != 3 {
		fmt.Printf("usage: %s m n\n", os.Args[0])
		os.Exit(1)
	}
	m, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Printf("invalid argument m = %s\n", os.Args[1])
		os.Exit(1)
	}
	n, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Printf("invalid argument n = %s\n", os.Args[2])
		os.Exit(1)
	}
	fmt.Printf("ack(%d, %d) = %d", m, n, ack(m, n))
}
