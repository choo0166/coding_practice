/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function (o1, o2) {
  if (Array.isArray(o1) && Array.isArray(o2)) {
      // arrays should have equal length
      if (o1.length !== o2.length) {
          return false
      } else {
          for (let i = 0; i < o1.length; i++) {
              if (!areDeeplyEqual(o1[i], o2[i])) {
                  return false
              }
          }
      }
  } else if (typeof (o1) === "object" && typeof (o2) === "object") {
      /* objects should have the same key value pair
      Note: null is considered object 
      */
      if (Array.isArray(o1) || Array.isArray(o2)) {
          return false
      }
      if (o1 === null || o2 === null || o1 === undefined || o2 === undefined) {
          return o1 === o2
      }
      if (Object.keys(o1).length !== Object.keys(o2).length) {
          return false
      } else {
          for (const key in o1) {
              if (!areDeeplyEqual(o1[key], o2[key])) {
                  return false
              }
          }
      }
  } else if (!(o1 === o2)) {
      // comparison of primitive types
      return false
  }
  return true
};