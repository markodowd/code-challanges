package kata

import "fmt"

func MultiTable(number int) string {
	multiplicationTable := ""

	for i := 1; i <= 10; i++ {
		value := i * number

		if i == 10 {
			multiplicationTable += fmt.Sprintf("%d * %d = %d", i, number, value)
		} else {
			multiplicationTable += fmt.Sprintf("%d * %d = %d\n", i, number, value)
		}
	}

	return multiplicationTable
}
