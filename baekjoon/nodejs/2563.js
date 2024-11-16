//https://www.acmicpc.net/problem/2563
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// let input = fs.readFileSync("./input").toString().trim().split("\r\n");

let grid = {};
for (let i = 0; i < 100; i += 1) {
  grid[i] = {};
  for (let j = 0; j < 100; j += 1) {
    grid[i][j] = 0;
  }
}

// console.dir(grid);

let n = parseInt(input[0]);

for (let i = 1; i < n + 1; i += 1) {
  for (
    let j = parseInt(input[i].split(" ")[0]);
    j < parseInt(input[i].split(" ")[0]) + 10;
    j += 1
  ) {
    for (
      let k = parseInt(input[i].split(" ")[1]);
      k < parseInt(input[i].split(" ")[1]) + 10;
      k += 1
    ) {
      grid[j][k] += 1;
    }
  }
}

let result = 0;
for (let i = 0; i < 100; i += 1) {
  for (let j = 0; j < 100; j += 1) {
    if (grid[i][j] > 0) {
      result += 1;
    }
  }
}
console.dir(result);
