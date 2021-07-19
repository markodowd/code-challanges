const arrayPlusArray = (arr1, arr2) =>
  [...arr1, ...arr2].reduce((total, value) => total + value);
