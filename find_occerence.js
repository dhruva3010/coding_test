function countOccurence(str) {
    const counts = {};

    for(const char of str) {
        if(!counts[char]) {
            counts[char] = 1;
        }
        else
        {
            counts[char] += 1;
        }
    }

    let result = '';

    for(const char in counts) {
        result += `${char}${counts[char]}`;
    }

    return result
}

console.log(countOccurence('abaabgh'));