/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
  /* If this function is invoked before delay of t s, 
  cancel the execution of the given function */
  const timer = setTimeout(fn, t, ...args) // executed only once
  return function() {
      clearTimeout(timer)
  }
};

/**
*  const result = [];
*
*  const fn = (x) => x * 5;
*  const args = [2], t = 20, cancelTimeMs = 50;
*
*  const start = performance.now();
*
*  const log = (...argsArr) => {
*      const diff = Math.floor(performance.now() - start);
*      result.push({"time": diff, "returned": fn(...argsArr)});
*  }
*       
*  const cancel = cancellable(log, args, t);
*
*  const maxT = Math.max(t, cancelTimeMs);
*           
*  setTimeout(cancel, cancelTimeMs);
*
*  setTimeout(() => {
*      console.log(result); // [{"time":20,"returned":10}]
*  }, maxT + 15)
*/