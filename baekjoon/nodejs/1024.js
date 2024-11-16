const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// const input = "32 6\n27 16 30 11 6 23".split("\n");

const N = input[0].split(" ")[0];
const M = input[0].split(" ")[1];
const target = input[1].split(" ");

const queue = [];
for (let i = 1; i < parseInt(N) + 1; i += 1) {
  queue.push(`${i}`);
}

let result = 0;
while (true) {
  if (target.length == 0) {
    break;
  }

  if (target[0] == queue[0]) {
    queue.shift();
    target.shift();
  } else {
    let targetIndex = queue.indexOf(target[0]);
    if (targetIndex < queue.length / 2) {
      queue.push(queue.shift());
      result += 1;
    } else {
      queue.unshift(queue.pop());
      result += 1;
    }
  }
}
console.log(result);
