const number = (busStops) =>
  busStops.map((val) => val[0] - val[1]).reduce((acc, val) => acc + val);
