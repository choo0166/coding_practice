/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  const helper = function(arr, index, acc) {
      if (index < arr.length) {
          return helper(arr, index + 1, fn(acc, arr[index]))
      } else {
          return acc
      }
  }
  return helper(nums, 0, init)
};

