package main

import (
	"fmt"
	"math"
	"os"
)

func main() {
	// max := 0
	numbers := []int{}
	for {
		var input int
		_, err := fmt.Fscan(os.Stdin, &input)
		if err != nil {
			break
		}
		numbers = append(numbers, input)

		avg := Average(numbers)
		dev := Deviation(numbers)
		fmt.Printf("%d %d\n", int(math.Abs(float64(avg-dev))), avg+dev)
	}
}
func Variance(nbr []int) int {
	avg := Average(nbr)
	var s int
	for _, v := range nbr {
		s += (int(v) - avg) * (int(v) - avg)
	}
	return s / int(len(nbr))
}
func Deviation(nbr []int) int {
	v := math.Sqrt(float64(Variance(nbr)))
	return int(v)
}
func Average(nbr []int) int {
	var sum int
	for _, v := range nbr {
		sum += v
	}
	return int(sum / len(nbr))
}
