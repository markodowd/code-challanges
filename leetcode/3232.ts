function canAliceWin(nums: number[]): boolean {
	let singleTracker = 0;
	let doubleTracker = 0;

	for (const num of nums) {
		if (num < 10) {
			singleTracker += num;
		} else {
			doubleTracker += num;
		}
	}

	return !(singleTracker === doubleTracker)
};
