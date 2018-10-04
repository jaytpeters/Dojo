function resetNegatives(arr) {
    for(var i = 0; i < arr.length; i++)
        arr[i] = (arr[i] < 0) ? 0 : arr[i];
    return arr;
}

function moveForward(arr) {
    for(var i = 0; i < arr.length-1; i++)
        arr[i] = arr[i+1];
    arr[i] = 0;
    return(arr);
}

function returnReversed(arr) {
    var temp = null;

    for(i = 0; i < arr.length/2; i++) {
        temp = arr[arr.length-i-1];
        arr[arr.length-i-1] = arr[i];
        arr[i] = temp;
    }

    return arr;
}

function repeatTwice(arr) {
    var newArr = [];

    for(var i = 0; i < arr.length; i++)
        newArr.push(arr[i], arr[i]);        
    
    return newArr;
}