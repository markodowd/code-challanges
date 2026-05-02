function finalString(s: string): string {
	let res: string[] = [];

	for (const char of s) {
		if (char === 'i') {
			res.reverse();
		} else {
			res.push(char);
		}
	}

	return res.join('');
}
