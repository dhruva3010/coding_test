function shallowCopy(obj) {
    return { ...obj };
}

function deepCopy(obj) {
    return JSON.parse(JSON.stringify(obj));
}

const obj = { a: 1, b: { c: 2 } };
const shallow = shallowCopy(obj);
const deep = deepCopy(obj);

console.log(shallow); // { a: 1, b: { c: 2 } }
console.log(deep);    // { a: 1, b: { c: 2 } }
