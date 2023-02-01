function fair(arr, separator) {
    let expected = "";
    for (var i = 0; i < arr.length; i++) {
        if (i < arr.length - 1) {
            expected = expected + arr[i] + separator;
        } else {
            expected += arr[i];
        }
    }
    return expected;
}

console.log(fair([1,2,3],","))