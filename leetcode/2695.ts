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
