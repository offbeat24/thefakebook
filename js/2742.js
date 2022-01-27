const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let ans = '';
let cnt = Number(input[0]);

for (let i=cnt; i>0; i--) {
  ans += i + '\n';
}

console.log(ans);