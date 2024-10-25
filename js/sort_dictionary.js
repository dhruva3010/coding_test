function sortDictionary(dictionary) {
    // Convert dictionary to array of key-value pairs
    const entries = Object.entries(dictionary);
    
    // Sort the array based on values
    entries.sort((a, b) => {
        if (typeof a[1] === 'string' && typeof b[1] === 'string') {
            return a[1].localeCompare(b[1]);
        } else {
            return a[1] - b[1];
        }
    });
    
    // Convert sorted array back to dictionary
    return Object.fromEntries(entries);
}

// Example usage
const unsortedDict = {
    'banana': 3,
    'apple': 1,
    'cherry': 2,
    'date': 4
};

console.log("Unsorted dictionary:", unsortedDict);
console.log("Sorted dictionary:", sortDictionary(unsortedDict));
