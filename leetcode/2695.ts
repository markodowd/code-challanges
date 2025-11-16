// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

class ArrayWrapper {
    private nums: number[]

    constructor(nums: number[]) {
        this.nums = nums
    }

    valueOf(): number {
        return this.nums.reduce((a,b) => a + b, 0)
    }

    toString(): string {
        return `[${this.nums.join(',')}]`
    }
}
