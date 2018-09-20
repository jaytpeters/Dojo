function reverse (arr) {
  var last = arr.length - 1;
  var temp = 0;
  for(var begin = 0; begin < arr.length/2; begin++) {
    temp = arr[begin];
    arr[begin] = arr[last];
    arr[last] = temp;
    last--;              
  }
}
