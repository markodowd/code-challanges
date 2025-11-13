function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    let answer = []

    for (let i = 0; i < arr.length; i++) {
        answer.push(fn(arr[i], i))
    }

    return answer
};
