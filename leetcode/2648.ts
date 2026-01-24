function* fibGenerator(): Generator<number, any, number> {
    let prev = 0;
    let curr = 1;

    yield prev;
    yield curr;

    while (true) {
        const next = prev + curr;

        yield next;
        
        prev = curr;
        curr = next;
    }
}
