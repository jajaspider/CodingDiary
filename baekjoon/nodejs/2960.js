//https://www.acmicpc.net/problem/2960
const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim();
let input = fs.readFileSync("./input").toString().trim();

let N = input[0];
let K = input[0];

let sieve = [];

for (let i = 2; i < N; i += 1) {
  sieve.push(i);
}
while (sieve) {
  let tempNum = sieve[0];
}

sieve.findIndex();
