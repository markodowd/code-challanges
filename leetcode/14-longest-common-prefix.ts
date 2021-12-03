function longestCommonPrefix(strs: string[]): string {
  return strs.reduce((prev, next) => {
    let i = 0;

    for (i; i <= 200; i++) {
      if (prev[i] && next[i] && prev[i] === next[i]) {
        continue;
      } else {
        break;
      }
    }

    return prev.slice(0, i);
  });
}
