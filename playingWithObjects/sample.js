var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];

for(var user in users) {
    if(users[user].name === "John") {
        console.log(users[user].age);
    }
}

 console.log(users[0].name);

 for(var user in users) {
     console.log(users[user].name + " - " + users[user].age);
 }