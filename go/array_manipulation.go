package main

import "fmt"

// Solution to https://programmingpraxis.com/2016/07/22/array-manipulation/

func leastGreater(a []int, i int) int {
	res := -1
	for j := i + 1; j < len(a); j++ {
		if a[j] > a[i] && (a[j] < res || res == -1) {
			res = a[j]
		}
	}
	return res
}

func solve(a []int) []int {
	res := make([]int, len(a))
	for i := 0; i < len(a); i++ {
		res[i] = leastGreater(a, i)
	}
	return res
}

func main() {
	a := []int{8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28}
	r := solve(a)
	fmt.Printf("%v\n", r)
}
