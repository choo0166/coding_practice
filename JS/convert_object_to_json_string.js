/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
  if (Array.isArray(object)) {
      if (object.length === 0) {
          return "[]"
      }
      return object.reduce((acc, e, i) => {
          if (i === object.length-1) {
              acc += jsonStringify(e) + "]"
          } else {
              acc += jsonStringify(e) + ","
          }
          return acc
      }, "[")
  } else if (typeof(object) === "object" && object) {
      const objKeys = Object.keys(object)
      if (objKeys.length === 0) {
          return "{}"
      }
      return objKeys.reduce((acc, e, i) => {
          if (i === objKeys.length-1) {
              acc += `"${e}":` + jsonStringify(object[e]) + "}"
          } else {
              acc += `"${e}":` + jsonStringify(object[e]) + ","
          }
          return acc
      }, "{")
  } else if (typeof(object) === "string") {
      return `"${object}"`
  } else {
      return String(object)
  }
};