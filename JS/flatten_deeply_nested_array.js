/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
  if (n === 0 || arr.length === 0) {
      return arr
  }
  const newArr = []
  const helper = (arr, depth) => {
      arr.forEach(e => {
          if (Array.isArray(e) && depth + 1 <= n) {
              helper(e, depth+1)
          } else {
              newArr.push(e)
          }
      })
  }
  helper(arr, 0)
  return newArr
};