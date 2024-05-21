/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
  let counter = n
  let isCalled = false
  return function() {
      if (isCalled) {
          counter += 1
      } else {
          isCalled = true
      }
      return counter
  };
};

/** 
* const counter = createCounter(10)
* counter() // 10
* counter() // 11
* counter() // 12
*/