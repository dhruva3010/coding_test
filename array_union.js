function union(arr1, arr2) {
    //create set from arr1
    const set1 = new Set(arr1);

    //append 2nd array to set1
    for(const element of arr2) {
        set1.add(element)
    };

    return [...set1]
}

const arr1 = [1, 5, 7];
const arr2 = [1, 4, 3];
console.log(union(arr1, arr2))