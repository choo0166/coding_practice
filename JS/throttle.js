/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function (fn, t) {

  let currArgs = null
  let timer = null
  const timeout = () => {
      if (currArgs) {
          fn(...currArgs)
          currArgs = null
          // previous timeout done, create new timeout
          timer = setTimeout(timeout, t)
      } else {
          timer = null
      }
  }
  return function (...args) {
      if (!timer) {
          fn(...args)
          timer = setTimeout(timeout, t)
      } else {
          // function called during delay period, set new arguments
          currArgs = args
      }
  }
};

/**
* const throttled = throttle(console.log, 100);
* throttled("log"); // logged immediately.
* throttled("log"); // logged at t=100ms.
*/