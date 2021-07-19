const validatePIN = (pin) =>
  pin == pin.match(/\d{4}/) || pin == pin.match(/\d{6}/);
