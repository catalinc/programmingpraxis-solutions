/*
 * Compute longest common subsequence of two strings
 */
package main

import (
	"fmt"
	"os"
	"strings"
)

func Lcs(s1, s2 string) string {
	m := make([][]int, len(s1)+1)
	for i := 0; i < len(s1)+1; i++ {
		m[i] = make([]int, len(s2)+1)
	}

	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[i]); j++ {
			if i == 0 || j == 0 {
				m[i][j] = 0
			}
		}
	}

	for i := 1; i < len(s1)+1; i++ {
		for j := 1; j < len(s2)+1; j++ {
			if s1[i-1] == s2[j-1] {
				m[i][j] = m[i-1][j-1] + 1
			} else {
				m[i][j] = max(m[i][j-1], m[i-1][j])
			}
		}
	}

	i := len(s1)
	j := len(s2)
	seq := make([]string, 0)
	for i > 0 && j > 0 {
		if m[i][j] > m[i-1][j-1] {
			seq = append(seq, string(s1[i-1]))
		}
		if i == j {
			i--
			j--
		} else if i > j {
			i--
		} else {
			j--
		}
	}

	reverse(seq)
	return strings.Join(seq, "")
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func reverse(seq []string) {
	for i := 0; i < len(seq)/2; i++ {
		seq[i], seq[len(seq)-1-i] = seq[len(seq)-1-i], seq[i]
	}
}

func main() {
	if len(os.Args) != 3 {
		fmt.Printf("usage: %s string1 string2\n", os.Args[0])
		os.Exit(1)
	}
	fmt.Printf("%s\n", Lcs(os.Args[1], os.Args[2]))
}
