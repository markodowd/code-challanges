function createCounter(n: number): () => number {
    let count = n
    return function() {
        const val = count
        count += 1
        return val
    }
}


