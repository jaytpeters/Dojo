function maximum(arr) {
    if(arr === undefined || arr.length == 0)
        return null;

    var max = arr[0];
    for(var i = 1; i < arr.length; i++) {
        max = arr[i] > max ? arr[i];
    }

    return max;
}