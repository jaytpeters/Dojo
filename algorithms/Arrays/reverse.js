function reverse(arr) {
	for(var i = 0; i < arr.length/2; i++) {
		[arr[i], arr[arr.length-i-i]] = [arr[arr.length-i-1], arr[i]];
	}
}