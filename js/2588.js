const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const a = Number(input[0]);
const b = Number(input[1]);
const b0 = b%10;
const b1 = (parseInt(b/10)%10);
const b2 = parseInt(b/100);
console.log(a*b0);
console.log(a*b1);
console.log(a*b2);
console.log(a*b);