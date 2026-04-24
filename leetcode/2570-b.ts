function mergeArrays(nums1: number[][], nums2: number[][]): number[][] {
	const trackingMap = new Map<number, number>();

	for (const [id, val] of nums1) {
		trackingMap.set(id, val);
	}

	for (const [id, val] of nums2) {
		const currentVal = trackingMap.get(id) || 0;
		trackingMap.set(id, currentVal + val);
	}

	return Array.from(trackingMap.entries())
		.sort((a, b) => a[0] - b[0]);
};
