type Counter = {
	increment: () => number,
	decrement: () => number,
	reset: () => number,
}

function createCounter(init: number): Counter {
	let original = init;
	let value = init;

	const increment = () => value += 1;
	const decrement = () => value -= 1;
	const reset = () => value = original;

	return { increment, decrement, reset };
};

