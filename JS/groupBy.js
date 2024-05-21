/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
  const obj = {}
  this.forEach(o => {
      const key = fn(o)
      if (key in obj) {
          obj[key].push(o)
      } else {
          obj[key] = [o]
      }
  })
  return obj
};

/**
* [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
*/