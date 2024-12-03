package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Part interface {
	Solve(input []string) int
}

type Part1 struct{}
type Part2 struct{}

func LoadFile() []string {
	var filePath string

	if len(os.Args) > 2 && os.Args[2] == "t" {
		filePath = "./input.test.txt"
	} else {
		filePath = "./input.txt"
	}

	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Cannot load file:", err)
		return nil
	}
	defer file.Close()

	lines := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

func All(arr []any, value any) bool {
	for _, v := range arr {
		if v != value {
			return false
		}
	}
	return true
}

func ArrayNumberFromString(input string) []int {
	strArr := strings.Split(input, " ")
	numArr := make([]int, len(strArr))
	for i, v := range strArr {
		numArr[i], _ = strconv.Atoi(v)
	}
	return numArr
}

func RemoveArrayItem[T any](arr []T, index int) []T {
	if index < 0 || index >= len(arr) {
		return arr
	}
	newArr := make([]T, len(arr)-1)
	copy(newArr, arr[:index])
	copy(newArr[index:], arr[index+1:])
	return newArr
}

func MakeRange(min, max int) []int {
	arr := make([]int, max-min+1)
	for i := range arr {
		arr[i] = min + i
	}
	return arr
}
