// const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// let input = fs.readFileSync("./input").toString().trim().split("\n");
let numbers = [];

for (let i = 0; i < 10000; i += 1) {
  let number = i.toString().split("");
  let result = i;
  for (let n of number) {
    result += parseInt(n);
  }
  numbers.push(result);
}

for (let i = 0; i < 10000; i += 1) {
  let index = numbers.indexOf(i);
  if (index == -1) {
    console.dir(i);
  }
}
