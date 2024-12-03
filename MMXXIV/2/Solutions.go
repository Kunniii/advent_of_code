package main

import (
	"fmt"
	"math"
)

func (p Part1) Solve(input []string) int {
	safes := 0

	for _, line := range input {
		numbers := ArrayNumberFromString(line)
		ok := make([]any, 0)
		flow := (numbers[0] - numbers[1]) > 0
		fmt.Printf("numbers: %v\n", numbers)
		for i := 0; i < len(numbers)-1; i++ {
			if (numbers[i]-numbers[i+1] > 0) == flow {
				diff := math.Abs(float64((numbers[i] - numbers[i+1])))
				ok = append(ok, 1 <= diff && diff <= 3)
			} else {
				ok = append(ok, false)
				break
			}
		}
		if All(ok, true) {
			safes++
		}
	}

	return safes
}

func (p Part2) Solve(input []string) int {
	safes := 0
	for _, line := range input {
		numbers := ArrayNumberFromString(line)
		if checkSafe(numbers) {
			safes++
		} else if tryToMakeSafe(numbers) {
			safes++
		}
	}
	return safes
}

func checkSafe(array []int) bool {
	ok := make([]any, 0)
	flow := (array[0] - array[1]) > 0
	fmt.Printf("array: %v\n", array)
	for i := 0; i < len(array)-1; i++ {
		if (array[i]-array[i+1] > 0) == flow {
			fmt.Printf("diff: %v\n", array[i]-array[i+1])
			diff := math.Abs(float64((array[i] - array[i+1])))
			ok = append(ok, 1 <= diff && diff <= 3)
		} else {
			ok = append(ok, false)
			break
		}
	}
	return All(ok, true)
}

func tryToMakeSafe(array []int) bool {
	index := MakeRange(0, len(array))

	for _, i := range index {
		arr := make([]int, len(array))
		copy(arr, array)
		fmt.Printf("Before %v\n", arr)
		arr = RemoveArrayItem(arr, i)
		fmt.Printf("After %v\n", arr)
		if checkSafe(arr) {
			return true
		}
	}
	return false
}
