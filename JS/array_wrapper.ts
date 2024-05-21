class ArrayWrapper {
  private v: number[]

  constructor(nums: number[]) {
      this.v = nums
  }
  
  valueOf(): number {
      return this.v.reduce((x, y) => { return x + y }, 0)
  }
  
  toString(): string {
      let s = "["
      for (let i=0; i<this.v.length; i++) {
          if (i === this.v.length-1) {
              s = s.concat(this.v[i].toString())
          }
          else {
              s = s.concat(this.v[i].toString() + ",")
          }
      }
      return s.concat("]")
  }
};

/**
* const obj1 = new ArrayWrapper([1,2]);
* const obj2 = new ArrayWrapper([3,4]);
* obj1 + obj2; // 10
* String(obj1); // "[1,2]"
* String(obj2); // "[3,4]"
*/