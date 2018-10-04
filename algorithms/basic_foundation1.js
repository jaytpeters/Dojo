function array_1to255() {
    var arr = [];
    for(var i = 1; i <= 255; i++)
        arr.push(i);
    return arr;
}

function sumEven_1to1000() {
    var sum = 0;
    for(var i = 2; i <= 1000; i+=2)
        sum += i;
    return sum;
}

function sumOdd_1to5000() {
    var sum = 0;
    for(var i = 1; i < 5000; i+= 2)
        sum += i;
    return sum;
}

function sumArray(arr) {
    var sum = 0;
    for(var i = 0; i < arr.length; i++)
        sum += arr[i];
    return sum;
}

function maxValueInArray(arr) {
    var max = arr[0];
    for(var i = 0; i < arr.length; i++)
        max = arr[i] > max ? arr[i] : max;
    return max;
}

function avgValuesInArray(arr) {
    var sum = 0;
    for(var i = 0; i < arr.length; i++)
        sum += arr[i];
    return sum/arr.length;
}

function arrayOdd() {
    var arr = [];
    for(var i = 1; i <= 50; i+=2)
        arr.push(i);
}

function greaterThanY(Y, arr) {
    var count = 0;
    for(var i = 0; i < arr.length; i++)
        count += arr[i] > Y ? 1 : 0;
    return count;
}

function squares(arr) {
    for(var i = 0; i < arr.length; i++)
        arr[i] = arr[i] * arr[i];
    return arr;
}

function negatives(arr) {
    for(var i = 0; i < arr.length; i++)
        arr[i] = arr[i] < 0 ? 0 : arr[i];
    return arr;
}

function maxMinAvg(arr) {
    var max = arr[0];
    var min = arr[0];
    var sum = 0;

    for(var i = 0; i < arr.length; i++) {
        max = arr[i] > max ? arr[i] : max;
        min = arr[i] < min ? arr[i] : min;
        sum += arr[i];
    }

    return [max,min,sum/arr.length];
}

function swapFirstLast(arr) {
    [arr[0],arr[arr.length-1]] = [arr[arr.length-1],arr[0]];
}

function numberToString(arr) {
    for(var i = 0; i < arr.length; i++)
        arr[i] = arr[i] < 0 ? "Dojo" : arr[i];
}