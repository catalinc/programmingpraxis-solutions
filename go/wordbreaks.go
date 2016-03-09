/*
 * Problem description is located at
 * http://programmingpraxis.com/2011/08/12/word-breaks/
 */

package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
)

func loadDict(fname string) map[string]bool {
	f, err := os.Open(fname)
	if err != nil {
		fmt.Printf("error opening %s (%v)\n", fname, err)
		os.Exit(1)
	}
	defer f.Close()

	dict := make(map[string]bool)

	r := bufio.NewReader(f)
	line, _, err := r.ReadLine()
	dict[string(line)] = true
	for err == nil {
		line, _, err = r.ReadLine()
		dict[string(line)] = true
	}

	return dict
}

func wordBreaks(s string, dict map[string]bool) string {
	if dict[s] {
		return s
	}
	for i := 2; i < len(s); i++ {
		prefix := s[0:i]
		suffix := s[i:len(s)]
		if dict[prefix] {
			return prefix + " " + wordBreaks(suffix, dict)
		}
	}
	return ""
}

var dictFile = flag.String("dict", "words.lst", "dictionary file")
var word = flag.String("word", "", "word to break")

func main() {
	flag.Parse()
	if len(*word) == 0 {
		fmt.Printf("input word is missing\n")
		os.Exit(1)
	}
	dict := loadDict(*dictFile)
	fmt.Printf("%s -> %s\n", *word, wordBreaks(*word, dict))
}
