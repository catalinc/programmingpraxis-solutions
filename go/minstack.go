package main

import "fmt"

type MinStack struct {
	stack []int
	mins  []int
}

func NewMinStack() *MinStack {
	return &MinStack{make([]int, 0), make([]int, 0)}
}

func (st *MinStack) String() string {
	if st.Empty() {
		return "empty stack"
	}
	return fmt.Sprintf("top=%d min=%d", st.Top(), st.Min())
}

func (st *MinStack) Empty() bool {
	return len(st.stack) == 0
}

func (st *MinStack) Push(n int) {
	st.stack = append(st.stack, n)
	if len(st.mins) == 0 || n <= st.mins[len(st.mins)-1] {
		st.mins = append(st.mins, n)
	}
}

func (st *MinStack) Top() int {
	if st.Empty() {
		panic("empty stack")
	}
	return st.stack[len(st.stack)-1]
}

func (st *MinStack) Pop() int {
	if st.Empty() {
		panic("empty stack")
	}
	n := st.stack[len(st.stack)-1]
	st.stack = st.stack[0 : len(st.stack)-1]
	if n == st.mins[len(st.mins)-1] {
		st.mins = st.mins[0 : len(st.mins)-1]
	}
	return n
}

func (st *MinStack) Min() int {
	if st.Empty() {
		panic("empty stack")
	}
	return st.mins[len(st.mins)-1]
}

func main() {
	st := NewMinStack()
	st.Push(3)
	st.Push(4)
	st.Push(5)
	fmt.Println(st)
	st.Push(1)
	st.Push(2)
	fmt.Println(st)
	st.Pop()
	st.Pop()
	fmt.Println(st)
}
