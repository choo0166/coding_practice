/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */
function objDiff(obj1, obj2) {
  const helper = (o1, o2, diff) => {
      if (Object(o1) !== o1 && Object(o2) !== o2) {
          // compare primitive types, including null or undefined
          return o1 === o2 ? {} : [o1, o2]
      } 
      else if ((Array.isArray(o1) && !(Array.isArray(o2))) || Array.isArray(o2) && !(Array.isArray(o1))) {
          // compare Array with Object
          return [o1, o2]
      }
      else if (typeof(o1) !== typeof(o2)) {
          // compare primitive type with object type
          return [o1, o2]
      }
      // compare arrays or objects
      const commonKeys = Object.keys(o1).filter(k => k in o2)
      for (const key of commonKeys) {
          const changes = helper(o1[key], o2[key], {})
          if (Array.isArray(changes) || Object.keys(changes).length > 0) {
              diff[key] = changes
          }
      }
      return diff
  }
  return helper(obj1, obj2, {})
};