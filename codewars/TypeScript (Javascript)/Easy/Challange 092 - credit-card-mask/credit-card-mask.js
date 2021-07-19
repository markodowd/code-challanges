const maskify = (cc) =>
  cc.length >= 4
    ? cc.replace(cc.slice(0, cc.length - 4), "#".repeat(cc.length - 4))
    : cc;
