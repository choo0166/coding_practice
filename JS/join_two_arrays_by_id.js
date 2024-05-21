/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
  const comparator = (a, b) => {
      return a.id - b.id
  }
  const newArr = []
  // Sort input arrays by object id
  arr1.sort(comparator)
  arr2.sort(comparator)

  let [i, j] = [0, 0]
  /* Iterate over both arrays until one is exhausted, 
  pushing each object in sorted order of their ids. If
  two objects share ids, include the unique key-value
  pairs of the object in the first array to the object
  in the second array */
  while (i < arr1.length && j < arr2.length) {
      const [e1, e2] = [arr1[i], arr2[j]]
      if (e1.id === e2.id) {
          const diff = Object.keys(e1).reduce((acc, key) => {
              if (!(key in e2)) {
                  acc[key] = e1[key]
              }
              return acc
          }, {})
          newArr.push(Object.assign(e2, diff))
          i++; j++
      } else if (e1.id < e2.id) {
          newArr.push(e1)
          i++
      } else {
          newArr.push(e2)
          j++
      }
  }
  // Push remaining elements of the non-exhausted array
  // console.log(newArr)
  if (i === arr1.length) {
      arr2.slice(j, arr2.length).forEach(e => {newArr.push(e)})
  } else if (j === arr2.length) {
      arr1.slice(i, arr1.length).forEach(e => {newArr.push(e)})
  }
  return newArr
};