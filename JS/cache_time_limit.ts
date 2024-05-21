class TimeLimitedCache {
  private cache: object
  private keyCount: number

  constructor() {
      this.cache = {}
      this.keyCount = 0
  }

  set(key: number, value: number, duration: number): boolean {
      if (key in this.cache) {
          // clear existing expiry timer
          const [v, t] = this.cache[key]
          clearTimeout(t)
          // update key value
          this.cache[key] = [value, setTimeout((key) => {delete this.cache[key]; this.keyCount -= 1}, duration, key)]
          return true
      } else {
          this.cache[key] = [value, setTimeout((key) => {delete this.cache[key]; this.keyCount -= 1}, duration, key)]
          this.keyCount += 1
          return false
      }
  }
  
  get(key: number): number {
      if (key in this.cache) {
          return this.cache[key][0]
      } else {
          return -1
      }
      
  }
  
  count(): number {
      return this.keyCount
  }
}

/**
* const timeLimitedCache = new TimeLimitedCache()
* timeLimitedCache.set(1, 42, 1000); // false
* timeLimitedCache.get(1) // 42
* timeLimitedCache.count() // 1
*/