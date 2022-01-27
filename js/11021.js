const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let output = '';

for(let i=1; i<=input[0]; i++) {
    let num = input[i].split(' ');
    console.log('Case #' + String(i)+ ': ' + (Number(num[0]) + Number(num[1])));
}
