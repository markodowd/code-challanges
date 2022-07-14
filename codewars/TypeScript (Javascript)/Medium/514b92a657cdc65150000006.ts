export class Challenge {
  static solution(number: number) {
    let total: number = 0

    for (let i = 0; i < number; i++) {
      if (i % 3 === 0 || i % 5 === 0) {
        total = total + i
      }
    }
    return total
  }
}
