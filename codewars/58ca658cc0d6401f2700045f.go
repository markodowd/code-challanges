package kata

func FindMultiples(integer, limit int) []int {
	arr := []int{integer}

	multiplier := 2
	total := 0

	for {
		total = integer * multiplier

		if total > limit {
			break
		}

		arr = append(arr, total)
		multiplier += 1
	}

	return arr
}
