// See http://programmingpraxis.com/2012/07/06/fractran/
package main

import (
	"fmt"
	"strings"
	"errors"
	"log"
	"math/big"
)

type Interpreter struct {
	integral *big.Int
	program  []*big.Rat
}

func (interpreter *Interpreter) Execute(n int64) <-chan *big.Int {
	ch := make(chan *big.Int)

	go func() {
		interpreter.integral.SetInt64(n)
		for {
			ch <- interpreter.integral
			found := false
			for _, r := range interpreter.program {
				z := new(big.Int)
				m := new(big.Int)
				z.Mul(interpreter.integral, r.Num())
				z.DivMod(z, r.Denom(), m)
				if m.Int64() == 0 {
					interpreter.integral = z
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

func (interpreter *Interpreter) LoadProgram(s string) error {
	a := strings.Split(s, " ")

	interpreter.integral = big.NewInt(0)
	interpreter.program = make([]*big.Rat, len(a))

	for i, substr := range a {
		r := new(big.Rat)
		if _, ok := r.SetString(substr); ok != true {
			return errors.New("fractan: invalid fraction '%s'")
		}
		interpreter.program[i] = r
	}

	return nil
}

func RunProgram(n int64, s string) error {
	interpreter := new(Interpreter)

	err := interpreter.LoadProgram(s)
	if err != nil {
		return err
	}

	ch := interpreter.Execute(n)
	for i := range ch {
		fmt.Printf("%v ", i)
	}
	return nil
}

func main() {
	err := RunProgram(2, "17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1")
	if err != nil {
		log.Fatal(err)
	}
}
