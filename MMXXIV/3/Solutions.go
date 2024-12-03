package main

import (
	"regexp"
	"strconv"
	"strings"
)

func mul(s string) int {
	s = s[4 : len(s)-1]
	a := strings.Split(s, ",")
	n1, _ := strconv.Atoi(a[0])
	n2, _ := strconv.Atoi(a[1])
	return n1 * n2
}

func (p Part1) Solve(input []string) int {
	total := 0
	pattern := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)`)

	for _, line := range input {
		bytesLine := []byte(line)
		if match := pattern.FindAll(bytesLine, -1); len(match) > 0 {
			for _, m := range match {
				total += mul(string(m))
			}
		}
	}

	return total
}

func (p Part2) Solve(input []string) int {
	pattern := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)`)
	total := 0
	skip := false
	for _, line := range input {
		bytesLine := []byte(line)
		if match := pattern.FindAll(bytesLine, -1); len(match) > 0 {
			for _, m := range match {
				s := string(m)
				if s == "don't()" {
					skip = true
				} else if s == "do()" {
					skip = false
				}
				if skip {
					continue
				}
				if strings.HasPrefix(s, "mul") {
					total += mul(s)
				}
			}
		}
	}
	return total
}
