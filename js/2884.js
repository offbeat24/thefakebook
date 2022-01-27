let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let H = input[0];
let M = input[1];

solution(H, M);

function solution(H, M) {

    if (M >= 45) {
        console.log(H, M - 45);
    }
    else if (M < 45) {
        if (H != 0) {
            console.log(H - 1, 60 - (45 - M));
        }
        if (H == 0) {
            console.log(23, 60 - (45 - M));
        }
    }
}