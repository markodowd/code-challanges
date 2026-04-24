function mergeArrays(nums1: number[][], nums2: number[][]): number[][] {
    let trackingMap: Record<number, number> = {}

    for (let [id, val] of nums1) {
        trackingMap[id] = val
    }

    for (let [id, val] of nums2) {
        trackingMap[id] = (trackingMap[id] || 0) + val;
    }

    const result = Object.entries(trackingMap).map(
        ([key, value]) => [Number(key), value]
    );

    return result
};
