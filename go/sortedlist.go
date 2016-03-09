/**
 * Problem description is located at http://programmingpraxis.com/2011/08/16/insert-into-a-cyclic-sorted-list
 */
package main

import "fmt"

type Node struct {
    value int
    next *Node
}

func NewNode(value int) *Node {
    return &Node{value, nil}
}

func (n *Node) String() string {
    s := ""
    for crt := n;; {
        s += fmt.Sprintf("%d", crt.value)
        crt = crt.next
        if crt != n && crt != nil {
            s += " "
        } else {
            break
        }
    }
    return s
}

func MakeTestList() *Node {
    n1 := NewNode(2)
    n2 := NewNode(3)
    n3 := NewNode(5)
    n4 := NewNode(7)
    n5 := NewNode(11)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n1

    return n3
}

func InsertCyclicSortedList(value int, nl *Node) {
    crt := nl
    for {
        if value >= crt.value && value <= crt.next.value {
            n := NewNode(value)
            n.next = crt.next
            crt.next = n
            break
        } else if crt.value > crt.next.value {
            if value >= crt.value || value <= crt.next.value {
                n := NewNode(value)
                n.next = crt.next
                crt.next = n

                break
            }
        }
        crt = crt.next
    }
}

func main() {
    nl := MakeTestList()
    fmt.Printf("test data: %s\n", nl)
    values := []int{4, 8, 9, 1, 12, 7, 0}
    for _, v := range values {
        InsertCyclicSortedList(v, nl)
        fmt.Printf("%d -> %s\n", v, nl)
    }
}

