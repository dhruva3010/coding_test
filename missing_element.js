function findMissingElement(arr) {
  const sortedArr = arr.sort();
  for (let i = 0; i < sortedArr.length - 1; i++) {
    if (sortedArr[i + 1] - sortedArr[i] > 1) {
      return sortedArr[i] + 1;
    }
  }
  return null;
}

console.log(findMissingElement([1, 2, 3, 4, 6, 7, 8])); // Output: 5
console.log(findMissingElement([1, 2, 3, 4, 5, 6, 8])); // Output: 7
