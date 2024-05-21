/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {

  const helper = function(arr, index, acc) {
      if (index < 0) {
          return acc
      } else {
          return helper(arr, index - 1, functions[index](acc))
      }
  }

  return function (x) {
      if (functions.length === 0) {
          return x
      }
      return helper(functions, functions.length-1, x)
  }
};

/**
* const fn = compose([x => x + 1, x => 2 * x])
* fn(4) // 9
*/