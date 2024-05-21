/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
  return {
      toBe: function(val2) {
          const res = val === val2
          if (!res) {
              throw new Error("Not Equal")
          }
          return res
      },
      notToBe: function(val2) {
          const res = val !== val2
          if (!res) {
              throw new Error("Equal")
          }
          return res
      }
  }
};

/**
* expect(5).toBe(5); // true
* expect(5).notToBe(5); // throws "Equal"
*/