const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [N, M, inventory] = input[0].split(" ");
N = parseInt(N);
M = parseInt(M);
inventory = parseInt(inventory);

let minHeight = Infinity;
let maxHeight = -Infinity;

const heightArray = new Array(257).fill(0);

for (let i = 1; i <= N; i++) {
  const row = input[i].split(" ").map(Number);
  for (const height of row) {
    heightArray[height]++;
    minHeight = Math.min(minHeight, height);
    maxHeight = Math.max(maxHeight, height);
  }
}

let time = Infinity;
let height = 0;

// 1차원배열 가장 낮은값부터 가장 높은값까지 수치 계산
// i는 목표치
for (let i = minHeight; i < maxHeight + 1; i += 1) {
  let count = 0;
  let usedBlock = 0;

  // j는 현재 배열의 값
  for (let j = minHeight; j <= maxHeight; j++) {
    const blockCount = heightArray[j];
    if (blockCount === 0) continue;

    if (j < i) {
      usedBlock -= (i - j) * blockCount;
      count += (i - j) * blockCount;
    } else if (j > i) {
      usedBlock += (j - i) * blockCount;
      count += (j - i) * blockCount * 2;
    }
  }

  if (usedBlock + inventory >= 0) {
    if (count < time || (count === time && i > height)) {
      time = count;
      height = i;
    }
  }
}

console.log(`${time} ${height}`);
