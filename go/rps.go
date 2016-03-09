/*
 * Rock - Paper - Scissors Game
 *
 * This implementation uses history string matching strategy.
 * See http://dllu.net/rps.html for more details.
 */

package main

import (
	"fmt"
	"strings"
	"os"
	"bufio"
	"rand"
	"bytes"
)

var combine = map[string]string{
	"PP": "1",
	"PR": "2",
	"PS": "3",
	"RP": "4",
	"RS": "5",
	"RR": "6",
	"SS": "7",
	"SP": "8",
	"SR": "9"}

var split = map[string]string{
	"1": "PP",
	"2": "PR",
	"3": "PS",
	"4": "RP",
	"5": "RS",
	"6": "RR",
	"7": "SS",
	"8": "SP",
	"9": "SR"}

var anti = map[string]string{
	"P": "S",
	"R": "P",
	"S": "R"}

func Input(prompt string) string {
	fmt.Printf("%s: ", prompt)
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Printf("input error %v", err)
		os.Exit(1)
	}
	return strings.TrimSpace(input)
}

func RandomMove() string {
	moves := []string{"R", "P", "S"}
	return moves[rand.Intn(len(moves))]
}

func Move(history string) string {
	hlen := len(history)
	if hlen == 0 {
		return RandomMove()
	}
	for i := Min(20, hlen-1); i > 0; i-- {
		search := history[hlen-i : hlen]
		if idx := strings.Index(history, search); idx > 0 {
			answered := string(history[idx+i-1])
			expected := string(split[answered][1])
			return anti[expected]
		}
	}
	return RandomMove()
}

func Min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func Score(myMove, userMove string) {
	fmt.Printf("Me -> %s You -> %s\n", myMove, userMove)
	if anti[myMove] == userMove {
		fmt.Printf("You win\n")
	} else if anti[userMove] == myMove {
		fmt.Printf("You lose\n")
	} else {
		fmt.Printf("Tie\n")
	}
}

func GameLoop() {
	history := bytes.NewBufferString("")
	for {
		userMove := Input("Your move ? (R)ock (P)aper (S)cissors or (Q)uit")
		userMove = strings.ToUpper(userMove)
		switch userMove {
		case "R", "P", "S":
			myMove := Move(string(history.Bytes()))
			Score(myMove, userMove)
			fmt.Fprint(history, combine[myMove+userMove])
		case "Q":
			fmt.Printf("Bye\n")
			os.Exit(0)
		default:
			fmt.Printf("invalid move\n")
		}
	}
}

func main() {
	GameLoop()
}
