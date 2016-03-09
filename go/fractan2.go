package main

import (
	"fmt"
	"math"
	"math/big"
	"strings"
)

func Fractan(k int64, s string) <-chan *big.Int {
	n := big.NewInt(k)
	a := strings.Split(s, " ")
	p := make([]*big.Rat, len(a))

	for i, substr := range a {
		r := new(big.Rat)
		r.SetString(substr)
		p[i] = r
	}

	ch := make(chan *big.Int)

	go func() {
		for {
			ch <- n
			found := false
			for _, r := range p {
				z := new(big.Int)
				m := new(big.Int)
				z.Mul(n, r.Num())
				z.DivMod(z, r.Denom(), m)
				if m.Int64() == 0 {
					n = z
					found = true
					break
				}
			}
			if !found {
				break
			}
		}
		close(ch)
	}()

	return ch
}

func Primes() {
	primegame := "17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1"
	ch := Fractan(2, primegame)
	for i := range ch {
		n := i.Int64()
		if n&(n-1) == 0 {
			fmt.Println(i, int64(math.Floor(math.Log2(float64(n))+0.5)))
		}
	}
}

func main() {
	Primes()
}
