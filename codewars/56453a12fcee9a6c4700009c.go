package kata

import "math"

func CloseCompare(a, b, margin float64) int {
	if margin >= math.Abs(a-b) {
		return 0
	}

	if a > b {
		return 1
	}

	return -1
}
