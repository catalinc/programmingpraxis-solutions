// See http://programmingpraxis.com/2012/08/10/minimum-scalar-product/
package main

import (
	"fmt"
	"sort"
)

type Reverse struct {
	sort.Interface
}

func (r Reverse) Less(i, j int) bool {
	return r.Interface.Less(j, i)
}

func ScalarProduct(v1, v2 []int) int {
	p := 0
	for i := 0; i < min(len(v1), len(v2)); i++ {
		p += v1[i] * v2[i]
	}
	return p
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func MinScalarProduct(v1, v2 []int) int {
	sort.Ints(v1)
	sort.Sort(Reverse{sort.IntSlice(v2)})
	return ScalarProduct(v1, v2)
}

func main() {
	fmt.Printf("%d\n", MinScalarProduct([]int{1, 3, -5}, []int{-2, 4, 1}))
	fmt.Printf("%d\n", MinScalarProduct([]int{1, 2, 3, 4, 5}, []int{1, 0, 1, 0, 1}))
}
