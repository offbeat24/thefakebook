const keymap = ["AA"]
const targets = ["BA", "AAC"]

console.log(solution(keymap, targets));

function solution(keymap, targets) {
  var answer = [];
  targets.forEach(target => {
    var cnt = 0;
    var c = Infinity;
    [...target].forEach(char => {
      if (cnt === -1) {
        return false;
      }
      keymap.forEach(key => {
        t = key.indexOf(char) + 1;
        if (t > 0) {
          c = Math.min(t, c);
        }
      })
      if (c === Infinity) {
        cnt = -1;
        return false;
      }
      else {
        cnt += c;
      }
      c = Infinity;
    })
    answer.push(cnt);
    cnt = 0;
  })
  return answer;
}