function isPalindrome(str) {
  return str.split("").reverse().join("") === str;
}

console.log(isPalindrome("racecar")); // Output: true
console.log(isPalindrome("hello")); // Output: false
