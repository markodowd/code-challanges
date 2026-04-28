function minMoves(nums: number[]): number {
	let total = 0

	const max_val = Math.max(...nums)

	for (let num of nums) {
		total += (max_val - num)
	}

	return total
};
