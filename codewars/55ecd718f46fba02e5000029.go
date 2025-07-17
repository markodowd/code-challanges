package kata

func Between(a, b int) []int {
	arr := []int{}

	for a <= b {
		arr = append(arr, a)
		a++
	}

	return arr
}
