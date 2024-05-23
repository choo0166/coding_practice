/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
  let pending = 0
  const results = Array.from(Array(functions.length))
  // initialize initial pool of n pending promises
  const pool = functions.slice(0, n).map((f, index) => {
      pending += 1
      return f()
      .then(res => { results[index] = res; pool[index] = "resolved"; pending -= 1 })
  })
  for (let i=n; i<functions.length; i++) {
      if (pending === n) {
          // n pending promises, wait for one to resolve
          // console.log("waiting")
          await Promise.race(pool.filter(e => e !== "resolved"))
      }
      pool.push(functions[i]().then(res => { results[i] = res; pool[i] = "resolved"; pending -= 1 }))
      pending += 1
  }
  
  await Promise.all(pool) // wait for all promises to resolve
  return results
};

/**
* const sleep = (t) => new Promise(res => setTimeout(res, t));
* promisePool([() => sleep(500), () => sleep(400)], 1)
*   .then(console.log) // After 900ms
*/