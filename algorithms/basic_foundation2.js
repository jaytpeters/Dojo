function biggieSize(arr) {
    for(var i = 0; i < arr.length; i++)
        arr[i] = arr[i] > 0 ? "big" : arr[i];
    return arr;
}

function printLowReturnHigh(arr) {
    var low = arr[0];
    var high = arr[0];

    for(var i = 0; i < arr.length; i++) {
        low = arr[i] < low ? arr[i] : low;
        high = arr[i] > high ? arr[i] : high;
    }

    console.log(low);
    return high;
}

function printOneReturnAnother(arr) {
    console.log(arr[arr.length-2]);
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] % 2)
            return arr[i];
    }
}

function doubleVision(arr) {
    var newArr = [];
    for(var i = 0; i < arr.length; i++)
        newArr.push(arr[i]*2);
}

function countPositives(arr) {
    var count = 0;
    for(var i = 0; i < arr.length; i++)
        count += arr[i] > 0 ? 1 : 0;
    arr[arr.length-1] = count;
}

function evenOdds(arr) {
    var oddCount = 0;
    var evenCount = 0;

    for(var i = 0; i < arr.length; i++) {
        if(arr[i] % 2) {
            oddCount++;
            evenCount = 0;
        } else {
            evenCount++;
            oddCount = 0;
        }

        if(oddCount >= 3) {
            console.log("That's odd!");
            oddCount = 0;
        }

        if(evenCount >= 3) {
            console.log("Even more so!")
            eventCount = 0;
        }
    }
}

function incrementTheSeconds(arr) {
    for(var i = 0; i < arr.length; i++) {
        if(i % 2)
            arr[i]++;
        console.log(arr[i]);
    }

    return arr;
}

function previousLengths(arr) {
    var previousTemp = arr[0];
    var currentTemp = arr[1];
    for(var i = 1; i < arr.length; i++) {
        currentTemp = arr[i];
        arr[i] = previousTemp.length;
        previousTemp = currentTemp;
    }
        
    return arr;
}

function addSevenToMost(arr) {
    var newArr = [];
    for(var i = 1; i < arr.length; i++) {
        newArr.push(arr[i]+7);
    }

    return newArr;
}

function reverseArray(arr) {
    var temp = 0;
    for(var i = 0; i < arr.length/2; i++) {
        temp = arr[arr.length-1-i];
        arr[arr.length-1-i] = arr[i];
        arr[i] = temp;
    }

    return arr;
}

function outlookNegative(arr) {
    var newArr = [];
    for(var i = 0; i < arr.length; i++)
        newArr[i] = arr[i] > 0 ? arr[i] * -1 : arr[i];
    return newArr;
}

function alwaysHungry(arr) {
    var countFood = 0;

    for(var i = 0; i < arr.length; i++) {
        if(arr[i] == "food") {
            countFood++;
            console.log("yummy");
        }
    }

    if(countFood == 0)
        console.log("I'm hungry");
}

function swapTowardTheCenter(arr) {
    var temp;
    for(var i = 0; i < arr.length/2; i+=2) {
        temp = arr[arr.length-1-i];
        arr[arr.length-1-i] = arr[i];
        arr[i] = temp;
    }
}

function scaleTheArray(arr, num) {
    for(var i = 0; i < arr.length; i++)
        arr[i] = arr[i] * num;
    return arr;
}