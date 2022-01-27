// const readline = require("readline");

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });

// let str = '';

// let ans = 0;
// let flag = 0;
// function zip(top){
//     for(let i=top; i >= 0; i--) {
        
//         if (str[i] == '(') {
//             ans *= Number(str[i-1]);
//             flag = i-1;
//             return;
//         }
//         else if (str[i] == ')') {
//             zip(i-1);
//             i = flag;
//         }
//         else {//if (str[i] != '(' && str[i] != ')') {
//             ans ++;
//         }
//     }
//     return;
// }

// function sol() {
//     zip(str.length - 1);
//     console.log(ans);
// }

// rl.on('line', function (line) {
//     str = line.trim();
//     sol();
//     rl.close();
    
//   }).on('close', function () {
//     process.exit();
//   });


// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').trim().toString();

//const str = input[0];

const str = '33(562(71(9)))';


var tmp = 0;
var data = 0;
var flag = 0;
function zip(top){
    for(var i=top; i >= 0; i--) {
        
        if (str[i] === '(') {
            tmp *= Number(str[i-1]);
            flag = i-1;
            return;
        }
        else if (str[i] === ')') {
            data += tmp;
            tmp = 0;
            zip(i-1);
            i = flag;
        }
        else {//if (str[i] != '(' && str[i] != ')') {
            tmp ++;
        }
    }
    tmp += data;
    return;
}


zip(str.length-1);
console.log(tmp.toString());
