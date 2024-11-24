const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// let input = fs.readFileSync("./input").toString().trim().split("\r\n");
let N = parseInt(input[0]);
for (let i = 1; i < N + 1; i += 1) {
  let left = [];
  let right = [];
  for (let j of input[i]) {
    // console.dir(j);
    if (j === "<") {
      if (left.length > 0) {
        right.push(left.pop());
      }
    } else if (j === ">") {
      if (right.length > 0) {
        left.push(right.pop());
      }
    } else if (j === "-") {
      if (left.length > 0) {
        left.pop();
      }
    } else {
      left.push(j);
    }
  }
  let leftString = left.join("");
  let rightString = right.reverse().join("");
  console.log(`${leftString}${rightString}`);
  //   console.dir(password);
  //   console.dir(input[i]);
}
