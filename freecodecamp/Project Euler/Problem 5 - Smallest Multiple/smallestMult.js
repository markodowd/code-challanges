function smallestMult(n) {
  //LCM of two numbers
  //https://wikimedia.org/api/rest_v1/media/math/render/svg/86f8023906e6ba7fce03049c576fa8c25a137ceb
  var lcm = function (a, b) {
    return (a / gcd(a, b)) * b;
  };
  //Euclidean recursive algorithm
  var gcd = function (a, b) {
    return b === 0 ? a : gcd(b, a % b);
  };
  var maxLCM = 1;
  //Getting the LCM in the range
  for (var i = 2; i <= n; i++) {
    maxLCM = lcm(maxLCM, i);
  }
  return maxLCM;
}
smallestMult(20);
