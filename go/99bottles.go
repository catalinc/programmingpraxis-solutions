/*
 *  99 bottles of beer song lyrics
 */
package main

import "fmt"

func main() {
	n := 99
	for n > 0 {
		fmt.Printf("%d bottle(s) of beer on the wall, %d bottle(s) of beer.\n", n, n)
		n--
		fmt.Printf("Take one down and pass it around, %d bottles of beer on the wall.\n", n)
	}
	fmt.Printf("No more bottles of beer on the wall, no more bottles of beer.\n")
	fmt.Printf("Go to the store and buy some more, 99 bottles of beer on the wall.\n")
}
