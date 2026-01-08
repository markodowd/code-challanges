type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
  let chunk = [];
  let tempArr = [];
  let count = 0;

  while (arr.length > 0) {
    const firstElement = arr.shift();
    tempArr.push(firstElement);
    count++;

    if (count === size) {
      chunk.push(tempArr);
      tempArr = [];
      count = 0;
    }
  }

  if (tempArr.length > 0) {
    chunk.push(tempArr);
  }

  return chunk;
}

