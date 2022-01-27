const fs = require('fs');
const inputData1 = fs.readFileSync('/dev/stdin').toString().split(' ');

const A = Number(inputData1[0]);
const B = Number(inputData1[1]);

console.log(A+B);
console.log(A-B);
console.log(A*B);
console.log(Math.floor(A/B));
console.log(A%B);