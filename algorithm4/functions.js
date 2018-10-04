function arrayValsLargerThan(arr, Y)
{
    var count = 0;

    for(var i = 0; i < arr.length; i++) {
        if(arr[i] > Y)
            count++;
    }

    console.log("# of values larger than Y: " + count);
}

function arrayMinMaxAvg(arr) {
    var min = arr[0];
    var max = arr[0];
    var sum = 0;

    for(var i = 0; i < arr.length; i++) {
        min = (arr[i] < min) ? arr[i] : min;
        max = (arr[i] > max) ? arr[i] : max;
        sum += arr[i];
    }

    console.log("Min: " + min + ", Max: " + max + ", Avg: " + sum/arr.length);
}

function arrayReplaceNegativeWithDojo(arr) {
    var newArray = [];
    for(var i = 0; i < arr.length; i++)
        arr[i] < 0 ? newArray.push("Dojo") : newArray.push(arr[i]);
    return newArray;
}

function arrayRemoveValsAt(arr, indexStart, indexEnd) {
    for(var i = indexEnd; i >= indexStart; i--) {
        if(i == arr.length - 1) {
            arr.pop();
            continue;
        }

        for(var j = i; j < arr.length - 1; j++)
            arr[j] = arr[j+1];

        arr.pop();
    }
    return arr;
}