const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// let input = fs.readFileSync("./input").toString().trim().split("\r\n");

function binarySearch(arr, target) {
  let low = 0,
    high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);

    function compare(a, b) {
      if (a.L === b.L) return b.P - a.P;
      return a.L - b.L;
    }

    const cmp = compare(arr[mid], target);
    if (cmp < 0) {
      low = mid + 1;
    } else if (cmp > 0) {
      high = mid - 1;
    } else {
      return mid;
    }
  }
  return low;
}

const problems = new Map();
const sortedProblems = [];

const N = Number.parseInt(input[0]);
for (let i = 0; i < N; i += 1) {
  const [P, L] = input[i + 1].split(" ").map(Number);
  problems.set(P, L);
  const index = binarySearch(sortedProblems, { P, L });
  sortedProblems.splice(index, 0, { P, L });
}

const M = Number.parseInt(input[N + 1]);
for (let i = 0; i < M; i += 1) {
  const [command, arg1, arg2] = input[N + 2 + i].split(" ");
  const Num = Number.parseInt(arg1);
  const Num2 = Number.parseInt(arg2);

  if (command === "add") {
    if (problems.has(Num)) {
      const oldL = problems.get(Num);
      problems.set(Num, Num2);
      const oldIndex = binarySearch(sortedProblems, { P: Num, L: oldL });
      sortedProblems.splice(oldIndex, 1);
    } else {
      problems.set(Num, Num2);
    }
    const newIndex = binarySearch(sortedProblems, { P: Num, L: Num2 });
    sortedProblems.splice(newIndex, 0, { P: Num, L: Num2 });
  }

  if (command === "recommend") {
    if (Num === 1) {
      const target = sortedProblems[sortedProblems.length - 1];
      console.log(target.P);
    } else if (Num === -1) {
      const target = sortedProblems[0];
      console.log(target.P);
    }
  }

  if (command === "solved") {
    if (problems.has(Num)) {
      const L = problems.get(Num);
      problems.delete(Num);
      const index = binarySearch(sortedProblems, { P: Num, L });
      sortedProblems.splice(index, 1);
    }
  }
}
