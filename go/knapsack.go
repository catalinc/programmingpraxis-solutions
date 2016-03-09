package main

// http://programmingpraxis.com/2011/08/23/knapsack/

import (
	"fmt"
	"sort"
	"os"
	"flag"
	"io"
	"bufio"
)

type Item struct {
	name   string
	value  int
	weight int
}

func (it *Item) String() string {
	return fmt.Sprintf("%s %d %d", it.name, it.value, it.weight)
}

type Items []*Item

func (items Items) Len() int {
	return len(items)
}

func (items Items) Less(i, j int) bool {
	return items[i].weight < items[j].weight
}

func (items Items) Swap(i, j int) {
	items[i], items[j] = items[j], items[i]
}

type Node struct {
	value int
	items Items
}

func Solve(items Items, capacity int) (int, Items) {
	sort.Sort(items)

	m := make([]Node, capacity+1)
	for i := 0; i < len(m); i++ {
		m[i] = Node{0, make(Items, 0)}
	}

	for _, item := range items {
		for w := capacity; w >= item.weight; w-- {
			prev := m[w-item.weight]
			if prev.value+item.value > m[w].value {
				m[w] = Node{prev.value + item.value, append(prev.items, item)}
			}
		}
	}

	sort.Sort(m[capacity].items)
	return m[capacity].value, m[capacity].items
}

func ReadInput(filename string) (items Items, capacity int, err error) {
	f, err := os.Open(filename)
	if err != nil {
		return nil, 0, err
	}
	defer f.Close()

	items = make(Items, 0)
	capacity = 0

	r := bufio.NewReader(f)

	line, err := r.ReadString('\n')
	if err != nil {
		return nil, 0, err
	}
	if _, err = fmt.Sscanf(line, "%d", &capacity); err != nil {
		return nil, 0, err
	}

	line, err = r.ReadString('\n')
	for err == nil {
		item := new(Item)
		if _, err = fmt.Sscanf(line, "%s%d%d", &item.name, &item.value, &item.weight); err != nil {
			return nil, 0, err
		}
		items = append(items, item)
		line, err = r.ReadString('\n')
	}
	if err != io.EOF {
		return nil, 0, err
	}

	return items, capacity, nil
}

func usage() {
	fmt.Fprintf(os.Stderr, "usage: %s [inputfile]\n", os.Args[0])
	flag.PrintDefaults()
	os.Exit(2)
}

func main() {
	flag.Usage = usage
	flag.Parse()

	args := flag.Args()
	if len(args) < 1 {
		fmt.Fprintf(os.Stderr, "input file is missing\n")
		os.Exit(1)
	}

	items, capacity, err := ReadInput(args[0])
	if err != nil {
		fmt.Fprintf(os.Stderr, "input error: %v\n", err)
		os.Exit(1)
	}

	maxValue, knapsackItems := Solve(items, capacity)
	fmt.Printf("%d\n", maxValue)
	for _, item := range knapsackItems {
		fmt.Printf("%v\n", item)
	}
}
