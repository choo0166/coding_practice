/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {

  return new Promise((resolve, reject) => {
      /* Using Promise.all
      // const promises = functions.map(f => { return f() })
      // Promise.all(promises).then(res => resolve(res)).catch(err => reject(err))
      */
      let resolveCount = 0
      const promises = functions.map((f, index) => {
          return f()
          .then(res => {
              // set callback to push resolved value to correct index
              promises[index] = res
              resolveCount += 1
          })
          .catch(err => reject(err))
          .finally(() => {
              // checks if all promises are fulfilled each time a promise is settled
              if (resolveCount === functions.length) {
                  resolve(promises)
              }
          })
      })
  })
};

/**
* const promise = promiseAll([() => new Promise(res => res(42))])
* promise.then(console.log); // [42]
*/