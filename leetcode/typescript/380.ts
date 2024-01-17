class RandomizedSet {
  a = []

  constructor() {
    this.a = []
  }

  insert(v) {
    if (this.a.includes(v)) return false
    this.a.push(v)
    return true
  }

  remove(v) {
    if (!this.a.includes(v)) return false
    const i = this.a.indexOf(v)
    const l = this.a[this.a.length - 1]
    this.a[i] = l
    this.a.pop()
    return true
  }

  getRandom() {
    return this.a[Math.floor(Math.random() * this.a.length)]
  }
}
