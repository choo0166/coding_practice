/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
  const newArr = []
  arr.forEach((value, index) => {
      if (fn(value, index)) {
          newArr.push(value)
      }
  })
  return newArr
};