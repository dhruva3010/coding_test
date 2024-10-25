function uniqueElements(arr1, arr2) {
    //create set from arr1
    const set1 = new Set(arr1);
    //add unique elemts from arr2
    for (const element of arr2) {
      set1.add(element);
    }
  
    //create set from arr2
    const set2 = new Set(arr2);
  
    //create result set
    const uniqueElemets = new Set();
  
    for (const element of set1) {
      if (!set2.has(element)) {
        uniqueElemets.add(element);
      }
    }
    return [...uniqueElemets];
  }
  
  //get only unique elements in 2 arrays
  const arr1 = [1, 3, 5, 7, 9];
  const arr2 = [1, 3, 5, 7];
  alert("Unique element in 2 arrays are " + uniqueElements(arr1, arr2));
  