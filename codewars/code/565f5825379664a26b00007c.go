package kata

func GetSize(w, h, d int) [2]int {
	surfaceArea := 2 * (w*h + w*d + h*d)
	volume := w * h * d

	return [2]int{surfaceArea, volume}
}
