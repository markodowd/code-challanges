function basicOp(operation, value1, value2) {
  var num1 = value1.toString();
  var num2 = value2.toString();

  return eval(num1 + operation + num2);
}
