/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
  if (arr.length === 0) {
      return arr
  }
  const newArr = []
  let i = 0
  while (i + size < arr.length) {
      newArr.push(arr.slice(i, i + size))
      i += size
  }
  newArr.push(arr.slice(i, arr.length))
  return newArr
};
