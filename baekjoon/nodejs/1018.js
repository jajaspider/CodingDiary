const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// let input = "8 8\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBBBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW";
// input = input.split("\n");
const firstLine = input[0];
const N = parseInt(firstLine.split(" ")[0]);
const M = parseInt(firstLine.split(" ")[1]);

let n_arr;
for (let i = 0; i < N; i += 1) {
    n_arr = input.slice(1, N + 1);
}

function cal(x, y) {
    let result1 = 0;
    let result2 = 0;
    for (let i = x; i < x + 8; i += 1) {
        for (let j = y; j < y + 8; j += 1) {
            if ((i + j) % 2 == 0) {
                if (n_arr[j][i] == 'B') {
                    result1 += 1;
                }
            }
            else {
                if (n_arr[j][i] == 'W') {
                    result1 += 1;
                }
            }
        }
    }

    for (let i = x; i < x + 8; i += 1) {
        for (let j = y; j < y + 8; j += 1) {
            if ((i + j) % 2 == 0) {
                if (n_arr[j][i] == 'W') {
                    result2 += 1;
                }
            }
            else {
                if (n_arr[j][i] == 'B') {
                    result2 += 1;
                }
            }
        }
    }
    return Math.min(result1, result2);
}


let result = [];
for (let i = 0; i < N - 7; i += 1) {
    for (let j = 0; i < M - 7; i += 1) {
        result.push(cal(i, j));
    }
}
console.dir(Math.min(result));
// const n_arr = input.slice(1, n + 1);
// const [m, ...m_arr] = input.slice(n + 1);


