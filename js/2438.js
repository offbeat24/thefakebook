const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();


let stars = "";
for(let i=0; i< input; i++){
    stars += '*';
    console.log(stars);
}

