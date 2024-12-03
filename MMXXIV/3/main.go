package main

import (
	"fmt"
	"os"
)

func main() {
	var part Part
	if len(os.Args) > 1 && os.Args[1] == "p1" {
		part = Part1{}
	} else {
		part = Part2{}
	}

	if inp := LoadFile(); inp != nil {
		outFile, err := os.Create("output.txt")
		if err != nil {
			fmt.Println(err)
			return
		}
		defer outFile.Close()

		fmt.Fprintln(outFile, part.Solve(inp))
	}
}
