/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function (fn) {

  /* Idea: Get the number of arguments the function expects,
  collect the arguments from the curried function, if the 
  number of arguments matches the expected number, then call
  the function and returns the result, otherwise returns the
  curried function */
  const expected = fn.length
  const allArgs = []
  return function curried(...args) {
      allArgs.push(...args)
      if (allArgs.length < expected) {
          return curried
      }
      return fn(...allArgs)
  }
};

/**
* function sum(a, b) { return a + b; }
* const csum = curry(sum);
* csum(1)(2) // 3
*/
