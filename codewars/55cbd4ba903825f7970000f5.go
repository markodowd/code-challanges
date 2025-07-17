package kata

func GetGrade(a, b, c int) rune {
	var average int = (a + b + c) / 3

	switch {
	case average >= 90:
		return 'A'
	case average >= 80:
		return 'B'
	case average >= 70:
		return 'C'
	case average >= 60:
		return 'D'
	default:
		return 'F'
	}
}
