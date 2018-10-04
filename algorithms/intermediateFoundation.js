function sigma(num) {
    var sum  = 0;
    for(var i = 1; i <= num; i++)
        sum += i;
    return sum;
}

function factorial(num) {
    var prod = 1;
    for(var i = 1; i <= num; i++)
        prod = prod * i;

    return prod;
}

function fibonacci(num) {
    if(num < 2)
        return num;

    var firstFib = 0;
    var secondFib = 1;
    var currentFib = 1;

    for(var i = 2; i < num; i++) {
        currentFib = firstFib + secondFib;
        firstFib = secondFib;
        secondFib = currentFib;    
    }

    return firstFib + secondFib;
}

function arraySecondToLast(arr) {
    if(arr.length < 2)
        return null;
    
    return arr[arr.length-2];
}

function arrayNthToLast(arr, n) {
    if(arr.length < n)
        return null;

    return arr[arr.length-n];
}

function arraySecondLargest(arr) {
    if(arr.length < 2)
        return null;

    var largest = arr[0];
    var secondLargest = arr[0];

    for(var i = 0; i < arr.length; i++) {
        if(arr[i] > largest) {
            secondLargest = largest;
            largest = arr[i];
        } else if((secondLargest == largest && arr[i] != secondLargest) || arr[i] > secondLargest)
            secondLargest = arr[i];
    }

    return secondLargest;
}

function doubleTrouble(arr) {
    var arrayLength = arr.length;

    for(var i = 0; i < arrayLength; i++)
        arr.push(arr[i]);
    for(var i = 0; i < arrayLength*2; i++) {
        arr[i] = arr[i+arrayLength-(Math.floor(i/2)+i%2)];
    }

    return arr;
}

function fibonacciRecursion(n) {
    if(n == 0)
        return 0;
    if(n == 1)
        return 1;

    return fibonacciRecursion(n-2) + fibonacciRecursion(n-1);
}