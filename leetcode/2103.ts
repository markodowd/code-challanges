enum Color {
	Red = 'R',
	Green = 'G',
	Blue = 'B'
}

function countPoints(rings: string): number {
	const rodMap: Record<string, string> = {};

	for (let i = 0; i < rings.length; i += 2) {
		const color = rings[i];
		const rod = rings[i + 1];

		rodMap[rod] = (rodMap[rod] ?? "") + color;
	}

	let count = 0;

	for (const rod in rodMap) {
		const colorsOnRod = rodMap[rod];

		const hasRed = colorsOnRod.includes(Color.Red);
		const hasGreen = colorsOnRod.includes(Color.Green);
		const hasBlue = colorsOnRod.includes(Color.Blue);

		if (hasRed && hasGreen && hasBlue) {
			count++;
		}
	}

	return count;
}
