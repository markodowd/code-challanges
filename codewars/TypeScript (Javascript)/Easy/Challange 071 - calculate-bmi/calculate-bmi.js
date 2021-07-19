function bmi(weight, height) {
  const value = weight / height ** 2;

  if (value <= 18.5) {
    return "Underweight";
  } else if (value <= 25.0) {
    return "Normal";
  } else if (value <= 30.0) {
    return "Overweight";
  } else {
    return "Obese";
  }
}
