const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

let num = parseInt(input[0]);

for (let i=1; i<=9; i++) console.log(num, '*' , i , '=', num * i);
