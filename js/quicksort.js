function quicksort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const pivot = arr[Math.floor(arr.length / 2)];
    const left = [];
    const middle = [];
    const right = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i]);
        } else if (arr[i] > pivot) {
            right.push(arr[i]);
        } else {
            middle.push(arr[i]);
        }
    }

    return [...quicksort(left), ...middle, ...quicksort(right)];
}

console.log(quicksort([3, 6, 8, 10, 1, 2, 1]));

// Output: [1, 1, 2, 3, 6, 8, 10]
