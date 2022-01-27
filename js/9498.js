const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

const sc = Number(input);

if(sc > 89) console.log('A');
else if(sc > 79) console.log('B');
else if(sc > 69) console.log('C');
else if(sc > 59) console.log('D');
else console.log('F');