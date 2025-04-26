package kata

func multipleOfIndex(ints []int) []int {
	arr := []int{ints[1]}

	for i := 2; i < len(ints); i++ {
		if ints[i]%i == 0 {
			arr = append(arr, ints[i])
		}
	}

	return arr
}
