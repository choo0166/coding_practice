/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
  if (Array.isArray(obj)) {
      return obj.filter(Boolean).map(compactObject)
  }

  if (obj !== Object(obj)) {
      return obj
  }

  return Object.entries(obj).reduce((acc, [k, v]) => {
      acc[k] = compactObject(v)
      if (!Boolean(acc[k])) {
          delete acc[k]
      }
      return acc
  }, {})
};

//[null, 0, false, {"a": null, "b": [false, 1]}]
