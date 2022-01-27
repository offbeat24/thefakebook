const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let cnt = Number(input[0]);
let ans = '';

for (let i=1; i<=cnt; i++) {
  let num = input[i].split(' ');
  ans += Number(num[0]) + Number(num[1]) + '\n';
}

console.log(ans);