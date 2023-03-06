const cards1 = ["a", "apple", "is"];
const cards2 = ["a", "apple"];
const goal = ["a", "apple", "is", "a", "pear"];

console.log(solution(cards1, cards2, goal));

function solution(cards1, cards2, goal) {
  var answer = '';
  var a = 0;
  var b = 0;
  for(i=0; i<goal.length; i++) {
    if (goal[i] === cards1[a]) {
      a++;
    }
    else if (goal[i] === cards2[b]) {
      b++;
    }
    else {
      return "No";
    }
  }
  answer = "Yes";
  return answer;
}