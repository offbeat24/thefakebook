const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let ans = '';
let cnt = Number(input[0]);

for (let i=1; i<=cnt; i++) {
  ans += i + '\n';
}

console.log(ans);