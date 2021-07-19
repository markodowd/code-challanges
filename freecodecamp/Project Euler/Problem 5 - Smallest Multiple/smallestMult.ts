function smallestMult(n: number) {
  //LCM of two numbers
  //https://wikimedia.org/api/rest_v1/media/math/render/svg/86f8023906e6ba7fce03049c576fa8c25a137ceb
  const lcm = (a: number, b: number) => (a / gcd(a, b)) * b;

  //Euclidean recursive algorithm
  const gcd = (a: number, b: number) => (b === 0 ? a : gcd(b, a % b));

  let maxLCM = 1;

  //Getting the LCM in the range
  for (let i = 2; i <= n; i++) {
    maxLCM = lcm(maxLCM, i);
  }
  return maxLCM;
}

smallestMult(20);
