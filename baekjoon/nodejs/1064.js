const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let input = fs.readFileSync("./input").toString().trim().split("\n");

// const Math = require("math");

input = input[0].split(" ");
let Xa = input[0];
let Ya = input[1];
let Xb = input[2];
let Yb = input[3];
let Xc = input[4];
let Yc = input[5];

if ((Xa === Xb) === Xc || (Ya === Yb) === Yc) {
  console.dir(-1);
  return;
}

const slope = (Yb - Ya) / (Xb - Xa);
const yIntercept = Ya - slope * Xa;
const y3 = slope * Xc + yIntercept;
console.dir(`${slope}x+${yIntercept}`);
console.dir(slope);
if (y3 == Yc) {
  console.dir(-1);
  return;
}

let lines = [];
lines.push(
  Math.sqrt(Math.abs(Math.pow(Xb - Xa, 2) + Math.pow(Yb - Ya, 2))).toFixed(15)
);
lines.push(
  Math.sqrt(Math.abs(Math.pow(Xc - Xb, 2) + Math.pow(Yc - Yb, 2))).toFixed(15)
);
lines.push(
  Math.sqrt(Math.abs(Math.pow(Xc - Xa, 2) + Math.pow(Yc - Ya, 2))).toFixed(15)
);

let result = Math.max.apply(Math, lines) * 2 - Math.min.apply(Math, lines) * 2;
console.dir(result);
