package kata

import (
	"math"
)

func BinToDec(bin string) int {
	l := len(bin) - 1
	total := 0

	for i := 0; i <= l; i++ {
		digit := int(bin[i] - '0')
		power := l - i
		total += digit * int(math.Pow(2, float64(power)))
	}

	return total
}
